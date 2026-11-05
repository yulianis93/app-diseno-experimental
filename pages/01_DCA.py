"""Módulo DCA: ANOVA de un factor, Tukey y supuestos."""
import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils import anova_utils as au  # noqa: E402

st.set_page_config(page_title="DCA", page_icon="🌱", layout="wide")
st.title("DCA – Diseño Completamente al Azar")
st.write("Compara las medias de **t tratamientos** asignados al azar a unidades "
         "experimentales homogéneas. Modelo: Yij = μ + τi + εij.")

RUTA_EJEMPLO = Path(__file__).resolve().parent.parent / "data" / "dca_secadores.csv"

# ---------- 1. Datos ----------
st.header("1. Datos")
archivo = st.file_uploader("Cargue un CSV (, o ;) o Excel (.xlsx)", type=["csv", "xlsx"])
try:
    if archivo is not None:
        df = au.cargar_datos(archivo)
    else:
        st.caption("Usando el ejemplo: humedad final de yuca en 4 secadores solares.")
        df = au.cargar_datos(str(RUTA_EJEMPLO))
except Exception as e:  # noqa: BLE001
    st.error(f"No se pudo leer el archivo: {e}")
    st.stop()

c1, c2 = st.columns(2)
col_trat = c1.selectbox("Columna de tratamientos", df.columns, index=0)
numericas = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c]) and c != col_trat]
col_resp = c2.selectbox("Columna de respuesta", numericas or list(df.columns), index=len(numericas) - 1 if numericas else 0)

with st.expander("Opcional: sumar una constante k a un tratamiento (su variante / reserva cognitiva)"):
    trat_k = st.selectbox("Tratamiento", ["(ninguno)"] + sorted(df[col_trat].astype(str).unique()))
    k = st.number_input("k", value=0.0, step=0.1, format="%.1f")
    if trat_k != "(ninguno)" and k != 0:
        df = df.copy()
        df.loc[df[col_trat].astype(str) == trat_k, col_resp] += k
        st.info(f"Se sumó k = {k} a las observaciones del tratamiento {trat_k}.")
st.dataframe(df, hide_index=True, width="stretch")

errores = au.validar_dca(df, col_trat, col_resp)
if errores:
    for e in errores:
        st.error(e)
    st.stop()
alfa = st.select_slider("Nivel de significancia α", [0.01, 0.05, 0.10], value=0.05)

modelo = au.ajustar_dca(df, col_trat, col_resp)

# ---------- 2. ANOVA ----------
st.header("2. Tabla ANOVA")
tabla = au.tabla_anova(modelo)
st.dataframe(tabla.style.format({"gl": "{:.0f}", "SC": "{:.4f}", "CM": "{:.4f}",
                                 "F": "{:.4f}", "p-valor": "{:.6f}"}, na_rep=""),
             hide_index=True, width="stretch")
m1, m2 = st.columns(2)
m1.metric("Coeficiente de variación", f"{au.coeficiente_variacion(modelo, df, col_resp):.2f} %")
m2.metric("Media general", f"{df[col_resp].mean():.4f}")
st.markdown(au.interpretar_dca(tabla, alfa))

# ---------- 3. Medias y gráfica ----------
st.header("3. Medias por tratamiento")
st.dataframe(au.resumen_tratamientos(df, col_trat, col_resp).round(4), hide_index=True,
             width="stretch")
fig = px.box(df, x=col_trat, y=col_resp, points="all", color=col_trat,
             title=f"{col_resp} por {col_trat}")
st.plotly_chart(fig, width="stretch")

# ---------- 4. Tukey (solo si se rechaza H0) ----------
st.header("4. Prueba de Tukey")
p_global = tabla.loc[0, "p-valor"]
if p_global < alfa:
    pares, dms = au.tukey(df, col_trat, col_resp, alfa)
    if df.groupby(col_trat)[col_resp].count().nunique() > 1:
        st.warning("Diseño no balanceado: la DMS es aproximada (media armónica de r).")
    st.metric("DMS de Tukey", f"{dms:.4f}")
    st.dataframe(pares.round(4), hide_index=True, width="stretch")
    st.subheader("Grupos (medias con la misma letra no difieren)")
    st.dataframe(au.letras_tukey(df, col_trat, col_resp, dms).round(4), hide_index=True,
                 width="stretch")
else:
    st.info("No se rechazó H0: no corresponde aplicar Tukey.")

# ---------- 5. Supuestos ----------
st.header("5. Supuestos del modelo")
s = au.supuestos(df, col_trat, col_resp, modelo)
a1, a2 = st.columns(2)
a1.metric("Shapiro-Wilk (normalidad de residuos)", f"p = {s['shapiro_p']:.4f}")
a2.metric("Levene (homogeneidad de varianzas)", f"p = {s['levene_p']:.4f}")
st.write("Normalidad: " + ("**se cumple**" if s["shapiro_p"] >= alfa else "**no se cumple**")
         + f" (W = {s['shapiro_W']:.4f}). Homogeneidad: "
         + ("**se cumple**" if s["levene_p"] >= alfa else "**no se cumple**")
         + f" (W = {s['levene_W']:.4f}). Con p ≥ α no hay evidencia contra el supuesto.")
g1, g2 = st.columns(2)
g1.plotly_chart(px.histogram(x=modelo.resid, nbins=8, title="Histograma de residuos",
                             labels={"x": "Residuo"}), width="stretch")
g2.plotly_chart(px.scatter(x=modelo.fittedvalues, y=modelo.resid,
                           title="Residuos vs. valores ajustados",
                           labels={"x": "Ajustado", "y": "Residuo"}), width="stretch")
