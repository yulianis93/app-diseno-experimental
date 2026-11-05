# Bitácora de uso de IA — Actividad 1 (DCA)

Estudiante: Yulianis Celada · Ruta: **B** (agente externo: Claude)

> Los campos marcados con **COMPLETAR** son suyos: la fecha de cada paso, qué corrigió
> usted y por qué. La rúbrica (C5) califica la reflexión propia, no solo el texto generado.

### Prompt 0 — Instrucciones permanentes
- Ruta: B (agente externo: Claude)
- Fecha: 2026-11-03
- Qué generó la IA (archivos): `.github/copilot-instructions.md`
- Qué acepté sin cambios: todas las reglas del enunciado
- Qué corregí y por qué: **COMPLETAR**
- Cómo lo verifiqué: revisé que el archivo existiera y coincidiera con el prompt

### Prompt 1 — Estructura del proyecto y librerías
- Ruta: B (agente externo: Claude)
- Fecha: 2026-11-03
- Qué generó la IA (archivos): carpetas `pages/ utils/ data/ verificacion/`, `utils/__init__.py`, `requirements.txt`, `.gitignore`, `data/dca_secadores.csv`
- Qué acepté sin cambios: estructura y datos base de los 16 valores
- Qué corregí y por qué: **COMPLETAR** (si cambió algún dato a su variante con k, anótelo aquí)
- Cómo lo verifiqué: `python -c "import streamlit, statsmodels"` y conté 16 filas en el CSV

### Prompt 2 — Interfaz: portada y menú
- Ruta: B (agente externo: Claude)
- Fecha: 2026-11-03
- Qué generó la IA (archivos): `app.py` y `pages/01_DCA.py` … `06_RSM.py`
- Qué acepté sin cambios: tabla de 6 módulos, advertencia académica, barra lateral
- Qué corregí y por qué: puse mi nombre en la constante `AUTOR`; **COMPLETAR** otros cambios
- Cómo lo verifiqué: abrí cada página con `streamlit.testing.AppTest` sin excepciones; **COMPLETAR**: captura de `streamlit run app.py`

### Prompt 3 — Funciones estadísticas
- Ruta: B (agente externo: Claude)
- Fecha: 2026-11-03
- Qué generó la IA (archivos): `utils/anova_utils.py` (cargar, validar, ajustar, tabla ANOVA, resumen, CV, Tukey, letras, supuestos, interpretación)
- Qué acepté sin cambios: **COMPLETAR**
- Qué corregí y por qué: **COMPLETAR**
- Cómo lo verifiqué: comparé la tabla impresa con un cálculo independiente por las fórmulas del enunciado (tabla de abajo)

### Prompt 4 — Módulo DCA
- Ruta: B (agente externo: Claude)
- Fecha: 2026-11-03
- Qué generó la IA (archivos): `pages/01_DCA.py` (carga CSV/Excel, ANOVA, medias, boxplot, Tukey condicionado al p-valor, Shapiro-Wilk, Levene, residuos y Q-Q)
- Qué acepté sin cambios: **COMPLETAR**
- Qué corregí y por qué: **COMPLETAR**
- Cómo lo verifiqué: la página corre sin errores y muestra los mismos números de la tabla de abajo

### Prompt 5/6 — Script de R y verificación
- Ruta: B (agente externo: Claude)
- Fecha: 2026-11-03
- Qué generó la IA (archivos): `verificacion/verificacion_dca.R`
- Qué acepté sin cambios: **COMPLETAR**
- Qué corregí y por qué: **COMPLETAR**
- Cómo lo verifiqué: **COMPLETAR — ejecute el script en R y pegue la salida en el .R**

## Tabla de verificación (datos base, k = 0)

| Cantidad | Mano (fórmulas) | App (Python) | R |
|---|---|---|---|
| Gran total Y.. | 210,6 | 210,6 | COMPLETAR |
| Factor de corrección | 2772,0225 | — | — |
| SC Tratamientos | 11,9275 | 11,9275 | COMPLETAR |
| SC Error | 1,9300 | 1,9300 | COMPLETAR |
| SC Total | 13,8575 | 13,8575 | COMPLETAR |
| CM Tratamientos | 3,9758 | 3,9758 | COMPLETAR |
| CM Error | 0,1608 | 0,1608 | COMPLETAR |
| F (3; 12) | 24,72 | 24,72 | COMPLETAR |
| p-valor | 2,0e-05 | 2,0e-05 | COMPLETAR |
| DMS Tukey (q = 4,1987) | 0,8419 | 0,8419 | COMPLETAR |
| CV | 3,05 % | 3,05 % | COMPLETAR |

Diferencias de redondeo: en el enunciado q(0,05; 4; 12) = 4,20 (dos decimales); el
valor exacto es 4,1987, por eso a mano la DMS sale 0,8431 con 4,20 y 0,8419 con el exacto.
**Esta tabla es con los datos base. Con su variante (k = último dígito del código ÷ 10 sumado
al secador D) los números cambian: repita la comparación con sus datos.**

## Pregunta de reserva cognitiva
Al sumar la misma constante k a todas las observaciones de un tratamiento, la **SC Error no
cambia** (cada dato se mueve igual que la media de su grupo, así que las desviaciones dentro
del grupo son las mismas). Lo que cambia es la SC Tratamientos y, por tanto, F. Comprobado
con k = 0,7 en D: SC Error = 1,9300 (igual), SC Trat 11,9275 → 14,7275, F 24,72 → 30,52.
