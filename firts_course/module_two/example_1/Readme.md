## Cálculo de Velocidades y Aceleraciones usando Diferencias Hacia Adelante

### Descripción

Este programa en C++ calcula las **velocidades** y **aceleraciones** de un objeto a partir de datos experimentales de **tiempo** y **posición**. Utiliza el método numérico de **diferencias hacia adelante** para estimar la derivada primera (velocidad) y la derivada segunda (aceleración) de la posición respecto al tiempo.

Los resultados se guardan en un archivo de texto tabulado, que puede abrirse fácilmente con cualquier editor de texto o programa de hojas de cálculo como Excel o LibreOffice Calc.

### ¿Cómo funciona?

1. **Datos de entrada desde archivo:**
    - El programa lee los datos de un archivo de texto llamado `datos.txt`.
    - El archivo debe tener **dos columnas** separadas por espacios o tabulaciones, con un encabezado en la primera línea.
    - **Estructura obligatoria del archivo:**

```
Tiempo   Posicion
0.0      0
0.5      0.61
1.0      0.18
1.5      2.13
2.0      3.63
2.5      6.05
3.0      10.02
3.5      16.54
4.0      27.29
```

    - La primera columna corresponde a los valores de tiempo y la segunda a las posiciones.
2. **Cálculo de velocidades:**
Se utiliza el método de diferencias hacia adelante:

```
velocidad[i] = (posiciones[i+1] - posiciones[i]) / (tiempos[i+1] - tiempos[i])
```

3. **Cálculo de aceleraciones:**
Se aplica el mismo método sobre las velocidades:

```
aceleracion[i] = (velocidades[i+1] - velocidades[i]) / (tiempos[i+2] - tiempos[i])
```

4. **Salida de resultados:**
El programa genera un archivo llamado `salida.txt` con las siguientes columnas:
    - Tiempo
    - Posición
    - Velocidad
    - Aceleración

### Ejemplo de salida (`salida.txt`)

```
Tiempo  Posicion  Velocidad  Aceleracion
0.0     0         v0         a0
0.5     0.61      v1         a1
1.0     0.18      v2         a2
...     ...       ...        ...
4.0     27.29
```

Donde `v0`, `a0`, etc., son los valores calculados por el programa.

### Uso

1. **Prepara el archivo de datos** con el formato mostrado arriba y guárdalo como `datos.txt` en el mismo directorio que el ejecutable.
2. **Compilar el programa:**

```bash
g++ -o diferencias diferencias.cpp
```

3. **Ejecuta el programa:**

```bash
./diferencias
```

4. **Revisa el archivo de resultados:**
Abre `salida.txt` para ver la tabla de resultados.

### Personalización

- Puede usar cualquier archivo de entrada que siga el formato de dos columnas con encabezado.
- El programa valida automáticamente que los datos sean suficientes y consistentes.
- Si lo desea, puede modificar el nombre del archivo de entrada en el código fuente.


### Requisitos

- Compilador de C++ compatible (por ejemplo, g++).

---
