# Verificación del DCA en R (Actividad 1 - Diseño Experimental)
# k = (último dígito del código) / 10. Código terminado en 4 -> k = 0.4
k <- 0.4

datos <- data.frame(
  secador = rep(c("A", "B", "C", "D"), each = 4),
  humedad = c(12.4, 13.1, 12.8, 13.5,
              14.1, 14.8, 13.9, 14.6,
              11.8, 12.3, 11.5, 12.2,
              13.5, 13.0, 13.8, 13.3)
)
datos$humedad[datos$secador == "D"] <- datos$humedad[datos$secador == "D"] + k
datos$secador <- factor(datos$secador)

modelo <- aov(humedad ~ secador, data = datos)
print(summary(modelo))                       # tabla ANOVA: gl, SC, CM, F, p

cme <- deviance(modelo) / df.residual(modelo)   # CM del error
r   <- 4
q   <- qtukey(0.95, nmeans = 4, df = df.residual(modelo))
cat("CME =", cme, "\nDMS Tukey =", q * sqrt(cme / r), "\n")
cat("CV (%) =", sqrt(cme) / mean(datos$humedad) * 100, "\n")

print(TukeyHSD(modelo))                      # comparaciones por pares
print(shapiro.test(residuals(modelo)))       # normalidad de residuos
print(bartlett.test(humedad ~ secador, data = datos))  # homogeneidad

# ---- Pegue aquí, como comentario, la salida obtenida en su R ----
#             Df Sum Sq Mean Sq F value   Pr(>F)    
# secador      3  13.17   4.389   27.29 1.21e-05 ***
# Residuals   12   1.93   0.161                     
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# CME = 0.1608333 
# DMS Tukey = 0.841916 
# CV (%) = 3.023867 
#   Tukey multiple comparisons of means
#     95% family-wise confidence level
# 
# Fit: aov(formula = humedad ~ secador, data = datos)
# 
# $secador
#      diff          lwr       upr     p adj
# B-A  1.40  0.558083992  2.241916 0.0016858
# C-A -1.00 -1.841916008 -0.158084 0.0189007
# D-A  0.85  0.008083992  1.691916 0.0475968
# C-B -2.40 -3.241916008 -1.558084 0.0000109
# D-B -0.55 -1.391916008  0.291916 0.2632302
# D-C  1.85  1.008083992  2.691916 0.0001444
# 
# 
# 	Shapiro-Wilk normality test
# 
# data:  residuals(modelo)
# W = 0.93904, p-value = 0.3374
# 
# 
# 	Bartlett test of homogeneity of variances
# 
# data:  humedad by secador
# Bartlett's K-squared = 0.31866, df = 3, p-value = 0.9565
# 
#             Df Sum Sq Mean Sq F value   Pr(>F)    
# secador      3  13.17   4.389   27.29 1.21e-05 ***
# Residuals   12   1.93   0.161                     
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# CME = 0.1608333 
# DMS Tukey = 0.841916 
# CV (%) = 3.023867 
#   Tukey multiple comparisons of means
#     95% family-wise confidence level
# 
# Fit: aov(formula = humedad ~ secador, data = datos)
# 
# $secador
#      diff          lwr       upr     p adj
# B-A  1.40  0.558083992  2.241916 0.0016858
# C-A -1.00 -1.841916008 -0.158084 0.0189007
# D-A  0.85  0.008083992  1.691916 0.0475968
# C-B -2.40 -3.241916008 -1.558084 0.0000109
# D-B -0.55 -1.391916008  0.291916 0.2632302
# D-C  1.85  1.008083992  2.691916 0.0001444
# 
# 
# 	Shapiro-Wilk normality test
# 
# data:  residuals(modelo)
# W = 0.93904, p-value = 0.3374
# 
# 
# 	Bartlett test of homogeneity of variances
# 
# data:  humedad by secador
# Bartlett's K-squared = 0.31866, df = 3, p-value = 0.9565
# 
#             Df Sum Sq Mean Sq F value   Pr(>F)    
# secador      3  13.17   4.389   27.29 1.21e-05 ***
# Residuals   12   1.93   0.161                     
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# CME = 0.1608333 
# DMS Tukey = 0.841916 
# CV (%) = 3.023867 
#   Tukey multiple comparisons of means
#     95% family-wise confidence level
# 
# Fit: aov(formula = humedad ~ secador, data = datos)
# 
# $secador
#      diff          lwr       upr     p adj
# B-A  1.40  0.558083992  2.241916 0.0016858
# C-A -1.00 -1.841916008 -0.158084 0.0189007
# D-A  0.85  0.008083992  1.691916 0.0475968
# C-B -2.40 -3.241916008 -1.558084 0.0000109
# D-B -0.55 -1.391916008  0.291916 0.2632302
# D-C  1.85  1.008083992  2.691916 0.0001444
# 
# 
# 	Shapiro-Wilk normality test
# 
# data:  residuals(modelo)
# W = 0.93904, p-value = 0.3374
# 
# 
# 	Bartlett test of homogeneity of variances
# 
# data:  humedad by secador
# Bartlett's K-squared = 0.31866, df = 3, p-value = 0.9565
# 
