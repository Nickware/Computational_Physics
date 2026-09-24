# Física Computacional

*Basado en la metodología de Nicholas J. Giordano*

## Mapa del repositorio

Este repositorio reúne ejercicios y proyectos de Física Computacional. La ruta recomendada va desde la programación básica, pasa por los métodos numéricos y la mecánica clásica, y termina en modelos aplicados de decaimiento y viento.

### Ruta de aprendizaje

1. **Primeros programas:** comienza en [`firts_course/module_one`](firts_course/module_one), con un programa introductorio en C++.
2. **Métodos numéricos:** continúa con [`module_two/example_1`](firts_course/module_two/example_1) para calcular velocidades y aceleraciones mediante diferencias finitas, y con [`module_two/example_2`](firts_course/module_two/example_2) para procesar datos y generar gráficas con Gnuplot.
3. **Mecánica y sistemas dinámicos:** estudia los modelos de bicicleta con y sin resistencia del aire en [`module_three/noairvsair`](firts_course/module_three/noairvsair) y el oscilador de Duffing en [`module_three/nonlinear`](firts_course/module_three/nonlinear).
4. **Modelos de decaimiento:** revisa [`decay`](decay/Readme.md), que reúne una misma estructura exponencial aplicada a fenómenos físicos, ambientales y económicos.
5. **Aerodinámica y viento:** termina con [`waves`](waves/Readme.md), donde se modelan las fuerzas sobre una cometa, la catenaria del hilo y la reconstrucción de un perfil vertical de viento.

### Índice de proyectos

#### Curso introductorio

| Proyecto | Qué contiene | Tecnologías |
| :-- | :-- | :-- |
| [`module_one`](firts_course/module_one) | Programa inicial y estructura básica de compilación | C++, Make |
| [`example_1`](firts_course/module_two/example_1) | Derivadas numéricas de posición para obtener velocidad y aceleración | Python, C++ |
| [`example_2`](firts_course/module_two/example_2) | Procesamiento de datos experimentales y generación de gráficas | C++, Gnuplot |
| [`noairvsair`](firts_course/module_three/noairvsair) | Comparación del movimiento de una bicicleta con y sin resistencia del aire | C++ |
| [`nonlinear`](firts_course/module_three/nonlinear) | Simulación del oscilador no lineal de Duffing | C++ |

#### Aplicaciones del decaimiento exponencial

El [README de `decay`](decay/Readme.md) es el punto de entrada de esta familia de proyectos. Todos parten de la idea de que una magnitud cambia proporcionalmente a su estado actual, pero cada carpeta cambia la interpretación física o aplicada de esa magnitud.

| Proyecto | Problema estudiado | Punto de entrada |
| :-- | :-- | :-- |
| `radioactive` | Desintegración nuclear y vida media | [`Readme.md`](decay/radioactive/Readme.md) |
| `credit_risk` | Supervivencia de un crédito y riesgo de default | [`Readme.md`](decay/credit_risk/Readme.md) |
| `loss_value` | Pérdida de valor de una inversión en Argentina | [`Readme.md`](decay/loss_value/Readme.md) |
| `water resources` | Disponibilidad hídrica en el páramo de Santurbán | [`Readme.md`](decay/water%20resources/Readme.md) |
| `mining` | Impacto de la actividad minera sobre recursos hídricos | [`Readme.md`](decay/mining/Readme.md) |
| `plastic_decomposition` | Persistencia y descomposición de plásticos en Bogotá | [`Readme.md`](decay/plastic_decomposition/Readme.md) |

#### Viento y cometas

| Proyecto | Qué contiene |
| :-- | :-- |
| [`modelo_cometa_catenaria.py`](waves/modelo_cometa_catenaria.py) | Equilibrio aerodinámico de la cometa y forma de la cuerda como catenaria |
| [`perfil_viento_cometa.py`](waves/perfil_viento_cometa.py) | Estimación de velocidad del viento y ajuste de un perfil vertical |
| [`README_perfil_viento.md`](waves/README_perfil_viento.md) | Explicación de la extensión de la cometa como anemómetro |

### Cómo leer la relación entre los proyectos

Los proyectos no forman una única aplicación ni dependen unos de otros mediante imports. La relación es progresiva y conceptual:

- `module_one` introduce la programación.
- `module_two` convierte datos en magnitudes físicas mediante derivación numérica.
- `module_three` aplica esas herramientas a sistemas mecánicos y no lineales.
- `decay` muestra cómo una misma ecuación puede transferirse entre dominios.
- `waves` integra equilibrio de fuerzas, geometría, simulación iterativa y ajuste de datos.

El repositorio mezcla C++, Python, True BASIC y Gnuplot porque conserva ejercicios con distintos objetivos didácticos. Los README de cada carpeta explican los requisitos y la ejecución particular de cada proyecto.

## Descripción del curso

Este curso introduce **técnicas computacionales y métodos numéricos** para resolver diversos problemas de física que van más allá de los enfoques analíticos. El programa utiliza el marco pedagógico de Nicholas J. Giordano y se enfoca en cómo la computación puede ampliar y profundizar la comprensión de los fenómenos físicos mediante la simulación y el análisis[^1].

## Objetivos de aprendizaje

Al finalizar el curso, los estudiantes podrán:

- Comprender el papel de la computación en la física moderna.
- Traducir problemas físicos a algoritmos.
- Aplicar métodos numéricos estándar, como búsqueda de raíces, integración, diferenciación, ecuaciones diferenciales y métodos de Monte Carlo, para resolver sistemas físicos.
- Visualizar e interpretar resultados computacionales.
- Desarrollar competencias en programación científica y pensamiento computacional[^3].


## Contenidos del curso

| Módulo | Temas y habilidades |
| :-- | :-- |
| **Introducción y programación** | Fundamentos del pensamiento computacional aplicado a la física. Introducción a lenguajes de programación, principalmente Python o MATLAB. Algoritmos y visualización de datos. |
| **Métodos numéricos** | Búsqueda de raíces (bisección y Newton-Raphson), interpolación (polinomios y Lagrange), mínimos cuadrados y ajuste de datos, integración numérica (reglas trapezoidal y de Simpson), y ecuaciones diferenciales ordinarias (Euler y Runge-Kutta). |
| **Mecánica clásica** | Aplicaciones al movimiento de proyectiles, sistemas oscilatorios, movimiento planetario, caos y sistemas dinámicos. Simulación de sistemas newtonianos y no lineales[^4][^5]. |
| **Procesos aleatorios** | Simulaciones de Monte Carlo, caminatas aleatorias, difusión, decaimiento nuclear y fundamentos de mecánica estadística. |
| **Electromagnetismo y física cuántica** | Simulación de electrostática, campos y sistemas cuánticos básicos, incluidas las ecuaciones de Schrödinger dependientes e independientes del tiempo. |
| **Temas avanzados** | Transformadas de Fourier, ecuaciones diferenciales parciales y sistemas complejos, como el modelo de Ising, autómatas celulares y transiciones de fase[^1]. |

## Metodología de enseñanza

- Clases interactivas sobre conceptos físicos y numéricos.
- Laboratorios prácticos de programación y ejercicios de código.
- Proyectos guiados que reproducen simulaciones del libro y exploran nuevos escenarios.
- Visualización de resultados para desarrollar intuición sobre las soluciones numéricas[^3].


## Evaluación

- Series de problemas y ejercicios de programación.
- Examen parcial sobre teoría e implementación.
- Proyecto de formulación, programación y documentación de una solución computacional para un problema físico relevante.


## Texto recomendado

- *Computational Physics* (2.ª edición), Nicholas J. Giordano y Hisao Nakanishi[^1]


## Aplicaciones típicas

- Simulación de sistemas clásicos y cuánticos que no pueden resolverse analíticamente.
- Visualización del comportamiento de sistemas complejos.
- Física estadística y estocástica.
- Investigaciones basadas en proyectos sobre temas de investigación actuales.


## Prerrequisitos

- Física introductoria.
- Cálculo diferencial e integral, de una y varias variables.
- Programación básica. No es obligatoria, pero resulta útil; el curso puede incluir una introducción rápida a los fundamentos de programación[^3].

Este curso utiliza la computación para hacer tangibles los conceptos físicos y preparar a los estudiantes para estudios avanzados, investigación y carreras profesionales en física y disciplinas relacionadas[^1][^3].

[^1]: https://www.mathworks.com/academia/books/computational-physics-giordano.html

[^3]: https://class-descriptions.northwestern.edu/4930/WCAS/PHYSICS/28874

[^4]: https://nust.edu.pk/wp-content/uploads/course_content_files/340753870_PHY-930%20%20%20Computational%20Physics%20.pdf

[^5]: https://www.ndsu.edu/fileadmin/physics.ndsu.edu/PDF_FILES/Detailed_Course_Descriptions/Phys370.pdf

[^6]: https://www.google.com.co/search?tbo=p\&tbm=bks\&q=inauthor%3A"Nicholas+J.+Giordano"

[^7]: https://units.imamu.edu.sa/colleges/en/science/Admission/PublishingImages/Lists/LinksDescription/AllItems/PHY 436-Computational Physics.pdf

[^8]: https://www.physics.purdue.edu/~hisao/book/

[^9]: https://sindromedown.net/virtual-library/b63N1V/9966507/Computational Physics Nicholas Giordano.pdf

[^10]: https://nust.edu.pk/wp-content/uploads/course_content_files/223713307_PHY-381%20Computational%20Physics.pdf

[^11]: https://www.physics.mun.ca/courses/p3800/LECTURES/L01/PHYS3800W2023outline.pdf

[^12]: https://facultyweb.kennesaw.edu/apapaefs/PHYS_3500K_Spring_2024_SYLLABUS.pdf

