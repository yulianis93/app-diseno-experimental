"""Funciones reutilizables para el ANOVA de un factor (Diseño Completamente al Azar).

Todas las funciones usan nombres de columna genéricos, de modo que sirven para
cualquier base de datos con una columna de tratamientos y una de respuesta.
"""
from __future__ import annotations

import io

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd


def cargar_datos(archivo) -> pd.DataFrame:
    """Lee un archivo CSV (separador ',' o ';') o Excel (.xlsx).

    Args:
        archivo: Ruta de texto o archivo subido en Streamlit (con atributo ``name``).

    Returns:
        DataFrame con los datos leídos.
    """
    nombre = str(getattr(archivo, "name", archivo)).lower()
    if nombre.endswith((".xlsx", ".xls")):
        # Excel: pandas usa openpyxl para leer la primera hoja.
        return pd.read_excel(archivo)
    # CSV: sep=None con engine="python" detecta automáticamente ',' o ';'.
    if hasattr(archivo, "read"):
        contenido = archivo.read()
        if isinstance(contenido, bytes):
            contenido = contenido.decode("utf-8-sig")
        return pd.read_csv(io.StringIO(contenido), sep=None, engine="python")
    return pd.read_csv(archivo, sep=None, engine="python", encoding="utf-8-sig")


def validar_dca(df: pd.DataFrame, col_trat: str, col_resp: str) -> list[str]:
    """Revisa que los datos sirvan para un DCA.

    Args:
        df: Datos.
        col_trat: Nombre de la columna de tratamientos.
        col_resp: Nombre de la columna de la variable respuesta.

    Returns:
        Lista de mensajes de error en español. Vacía si todo está bien.
    """
    errores: list[str] = []
    faltan = [c for c in (col_trat, col_resp) if c not in df.columns]
    if faltan:
        return [f"Faltan las columnas: {', '.join(faltan)}."]
    if col_trat == col_resp:
        return ["La columna de tratamientos y la de respuesta deben ser distintas."]
    if not pd.api.types.is_numeric_dtype(df[col_resp]):
        errores.append(f"La respuesta '{col_resp}' debe ser numérica.")
    if df[[col_trat, col_resp]].isna().any().any():
        errores.append("Hay datos faltantes en las columnas elegidas.")
    if errores:
        return errores
    conteo = df[col_trat].value_counts()
    if len(conteo) < 2:
        errores.append("Se necesitan al menos 2 tratamientos.")
    if (conteo < 2).any():
        errores.append("Cada tratamiento debe tener al menos 2 réplicas.")
    return errores


def ajustar_dca(df: pd.DataFrame, col_trat: str, col_resp: str):
    """Ajusta el modelo lineal Y = mu + tau_i + e_ij.

    Q("...") protege nombres con espacios o tildes dentro de la fórmula.
    """
    d = df[[col_trat, col_resp]].rename(columns={col_trat: "trat", col_resp: "resp"})
    return smf.ols('Q("resp") ~ C(Q("trat"))', data=d).fit()


def tabla_anova(modelo) -> pd.DataFrame:
    """Construye la tabla ANOVA en español: Fuente, gl, SC, CM, F, p-valor."""
    # anova_lm(typ=2): con un solo factor equivale al ANOVA clásico.
    a = anova_lm(modelo, typ=2)
    sc_trat, sc_err = a.iloc[0]["sum_sq"], a.iloc[1]["sum_sq"]
    gl_trat, gl_err = a.iloc[0]["df"], a.iloc[1]["df"]
    tabla = pd.DataFrame({
        "Fuente": ["Tratamientos", "Error", "Total"],
        "gl": [gl_trat, gl_err, gl_trat + gl_err],
        "SC": [sc_trat, sc_err, sc_trat + sc_err],
        # CM = SC / gl (cuadrado medio)
        "CM": [sc_trat / gl_trat, sc_err / gl_err, np.nan],
        # F = CM_trat / CM_error
        "F": [a.iloc[0]["F"], np.nan, np.nan],
        "p-valor": [a.iloc[0]["PR(>F)"], np.nan, np.nan],
    })
    return tabla


def resumen_tratamientos(df: pd.DataFrame, col_trat: str, col_resp: str) -> pd.DataFrame:
    """n, total, media y desviación estándar por tratamiento."""
    g = df.groupby(col_trat, sort=True)[col_resp]
    return pd.DataFrame({
        "n": g.count(),
        "Total": g.sum(),
        "Media": g.mean(),
        "Desv. estándar": g.std(ddof=1),
    }).reset_index()


def coeficiente_variacion(modelo, df: pd.DataFrame, col_resp: str) -> float:
    """CV (%) = raíz(CME) / media general * 100."""
    cme = modelo.mse_resid  # cuadrado medio del error
    return float(np.sqrt(cme) / df[col_resp].mean() * 100)


def tukey(df: pd.DataFrame, col_trat: str, col_resp: str,
          alfa: float = 0.05) -> tuple[pd.DataFrame, float]:
    """Prueba de Tukey y DMS.

    DMS = q(alfa; t; glE) * raíz(CME / r), con q de scipy.stats.studentized_range.
    Si el diseño no es balanceado la DMS usa la media armónica de r (aproximada).

    Returns:
        (comparaciones por pares en español, DMS)
    """
    res = pairwise_tukeyhsd(df[col_resp], df[col_trat].astype(str), alpha=alfa)
    pares = pd.DataFrame(res._results_table.data[1:], columns=res._results_table.data[0])
    pares.columns = ["Grupo 1", "Grupo 2", "Dif. de medias", "p ajustado",
                     "Límite inf.", "Límite sup.", "Rechaza H0"]
    modelo = ajustar_dca(df, col_trat, col_resp)
    t = df[col_trat].nunique()
    gl_error = modelo.df_resid
    n_rep = df.groupby(col_trat)[col_resp].count()
    r = stats.hmean(n_rep) if n_rep.nunique() > 1 else n_rep.iloc[0]
    q = stats.studentized_range.ppf(1 - alfa, t, gl_error)
    dms = float(q * np.sqrt(modelo.mse_resid / r))
    return pares, dms


def letras_tukey(df: pd.DataFrame, col_trat: str, col_resp: str, dms: float) -> pd.DataFrame:
    """Asigna letras de grupo (medias con la misma letra no difieren) usando la DMS."""
    medias = df.groupby(col_trat)[col_resp].mean().sort_values()
    nombres, valores = list(medias.index), list(medias.values)
    letras = {n: "" for n in nombres}
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    k = 0
    grupos: list[tuple[int, int]] = []
    for i in range(len(nombres)):
        j = i
        while j + 1 < len(nombres) and valores[j + 1] - valores[i] <= dms:
            j += 1
        if not any(a <= i and j <= b for a, b in grupos):
            grupos.append((i, j))
    for a, b in grupos:
        for idx in range(a, b + 1):
            letras[nombres[idx]] += alfabeto[k]
        k += 1
    return pd.DataFrame({col_trat: nombres, "Media": valores,
                         "Grupo": [letras[n] for n in nombres]})


def supuestos(df: pd.DataFrame, col_trat: str, col_resp: str, modelo) -> dict:
    """Shapiro-Wilk sobre residuos y Levene (mediana) entre tratamientos."""
    sw = stats.shapiro(modelo.resid)
    grupos = [g[col_resp].values for _, g in df.groupby(col_trat)]
    lv = stats.levene(*grupos, center="median")
    return {"shapiro_W": float(sw.statistic), "shapiro_p": float(sw.pvalue),
            "levene_W": float(lv.statistic), "levene_p": float(lv.pvalue)}


def interpretar_dca(tabla: pd.DataFrame, alfa: float = 0.05) -> str:
    """Texto sencillo con la decisión sobre H0."""
    f, p = tabla.loc[0, "F"], tabla.loc[0, "p-valor"]
    if p < alfa:
        return (f"F = {f:.3f}, p = {p:.4g} < {alfa}: se **rechaza H0**. Al menos un "
                "tratamiento tiene media distinta; use la prueba de Tukey para saber cuáles.")
    return (f"F = {f:.3f}, p = {p:.4g} ≥ {alfa}: **no se rechaza H0**. No hay evidencia de "
            "diferencias entre tratamientos; no corresponde hacer comparaciones múltiples.")
