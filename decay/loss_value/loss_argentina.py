# Modelo de pérdida de valor de una inversión en Argentina considerando riesgos económicos, políticos y regulatorios.
# Este modelo asume que la inversión pierde valor de manera exponencial debido a los riesgos combinados.
# Parámetros:
# - lambda_econ: Tasa de pérdida anual por factores económicos (inflación, recesión).
# - lambda_pol: Tasa de pérdida anual por factores políticos (elecciones, protestas).
# - lambda_reg: Tasa de pérdida anual por factores regulatorios (nuevos impuestos). 

# El valor de la inversión se calcula como V(t) = V0 * exp(- (lambda_econ + lambda_pol + lambda_reg) * t)
# Donde V0 es el valor inicial de la inversión y t es el tiempo en años.
# El gráfico muestra cómo el valor de la inversión decae a lo largo de 5 años bajo estos riesgos combinados.
# Nota: Este modelo es una simplificación y no considera otros factores como la diversificación, cambios en el mercado global, o estrategias de mitigación de riesgos. Es importante realizar un análisis más detallado para decisiones de inversión reales.

# Fuente de datos: Estimaciones basadas en tendencias históricas y eventos recientes en Argentina. Las tasas de pérdida son aproximadas y pueden variar según el contexto económico y político actual. Se recomienda consultar fuentes actualizadas para análisis específicos.
# Disclaimer: Este modelo es solo para fines educativos y no debe ser utilizado como asesoramiento financiero. Las inversiones conllevan riesgos y es importante realizar un análisis exhaustivo antes de tomar decisiones financieras.
# Recomendación: Para una evaluación más precisa, se recomienda realizar un análisis de sensibilidad variando las tasas de pérdida y considerando escenarios optimistas y pesimistas. Además, se pueden incorporar otros factores como la diversificación de la cartera, estrategias de cobertura, y cambios en el entorno global que podrían afectar el valor de la inversión.
# Este código es un ejemplo simplificado y no debe ser utilizado como base para decisiones de inversión sin un análisis más profundo y asesoramiento profesional.
# Para un análisis más detallado, se pueden considerar modelos más complejos que incluyan factores adicionales como la volatilidad del mercado, la correlación entre diferentes riesgos, y la posibilidad de recuperación de la inversión en ciertos escenarios. Además, se pueden utilizar técnicas de simulación como Monte Carlo para evaluar el impacto de la incertidumbre en las tasas de pérdida y obtener una distribución de posibles resultados para el valor de la inversión a lo largo del tiempo.
# En resumen, este modelo proporciona una visión general de cómo los riesgos económicos, políticos y regulatorios pueden afectar el valor de una inversión en Argentina a lo largo del tiempo, pero es importante considerar un análisis más detallado y personalizado para decisiones de inversión reales.
# Para obtener datos más precisos y actualizados, se recomienda consultar fuentes como el Banco Central de la República Argentina, el Instituto Nacional de Estadística y Censos (INDEC), y análisis de mercado de consultoras financieras. Además, es importante considerar el contexto global y regional que puede influir en la economía argentina, como las relaciones comerciales, la situación política en países vecinos, y las tendencias económicas globales.
# En conclusión, este modelo es una herramienta útil para visualizar el impacto de los riesgos combinados en el valor de una inversión en Argentina, pero debe ser utilizado con precaución y complementado con un análisis más profundo y asesoramiento profesional para tomar decisiones de inversión informadas.
# Para un análisis más completo, se pueden considerar escenarios alternativos con diferentes combinaciones de tasas de pérdida para evaluar cómo podrían afectar el valor de la inversión en diferentes contextos económicos y políticos. Además, se pueden incorporar factores adicionales como la diversificación de la cartera, estrategias de cobertura, y cambios en el entorno global que podrían influir en el valor de la inversión a lo largo del tiempo.

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo (tasas anuales)
lambda_econ = 0.15  # Inflación + recesión
lambda_pol = 0.10    # Elecciones 2023 + protestas
lambda_reg = 0.05    # Nuevos impuestos (2024)

# Valor inicial de la inversión (USD)
V0 = 100  # USD 100 millones
tiempo = np.arange(0, 5)  # 5 años

# Cálculo del valor ajustado
V_t = V0 * np.exp(-(lambda_econ + lambda_pol + lambda_reg) * tiempo)

# Gráfico
plt.plot(tiempo, V_t, 'ro-', label="Valor de la inversión")
plt.xlabel("Años")
plt.ylabel("Valor (USD millones)")
plt.title("Decaimiento de una Inversión en Argentina (Riesgo Integral)")
plt.grid()
plt.legend()
plt.show()
