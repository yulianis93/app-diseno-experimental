# Bitácora de uso de IA — Actividad 1 (DCA)

Estudiante: Yulianis Celada · Ruta: **B** (agente externo: Claude) · Variante: k = 0,4 (código termina en 4)

### Prompt 0 — Instrucciones permanentes
- Ruta: B (agente externo: Claude)
- Fecha: generado 2026-11-03; aplicado 2026-11-04
- Qué generó la IA (archivos): `.github/copilot-instructions.md`
- Qué acepté sin cambios: todas las reglas del enunciado
- Qué corregí y por qué: nada; el archivo coincidía con el prompt del enunciado
- Cómo lo verifiqué: revisé que el archivo existiera en `.github/` y lo subí con commit

### Prompt 1 — Estructura del proyecto y librerías
- Ruta: B (agente externo: Claude)
- Fecha: generado 2026-11-03; aplicado 2026-11-04
- Qué generó la IA (archivos): carpetas `pages/ utils/ data/ verificacion/`, `utils/__init__.py`, `requirements.txt`, `.gitignore`, `data/dca_secadores.csv`
- Qué acepté sin cambios: la estructura y los 16 datos base del CSV
- Qué corregí y por qué: al copiar los archivos al Codespace quedaron sueltos en la carpeta principal, y Python no encontraba `utils`; los moví a sus carpetas con `mv` y rehice los commits. El CSV queda con datos base (k = 0); mi k = 0,4 lo aplico al secador D desde la app y desde el script de R. Al `.gitignore` de GitHub le agregué `exports/` y `.streamlit/secrets.toml`.
- Cómo lo verifiqué: `pip install -r requirements.txt` y corrí las funciones con `python -c`, que imprimió la tabla ANOVA

### Prompt 2 — Interfaz: portada y menú
- Ruta: B (agente externo: Claude)
- Fecha: generado 2026-11-03; aplicado 2026-11-04
- Qué generó la IA (archivos): `app.py` y `pages/01_DCA.py` a `pages/06_RSM.py`
- Qué acepté sin cambios: tabla de 6 módulos, advertencia académica y barra lateral
- Qué corregí y por qué: cambié la constante `AUTOR` por mi nombre, porque el archivo traía un texto de ejemplo
- Cómo lo verifiqué: ejecuté `streamlit run app.py`, abrí el menú de las 6 páginas y tomé la captura de la portada

### Prompt 3 — Funciones estadísticas
- Ruta: B (agente externo: Claude)
- Fecha: generado 2026-11-03; aplicado 2026-11-04
- Qué generó la IA (archivos): `utils/anova_utils.py` (cargar, validar, ajustar, tabla ANOVA, resumen, CV, Tukey, letras, supuestos, interpretación)
- Qué acepté sin cambios: las funciones y sus comentarios con las fórmulas
- Qué corregí y por qué: nada en el código; las probé con mi variante (k = 0,4 al secador D) para compararlas con mi Fase 1
- Cómo lo verifiqué: la salida dio SC Trat 13,1675, SC Error 1,9300, F 27,2902, CV 3,02 y DMS 0,8419, que coinciden con mi hoja a mano

### Prompt 4 — Módulo DCA
- Ruta: B (agente externo: Claude)
- Fecha: generado 2026-11-03; aplicado 2026-11-04
- Qué generó la IA (archivos): `pages/01_DCA.py` (carga CSV/Excel, ANOVA, medias, boxplot, Tukey condicionado al p-valor, Shapiro-Wilk, Levene y gráficas de residuos)
- Qué acepté sin cambios: el módulo completo, incluida la opción de sumar k a un tratamiento
- Qué corregí y por qué: nada en el código; usé la opción de k con D y k = 0,4 para trabajar con mi variante
- Cómo lo verifiqué: la tabla ANOVA de la app coincide con mi Fase 1 (SC Trat 13,1675, SC Error 1,9300, F 27,29) y tomé la captura

### Prompt 5/6 — Script de R y verificación
- Ruta: B (agente externo: Claude)
- Fecha: generado 2026-11-03; aplicado 2026-11-04
- Qué generó la IA (archivos): `verificacion/verificacion_dca.R`
- Qué acepté sin cambios: ANOVA, Tukey, Shapiro-Wilk y Bartlett
- Qué corregí y por qué: el script original no tenía la variable `k` y daba los datos base (F = 24,72); lo reemplacé por uno con `k <- 0.4` para que use mi variante
- Cómo lo verifiqué: ejecuté `Rscript verificacion/verificacion_dca.R`, obtuve F = 27,29 y DMS = 0,8419, y pegué la salida como comentario en el .R

## Tabla de verificación con mi variante (k = 0,4)

| Cantidad | Mano (mi hoja) | App (Python) | R |
|---|---|---|---|
| Gran total Y.. | 212,2 | 212,2 | — |
| Factor de corrección | 2814,30 | — | — |
| SC Tratamientos | 13,16 | 13,1675 | 13,17 |
| SC Error | 1,93 | 1,9300 | 1,93 |
| SC Total | 15,09 | 15,0975 | — |
| CM Tratamientos | 4,38 | 4,3892 | 4,389 |
| CM Error | 0,16 | 0,1608 | 0,161 |
| F (3; 12) | 27,29 | 27,2902 | 27,29 |
| p-valor | < 0,0001 | 1,2e-05 | 1,21e-05 |
| DMS Tukey | 0,842 | 0,8419 | 0,8419 |
| CV | 3,02 % | 3,02 % | 3,0239 % |

Diferencias de redondeo: a mano trabajé con 2 decimales y q = 4,20; Python y R usan q = 4,1987, por eso la DMS pasa de 0,842 a 0,8419. Con 4,20 a mano la DMS exacta es 0,8422.

## Tabla de verificación con datos base (k = 0)

| Cantidad | Mano (fórmulas) | App (Python) | R |
|---|---|---|---|
| Gran total Y.. | 210,6 | 210,6 | — |
| Factor de corrección | 2772,0225 | — | — |
| SC Tratamientos | 11,9275 | 11,9275 | 11,93 |
| SC Error | 1,9300 | 1,9300 | 1,93 |
| SC Total | 13,8575 | 13,8575 | — |
| CM Tratamientos | 3,9758 | 3,9758 | 3,976 |
| CM Error | 0,1608 | 0,1608 | 0,161 |
| F (3; 12) | 24,72 | 24,72 | 24,72 |
| p-valor | 2,0e-05 | 2,0e-05 | 2,01e-05 |
| DMS Tukey (q = 4,1987) | 0,8419 | 0,8419 | 0,8419 |
| CV | 3,05 % | 3,05 % | 3,04684 % |

## Supuestos
Shapiro-Wilk (normalidad de residuos) da W = 0,939 y p = 0,337 tanto en Python como en R. Para homogeneidad de varianzas la app usa Levene y R usa Bartlett; son pruebas distintas, por eso sus p-valores no son iguales, pero ambas llevan a no rechazar la homogeneidad.

## Pregunta de reserva cognitiva
Al sumar la misma constante k a todas las observaciones de un tratamiento, la **SC Error no cambia**: cada dato se mueve igual que la media de su grupo, así que las desviaciones dentro del grupo son las mismas. Lo que cambia es la SC Tratamientos y, por tanto, F. Lo comprobé: con k = 0 la SC Error es 1,9300 y con k = 0,4 también es 1,93, mientras la SC Tratamientos pasó de 11,9275 a 13,1675 y F de 24,72 a 27,29.
EOFcat > BITACORA_IA.md <<'EOF'
# Bitácora de uso de IA — Actividad 1 (DCA)

Estudiante: Yulianis Celada · Ruta: **B** (agente externo: Claude) · Variante: k = 0,4 (código termina en 4)

### Prompt 0 — Instrucciones permanentes
- Ruta: B (agente externo: Claude)
- Fecha: generado 2026-11-03; aplicado 2026-11-04
- Qué generó la IA (archivos): `.github/copilot-instructions.md`
- Qué acepté sin cambios: todas las reglas del enunciado
- Qué corregí y por qué: nada; el archivo coincidía con el prompt del enunciado
- Cómo lo verifiqué: revisé que el archivo existiera en `.github/` y lo subí con commit

### Prompt 1 — Estructura del proyecto y librerías
- Ruta: B (agente externo: Claude)
- Fecha: generado 2026-11-03; aplicado 2026-11-04
- Qué generó la IA (archivos): carpetas `pages/ utils/ data/ verificacion/`, `utils/__init__.py`, `requirements.txt`, `.gitignore`, `data/dca_secadores.csv`
- Qué acepté sin cambios: la estructura y los 16 datos base del CSV
- Qué corregí y por qué: al copiar los archivos al Codespace quedaron sueltos en la carpeta principal, y Python no encontraba `utils`; los moví a sus carpetas con `mv` y rehice los commits. El CSV queda con datos base (k = 0); mi k = 0,4 lo aplico al secador D desde la app y desde el script de R. Al `.gitignore` de GitHub le agregué `exports/` y `.streamlit/secrets.toml`.
- Cómo lo verifiqué: `pip install -r requirements.txt` y corrí las funciones con `python -c`, que imprimió la tabla ANOVA

### Prompt 2 — Interfaz: portada y menú
- Ruta: B (agente externo: Claude)
- Fecha: generado 2026-11-03; aplicado 2026-11-04
- Qué generó la IA (archivos): `app.py` y `pages/01_DCA.py` a `pages/06_RSM.py`
- Qué acepté sin cambios: tabla de 6 módulos, advertencia académica y barra lateral
- Qué corregí y por qué: cambié la constante `AUTOR` por mi nombre, porque el archivo traía un texto de ejemplo
- Cómo lo verifiqué: ejecuté `streamlit run app.py`, abrí el menú de las 6 páginas y tomé la captura de la portada

### Prompt 3 — Funciones estadísticas
- Ruta: B (agente externo: Claude)
- Fecha: generado 2026-11-03; aplicado 2026-11-04
- Qué generó la IA (archivos): `utils/anova_utils.py` (cargar, validar, ajustar, tabla ANOVA, resumen, CV, Tukey, letras, supuestos, interpretación)
- Qué acepté sin cambios: las funciones y sus comentarios con las fórmulas
- Qué corregí y por qué: nada en el código; las probé con mi variante (k = 0,4 al secador D) para compararlas con mi Fase 1
- Cómo lo verifiqué: la salida dio SC Trat 13,1675, SC Error 1,9300, F 27,2902, CV 3,02 y DMS 0,8419, que coinciden con mi hoja a mano

### Prompt 4 — Módulo DCA
- Ruta: B (agente externo: Claude)
- Fecha: generado 2026-11-03; aplicado 2026-11-04
- Qué generó la IA (archivos): `pages/01_DCA.py` (carga CSV/Excel, ANOVA, medias, boxplot, Tukey condicionado al p-valor, Shapiro-Wilk, Levene y gráficas de residuos)
- Qué acepté sin cambios: el módulo completo, incluida la opción de sumar k a un tratamiento
- Qué corregí y por qué: nada en el código; usé la opción de k con D y k = 0,4 para trabajar con mi variante
- Cómo lo verifiqué: la tabla ANOVA de la app coincide con mi Fase 1 (SC Trat 13,1675, SC Error 1,9300, F 27,29) y tomé la captura

### Prompt 5/6 — Script de R y verificación
- Ruta: B (agente externo: Claude)
- Fecha: generado 2026-11-03; aplicado 2026-11-04
- Qué generó la IA (archivos): `verificacion/verificacion_dca.R`
- Qué acepté sin cambios: ANOVA, Tukey, Shapiro-Wilk y Bartlett
- Qué corregí y por qué: el script original no tenía la variable `k` y daba los datos base (F = 24,72); lo reemplacé por uno con `k <- 0.4` para que use mi variante
- Cómo lo verifiqué: ejecuté `Rscript verificacion/verificacion_dca.R`, obtuve F = 27,29 y DMS = 0,8419, y pegué la salida como comentario en el .R

## Tabla de verificación con mi variante (k = 0,4)

| Cantidad | Mano (mi hoja) | App (Python) | R |
|---|---|---|---|
| Gran total Y.. | 212,2 | 212,2 | — |
| Factor de corrección | 2814,30 | — | — |
| SC Tratamientos | 13,16 | 13,1675 | 13,17 |
| SC Error | 1,93 | 1,9300 | 1,93 |
| SC Total | 15,09 | 15,0975 | — |
| CM Tratamientos | 4,38 | 4,3892 | 4,389 |
| CM Error | 0,16 | 0,1608 | 0,161 |
| F (3; 12) | 27,29 | 27,2902 | 27,29 |
| p-valor | < 0,0001 | 1,2e-05 | 1,21e-05 |
| DMS Tukey | 0,842 | 0,8419 | 0,8419 |
| CV | 3,02 % | 3,02 % | 3,0239 % |

Diferencias de redondeo: a mano trabajé con 2 decimales y q = 4,20; Python y R usan q = 4,1987, por eso la DMS pasa de 0,842 a 0,8419. Con 4,20 a mano la DMS exacta es 0,8422.

## Tabla de verificación con datos base (k = 0)

| Cantidad | Mano (fórmulas) | App (Python) | R |
|---|---|---|---|
| Gran total Y.. | 210,6 | 210,6 | — |
| Factor de corrección | 2772,0225 | — | — |
| SC Tratamientos | 11,9275 | 11,9275 | 11,93 |
| SC Error | 1,9300 | 1,9300 | 1,93 |
| SC Total | 13,8575 | 13,8575 | — |
| CM Tratamientos | 3,9758 | 3,9758 | 3,976 |
| CM Error | 0,1608 | 0,1608 | 0,161 |
| F (3; 12) | 24,72 | 24,72 | 24,72 |
| p-valor | 2,0e-05 | 2,0e-05 | 2,01e-05 |
| DMS Tukey (q = 4,1987) | 0,8419 | 0,8419 | 0,8419 |
| CV | 3,05 % | 3,05 % | 3,04684 % |

## Supuestos
Shapiro-Wilk (normalidad de residuos) da W = 0,939 y p = 0,337 tanto en Python como en R. Para homogeneidad de varianzas la app usa Levene y R usa Bartlett; son pruebas distintas, por eso sus p-valores no son iguales, pero ambas llevan a no rechazar la homogeneidad.

## Pregunta de reserva cognitiva
Al sumar la misma constante k a todas las observaciones de un tratamiento, la **SC Error no cambia**: cada dato se mueve igual que la media de su grupo, así que las desviaciones dentro del grupo son las mismas. Lo que cambia es la SC Tratamientos y, por tanto, F. Lo comprobé: con k = 0 la SC Error es 1,9300 y con k = 0,4 también es 1,93, mientras la SC Tratamientos pasó de 11,9275 a 13,1675 y F de 24,72 a 27,29.
