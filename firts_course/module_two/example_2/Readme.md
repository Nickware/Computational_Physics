# Simulación que procesa datos experimentales de una partícula en movimiento rectilíneo

Esta simulación en C++ procesa datos experimentales de una partícula en movimiento rectilíneo, específicamente para leer tiempos y posiciones desde un archivo de texto, calcular velocidades y aceleraciones, guardar los resultados en un nuevo archivo y generar gráficos automáticamente usando Gnuplot.

## Pasos principales

### 1. Lectura de datos

- Abrir el archivo `datos.txt` y lee pares de valores: **tiempo** y **posición**.
- Los valores se almacenan en dos vectores: `tiempos` y `posiciones`.


### 2. Cálculo de velocidades

- Calcular la **velocidad promedio** entre puntos consecutivos usando la fórmula:

$$
v = \frac{\text{posicion}_{i+1} - \text{posicion}_i}{\text{tiempo}_{i+1} - \text{tiempo}_i}
$$
- Agregar los resultados al vector `velocidades`.


### 3. Cálculo de aceleraciones

- Calcular la **aceleración promedio** entre velocidades consecutivas:

$$
a = \frac{\text{velocidad}_{i+1} - \text{velocidad}_i}{\text{tiempo}_{i+2} - \text{tiempo}_i}
$$
- Los valores se añaden al vector `aceleraciones`.


### 4. Guardado de resultados

- Crear `salida.txt`, con una tabla que incluye:
    - **Tiempo**
    - **Posición**
    - **Velocidad** (si está disponible)
    - **Aceleración** (si está disponible)
- El formato es tabular, adecuado para análisis posterior.


### 5. Generación de instrucciones para gráficas

- Crear el archivo `grafica.gp` con comandos de Gnuplot para graficar:
    - Posición vs. Tiempo
    - Velocidad vs. Tiempo
    - Aceleración vs. Tiempo
- Configurar títulos, ejes, formato PNG y nombres de archivo para cada gráfica.


### 6. Ejecución de Gnuplot

- Invocar Gnuplot mediante un comando del sistema para crear las imágenes de las gráficas.


## Resumen de salidas producidas

| Archivo | Contenido |
| :-- | :-- |
| `salida.txt` | Tabla con tiempo, posición, velocidad y aceleración |
| `grafica.gp` | Script de Gnuplot para generar las gráficas |
| `posicion.png` | Gráfica de posición vs. tiempo |
| `velocidad.png` | Gráfica de velocidad vs. tiempo |
| `aceleracion.png` | Gráfica de aceleración vs. tiempo |

## Usos típicos

- Útil en **física experimental** o laboratorios de una partícula en movimiento rectilíneo.
- Facilita un procesamiento y análisis automatizado de resultados.
- Permite visualización rápida y reducción de errores manuales.


## Oportunidades de mejora

- El cálculo de aceleración supone intervalos de tiempo uniformes o suficientemente pequeños.
- El programa no maneja excepciones para datos corruptos o incompletos.
- Es necesario tener **Gnuplot instalado** en el sistema para la generación de gráficas.

Este flujo automatiza la conversión de mediciones de posición en un análisis cinemático completo y visual, ahorrando tiempo y mejorando la rigurosidad del procesamiento de datos.
