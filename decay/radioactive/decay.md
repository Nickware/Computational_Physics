# Simulación de Desintegración Radioactiva (True BASIC)

## Descripción del programa

Este programa simula el **decaimiento radioactivo** de una muestra de núcleos inestables (uranio) utilizando un método de integración numérica de primer orden (Euler). Resuelve la ecuación diferencial:

$$\frac{dN}{dt} = -\frac{N}{\tau}$$

donde:
- **N**: número de núcleos en el instante t
- **τ (tau)**: constante de tiempo de desintegración (vida media)

La solución discretizada implementada es:

$$N(t + \Delta t) = N(t) \cdot \left(1 - \frac{\Delta t}{\tau}\right)$$

### Estructura modular

El programa está organizado en **tres bloques funcionales** que separan responsabilidades:

| Subrutina | Función |
|---|---|
| `initializate` | Solicitar al usuario los parámetros iniciales (N₀, τ, Δt) |
| `calculate` | Calcular la evolución temporal del sistema |
| `display` | Graficar los resultados y muestra información relevante |

### Archivos del proyecto

```
decay/
├── decay.bas          # Programa principal
├── decay_subs.bas     # Subrutinas (initializate, calculate, display)
├── sgfun.bas          # Librería gráfica (proporcionada por el entorno)
└── sglib.bas          # Librería gráfica auxiliar
```

---

## Cómo ejecutarlo

### Requisitos
- Entorno **True BASIC** instalado (versión clásica o Chromebook)
- Las librerías gráficas `sgfun*` y `sglib*` disponibles en el directorio

### Pasos de ejecución

1. **Coloca todos los archivos** (`decay.bas`, `decay_subs.bas`, `sgfun.bas`, `sglib.bas`) en el mismo directorio.

2. **Abre el entorno True BASIC** y carga el programa principal:
   ```
   OLD "decay.bas"
   ```

3. **Ejecuta el programa**:
   ```
   RUN
   ```

4. **Responde a los prompts** del usuario:
   ```
   Ingrese el número de núcleos iniciales -> 1000
   Ingrese la constante de tiempo (tau) -> 10
   Ingrese el paso de tiempo (dt) -> 0.1
   ```

5. **Observa la gráfica** de desintegración exponencial y la constante de tiempo mostrada en pantalla.

### Para salir
Presionar `Ctrl+C` o cierra la ventana gráfica.

---

## Guía de migración a otros lenguajes

### Consideraciones generales

Al migrar este código, ten en cuenta:

| Aspecto | True BASIC | Lenguajes modernos |
|---|---|---|
| Arrays | `DIM arr(100)` | `std::vector`, `numpy.array`, matrices nativas |
| Subrutinas | `SUB ... END SUB` | Funciones/métodos |
| Gráficas | `CALL datagraph(...)` | Librerías dedicadas (matplotlib, gnuplot, Qt) |
| Entrada | `INPUT PROMPT` | `input()`, `std::cin`, `scanf` |
| Indexación | Empieza en 1 | Python/C++ empiezan en 0 |

---

### Migración a Python

**Librerías recomendadas**: `numpy`, `matplotlib`

```python
import numpy as np
import matplotlib.pyplot as plt

def initializate():
    N0 = float(input("Ingrese el número de núcleos iniciales -> "))
    tau = float(input("Ingrese la constante de tiempo (tau) -> "))
    dt = float(input("Ingrese el paso de tiempo (dt) -> "))
    return N0, tau, dt

def calculate(N0, tau, dt, n_steps):
    n_uranium = np.zeros(n_steps)
    t = np.zeros(n_steps)
    n_uranium[0] = N0
    for i in range(n_steps - 1):
        n_uranium[i+1] = n_uranium[i] * (1 - dt/tau)
        t[i+1] = t[i] + dt
    return n_uranium, t

def display(n_uranium, t, tau, dt):
    plt.plot(t, n_uranium, 'k-')
    plt.title("Desintegración Radioactiva")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Número de núcleos")
    plt.grid(True)
    plt.text(t[-1]*0.5, n_uranium[0]*0.5, f"τ = {tau}")
    plt.show()

if __name__ == "__main__":
    N0, tau, dt = initializate()
    n_steps = 1000
    n_uranium, t = calculate(N0, tau, dt, n_steps)
    display(n_uranium, t, tau, dt)
```

**Ventajas**: sintaxis limpia, gráficas profesionales, ideal para análisis posterior.

---

### Migración a Octave / MATLAB

**Muy similar al BASIC original** gracias a la sintaxis matricial nativa.

```octave
function decay()
    [N0, tau, dt] = initializate();
    [n_uranium, t] = calculate(N0, tau, dt);
    display_results(n_uranium, t, tau);
end

function [N0, tau, dt] = initializate()
    N0 = input("Ingrese el número de núcleos iniciales -> ");
    tau = input("Ingrese la constante de tiempo (tau) -> ");
    dt = input("Ingrese el paso de tiempo (dt) -> ");
end

function [n, t] = calculate(N0, tau, dt)
    n_steps = 1000;
    n = zeros(1, n_steps);
    t = zeros(1, n_steps);
    n(1) = N0;
    for i = 1:(n_steps-1)
        n(i+1) = n(i) * (1 - dt/tau);
        t(i+1) = t(i) + dt;
    end
end

function display_results(n, t, tau)
    plot(t, n, 'k', 'LineWidth', 2);
    title("Desintegración Radioactiva");
    xlabel("Tiempo (s)");
    ylabel("Número de núcleos");
    text(t(end)/2, n(1)/2, sprintf("\\tau = %.2f", tau));
    grid on;
end
```

**Ventajas**: transición casi directa desde BASIC, ideal para ingeniería.

---

### Migración a C++

**Librerías recomendadas**: `<vector>`, `<iostream>`, `matplotlib-cpp` o `gnuplot-iostream` para gráficas.

```cpp
#include <iostream>
#include <vector>
#include <cmath>

void initializate(double &N0, double &tau, double &dt) {
    std::cout << "Ingrese el número de núcleos iniciales -> ";
    std::cin >> N0;
    std::cout << "Ingrese la constante de tiempo (tau) -> ";
    std::cin >> tau;
    std::cout << "Ingrese el paso de tiempo (dt) -> ";
    std::cin >> dt;
}

void calculate(double N0, double tau, double dt, 
               std::vector<double> &n_uranium, std::vector<double> &t) {
    int n_steps = t.size();
    n_uranium[0] = N0;
    for (int i = 0; i < n_steps - 1; ++i) {
        n_uranium[i+1] = n_uranium[i] * (1.0 - dt/tau);
        t[i+1] = t[i] + dt;
    }
}

void display(const std::vector<double> &n, const std::vector<double> &t, double tau) {
    // Aquí se integraría matplotlib-cpp o gnuplot-iostream
    std::cout << "Graficando " << n.size() << " puntos...\n";
    std::cout << "Constante de tiempo: " << tau << "\n";
}

int main() {
    double N0, tau, dt;
    initializate(N0, tau, dt);
    
    int n_steps = 1000;
    std::vector<double> n_uranium(n_steps), t(n_steps);
    calculate(N0, tau, dt, n_uranium, t);
    display(n_uranium, t, tau);
    
    return 0;
}
```

**Compilación**:
```bash
g++ -std=c++17 decay.cpp -o decay
./decay
```

**Ventajas**: máximo rendimiento, ideal para simulaciones a gran escala.

---

## Notas finales

- **Verificación física**: la solución analítica es $N(t) = N_0 \cdot e^{-t/\tau}$. Compara siempre tu resultado numérico con esta curva para validar el método de Euler.
- **Estabilidad numérica**: si $\Delta t > \tau$, el método de Euler se vuelve inestable. Usa pasos pequeños ($\Delta t \ll \tau$).
- **Métodos mejores**: para mayor precisión, considera implementar **Runge-Kutta de 4º orden** en la migración.