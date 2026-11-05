# App de Diseño Experimental

App en Streamlit para el curso de Diseño Experimental (Ingeniería Agrícola, Universidad de Sucre, 2026-2).
Incluye la portada con el menú de 6 módulos y el módulo **DCA** (ANOVA de un factor, medias, boxplot,
Tukey, supuestos de Shapiro-Wilk y Levene). Los demás módulos están en construcción.

## Ejecutar

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Estructura

| Carpeta / archivo | Para qué sirve |
|---|---|
| `app.py` | Portada de la app |
| `pages/` | Un archivo por diseño experimental |
| `utils/anova_utils.py` | Funciones estadísticas reutilizables |
| `data/` | Datos de ejemplo (`dca_secadores.csv`) |
| `verificacion/` | Script de R para contrastar los resultados |
| `BITACORA_IA.md` | Registro del uso de IA |

## Ejemplo

Humedad final de rodajas de yuca en 4 secadores solares (4 réplicas cada uno).

Autor: Yulianis Celada
