# Verificación del DCA en R: secadores solares de yuca
# Ejecutar desde la raíz del repositorio:  Rscript verificacion/verificacion_dca.R
# Después de ejecutarlo, PEGUE su salida real como comentario al final de este archivo.

datos <- read.csv("data/dca_secadores.csv")
datos$secador <- factor(datos$secador)

# 1) ANOVA de un factor: Y_ij = mu + tau_i + e_ij
modelo <- aov(humedad ~ secador, data = datos)
print(summary(modelo))

# 2) Cuadrado medio del error, gl del error y coeficiente de variación
cme  <- deviance(modelo) / df.residual(modelo)   # CME = SC Error / gl Error
gl_e <- df.residual(modelo)
cv   <- sqrt(cme) / mean(datos$humedad) * 100
cat("\nCME =", cme, " gl error =", gl_e, " CV (%) =", cv, "\n")

# 3) Tukey HSD y DMS = q(0.05; t; glE) * sqrt(CME / r)
print(TukeyHSD(modelo, conf.level = 0.95))
t <- nlevels(datos$secador)
r <- unique(table(datos$secador))
q <- qtukey(0.95, nmeans = t, df = gl_e)
dms <- q * sqrt(cme / r)
cat("\nq =", q, " DMS =", dms, "\n")

# 4) Supuestos
print(shapiro.test(residuals(modelo)))             # normalidad de residuos
print(bartlett.test(humedad ~ secador, data = datos))  # homogeneidad (Bartlett)

# ---- Valores esperados con los datos base (calculados con Python) ----
# SC Trat = 11.9275, SC Error = 1.9300, SC Total = 13.8575
# CM Trat = 3.9758, CME = 0.1608, F = 24.72 (gl 3 y 12), p = 2.0e-05
# CV = 3.05 %, DMS Tukey = 0.8419
# ---- SALIDA REAL DE R (pegar aquí tras ejecutar) ----
