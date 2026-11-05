# Instrucciones permanentes para el agente

- Proyecto: App de Diseño Experimental en Python y Streamlit, curso de Diseño Experimental, Ingeniería Agrícola, Universidad de Sucre.
- Estructura: `app.py` (portada), `pages/` (un archivo por diseño), `utils/` (funciones reutilizables, con `__init__.py`), `data/` (CSV de ejemplo), `verificacion/` (scripts de R).
- Todo el código, comentarios, docstrings y mensajes de la interfaz en español.
- Cada paso estadístico lleva un comentario que explique qué calcula y por qué, pensado para estudiantes de Ingeniería Agrícola.
- Funciones con type hints y docstrings estilo Google.
- Librerías permitidas: streamlit, pandas, numpy, scipy, statsmodels, plotly, openpyxl. No agregues otras sin pedir permiso.
- Los ANOVA se ajustan con `statsmodels.formula.api.ols` y `statsmodels.stats.anova.anova_lm(typ=2)`. Tukey con `statsmodels.stats.multicomp.pairwise_tukeyhsd`.
- No inventes resultados: los números salen siempre del cálculo.
- Antes de terminar una tarea, ejecuta el código y corrige los errores que aparezcan.
