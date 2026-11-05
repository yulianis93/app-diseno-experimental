"""Portada de la App de Diseño Experimental."""
import pandas as pd
import streamlit as st

AUTOR = "yulianis celada"

st.set_page_config(page_title="App de Diseño Experimental", page_icon="🌱", layout="wide")

st.title("🌱 App de Diseño Experimental")
st.subheader("Ingeniería Agrícola – Universidad de Sucre")
st.write(
    "El diseño experimental permite planear ensayos en campo, invernadero o laboratorio "
    "para comparar tratamientos (variedades, dosis de fertilizante, sistemas de riego, "
    "secadores, etc.) controlando el error experimental y tomando decisiones técnicas "
    "con respaldo estadístico, no solo con la intuición."
)

modulos = pd.DataFrame([
    ("DCA", "Diseño Completamente al Azar", "Unidades experimentales homogéneas (invernadero, laboratorio)", "Comparar 4 secadores solares por la humedad final de la yuca", "Disponible"),
    ("DBCA", "Diseño en Bloques Completos al Azar", "Hay un gradiente que se puede bloquear (pendiente, fertilidad)", "Comparar variedades de maíz en bloques según la pendiente del lote", "En construcción"),
    ("DCL", "Diseño en Cuadrado Latino", "Dos fuentes de variación que se bloquean a la vez (filas y columnas)", "Comparar dosis de abono con gradiente de humedad y de luz", "En construcción"),
    ("DPD", "Diseño en Parcelas Divididas", "Un factor difícil de aplicar en parcelas grandes y otro en subparcelas", "Riego en parcelas principales y variedades en subparcelas", "En construcción"),
    ("Factoriales", "Experimentos factoriales", "Se estudian varios factores y sus interacciones", "Dosis de N × densidad de siembra en arroz", "En construcción"),
    ("RSM", "Metodología de superficie de respuesta", "Buscar el óptimo de una respuesta con factores continuos", "Temperatura y tiempo óptimos de secado", "En construcción"),
], columns=["Módulo", "Nombre completo", "Cuándo se usa", "Ejemplo agrícola", "Estado"])
st.subheader("Módulos")
st.dataframe(modulos, hide_index=True, width="stretch")

st.subheader("Cómo usar la app")
st.markdown(
    "1. **Elija el módulo** en el menú lateral (hoy solo el DCA está disponible).\n"
    "2. **Cargue sus datos** (CSV o Excel) o use el ejemplo incluido.\n"
    "3. **Revise los resultados**: ANOVA, medias, gráficas, Tukey y supuestos.\n"
    "4. **Verifique a mano**: compare con su cálculo en papel antes de aceptar la salida."
)
st.warning("Esta app apoya el aprendizaje. El estudiante interpreta los resultados, "
           "verifica supuestos y compara con su cálculo manual.")

with st.sidebar:
    st.markdown(f"**Autor:** {AUTOR}")
    st.markdown("**Curso:** Diseño Experimental")
    st.markdown("**Semestre:** 2026-2")
