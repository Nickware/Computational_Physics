# Física de las cometas y su vuelo en Bogotá durante agosto

## Mapa rápido

| Archivo | Función | Salida principal |
| :-- | :-- | :-- |
| [`modelo_cometa_catenaria.py`](modelo_cometa_catenaria.py) | Resuelve el equilibrio directo de una cometa y la forma del hilo | `forma_hilo_cometa.png` |
| [`perfil_viento_cometa.py`](perfil_viento_cometa.py) | Simula mediciones, invierte el modelo y ajusta un perfil de viento | `perfil_viento_cometa.png` |
| [`README_perfil_viento.md`](README_perfil_viento.md) | Documenta el modelo inverso y su interpretación | Documentación |

El flujo recomendado es ejecutar primero el modelo directo y después el
modelo inverso. El segundo reutiliza las funciones del primero.

## Ejecución de los modelos

Los ejemplos ejecutables están en Python y requieren `numpy` y `matplotlib`:

```bash
cd waves
python3 -m pip install numpy matplotlib
python3 modelo_cometa_catenaria.py
python3 perfil_viento_cometa.py
```

Desde la raíz del repositorio también pueden ejecutarse así:

```bash
python3 waves/modelo_cometa_catenaria.py
python3 waves/perfil_viento_cometa.py
```

El primer script genera `forma_hilo_cometa.png`. El segundo genera
`perfil_viento_cometa.png` a partir de un experimento sintético. Ninguno de
los dos sustituye mediciones de campo ni un estudio formal de viabilidad
eólica.

## Convenciones y unidades

| Símbolo | Significado | Unidad |
| :-- | :-- | :-- |
| `rho` | Densidad del aire | kg/m³ |
| `V` | Velocidad del viento | m/s |
| `A` | Área proyectada de la cometa | m² |
| `CL`, `CD` | Coeficientes de sustentación y arrastre | adimensional |
| `mu` | Masa lineal del hilo | kg/m |
| `W_cometa` | Peso de la estructura de la cometa | N |
| `longitud_hilo` | Longitud desplegada del hilo | m |

El modelo incluye el peso del hilo mediante `mu * g * s`. Por eso
`W_cometa` representa únicamente el peso de la estructura de la cometa y no
debe incluir otra vez la masa del hilo.

## 1. ¿Por qué vuelan las cometas?

Una cometa vuela porque el viento, al chocar con su superficie inclinada, genera una fuerza aerodinámica que se descompone en dos componentes: la **sustentación** (perpendicular a la dirección del viento) y el **arrastre** (paralelo a esa dirección). En vuelo estable, esta fuerza aerodinámica se equilibra con el peso de la estructura, el peso distribuido del hilo y la tensión que ejerce la cuerda sostenida por el volador.

En agosto, los vientos alisios del sureste se intensifican sobre gran parte de Colombia —especialmente en el centro y norte del país— alcanzando velocidades típicas de 20–30 km/h. Esa intensidad es suficiente para generar sustentación apreciable en superficies ligeras como las cometas, sin ser tan turbulenta como para desestabilizarlas. De ahí que agosto se conozca tradicionalmente como el mes de las cometas.

## 2. Las fuerzas en juego

Sobre una cometa en vuelo estacionario actúan tres fuerzas:

- **Peso** ($W$): de la estructura de la cometa más la porción de hilo que está en el aire.
- **Tensión de la cuerda** ($T$): dirigida desde la cometa hacia el punto donde el volador la sostiene.
- **Resultante aerodinámica** ($R$): suma vectorial de sustentación ($L$) y arrastre ($D$).

Para que la cometa se mantenga en el aire, la sustentación debe superar al peso total (cometa + hilo), y el arrastre debe ser compensado por la componente horizontal de la tensión. Cuando las tres fuerzas se equilibran vectorialmente, la cometa queda en una posición aparentemente fija, aunque en la práctica oscila alrededor de ese punto de equilibrio.

### Ángulo de ataque y estabilidad

El **ángulo de ataque** —el ángulo entre el viento y el plano de la cometa— determina cuánta sustentación y arrastre se generan. Ángulos grandes aumentan la sustentación pero también el arrastre y el riesgo de entrar en pérdida. La posición del centro de presiones respecto al centro de gravedad determina si la cometa se estabiliza o tiende a voltearse; por eso se usan colas, quillas y diseños asimétricos que introducen momentos correctivos cuando una ráfaga la perturba.

El punto donde se ata la brida controla directamente el ángulo de ataque: al mover ese punto o al tensar/soltar el hilo, el volador cambia la orientación de la cometa respecto al viento y, con ello, el punto de equilibrio.

## 3. Modelo numérico simplificado (sin peso del hilo)

Como primera aproximación, se puede calcular sustentación y arrastre con la fórmula estándar de aerodinámica:

$$L = \frac{1}{2}\rho V^2 C_L A \qquad D = \frac{1}{2}\rho V^2 C_D A$$

donde $\rho$ es la densidad del aire, $V$ la velocidad del viento relativa a la cometa, $A$ el área proyectada, y $C_L$, $C_D$ los coeficientes de sustentación y arrastre (dependen de la forma y el ángulo de ataque).

**Ejemplo 1 — viento suave (8 km/h) en un parque de Bogotá**, con una cometa plana sencilla:

| Parámetro | Valor |
|---|---|
| Área efectiva $A$ | 0,8 m² |
| Masa cometa + hilo | 0,25 kg → $W\approx 2{,}45$ N |
| Densidad del aire (Bogotá, ~2600 m) $\rho$ | 0,89 kg/m³ |
| Viento $V$ | 2,2 m/s |
| $C_L$, $C_D$ | 0,8 / 0,3 |

Resultado: $L\approx 1{,}4$ N, $D\approx 0{,}53$ N. Como $L < W$, con este viento tan suave la cometa apenas se sostendría o tendería a caer — necesita más viento o mejor ángulo de ataque.

**Ejemplo 2 — viento fuerte de agosto (20 km/h ≈ 5,6 m/s) en Ciudad Bolívar**, con una cometa Delta de 1 m de envergadura:

| Parámetro | Valor |
|---|---|
| Área proyectada $A$ | 0,7 m² |
| Masa cometa + hilo | 0,25 kg → $W\approx 2{,}45$ N |
| $C_L$, $C_D$ (Delta bien ajustada) | 1,0 / 0,2 |

Resultado: $L\approx 9{,}8$ N, $D\approx 1{,}95$ N. Aquí $L$ es varias veces $W$, lo que permite que la cuerda tome un ángulo alto respecto al suelo (típicamente 50°–70°) y que la cometa alcance buena altura.

Esta primera aproximación trata el hilo como una **línea recta sin peso propio significativo** (solo se incluye su masa en el peso total, pero no su efecto en la forma de la cuerda). Es razonable como orden de magnitud, pero no captura la curvatura real del hilo cuando hay muchos metros desplegados.

## 4. Modelo completo: equilibrio de la cometa + catenaria del hilo

Un modelo más riguroso separa dos partes que se resuelven en cadena:

**(a) Equilibrio de la cometa**, tratada como un punto en el extremo superior del hilo. Sobre ella actúan el peso propio $W_{cometa}$, la sustentación $L$ (vertical) y el arrastre $D$ (horizontal, en la dirección del viento), y la tensión que ejerce el hilo justo en el punto de amarre, con componentes horizontal $H$ y vertical $V_{top}$. El equilibrio de fuerzas da directamente:

$$H = D \qquad V_{top} = L - W_{cometa}$$

Es decir, la componente horizontal de la tensión en el punto más alto del hilo iguala al arrastre, y la componente vertical iguala a la sustentación neta (descontado el peso de la cometa).

**(b) Forma del hilo como catenaria.** El hilo tiene una masa por unidad de longitud $\mu$ (kg/m). Como no hay fuerzas horizontales distribuidas a lo largo del hilo (se desprecia el arrastre del aire sobre el hilo mismo, solo su peso), la componente horizontal de la tensión $H$ es **constante en toda la longitud del hilo**. La componente vertical, en cambio, crece desde el punto donde lo sostiene el volador hasta el punto de amarre en la cometa, porque en cada punto el hilo debe soportar el peso de todo el tramo que tiene debajo:

$$V(s) = V_0 + \mu g\, s$$

donde $s$ es la longitud de hilo medida desde el suelo y $V_0$ es la componente vertical de la tensión que siente el volador en su mano. Como en el extremo superior ($s=\ell$, con $\ell$ la longitud total desplegada) ya sabemos que $V(\ell)=V_{top}=L-W_{cometa}$, se despeja directamente:

$$V_0 = L - W_{cometa} - \mu g \ell$$

Con $H$ y $V_0$ conocidos, la forma completa del hilo (altura y distancia horizontal en función de $s$) tiene solución cerrada, la misma que la de una cadena colgante clásica:

$$x(s) = \frac{H}{\mu g}\left[\operatorname{asinh}\frac{V(s)}{H} - \operatorname{asinh}\frac{V_0}{H}\right] \qquad y(s) = \frac{1}{\mu g}\left[T(s) - T_0\right]$$

con $T(s)=\sqrt{H^2+V(s)^2}$. Evaluando en $s=\ell$ se obtiene la altura real de la cometa, la distancia horizontal al volador, el ángulo de la cuerda en la mano ($\theta_0=\arctan(V_0/H)$) y el ángulo en el punto de amarre ($\theta_{top}=\arctan(V_{top}/H)$).

Este modelo es más completo que el anterior porque ya no asume que el hilo es una línea recta: predice explícitamente su curvatura (sag), y muestra que, para hilos delgados de cometa (masa por metro muy baja frente a la tensión que soportan), la curvatura suele ser pequeña — el hilo se comporta casi como una línea recta, salvo con vientos muy débiles o hilos muy largos y pesados.

### Simplificaciones que quedan fuera de este modelo

- Se desprecia el arrastre aerodinámico *sobre el propio hilo* (solo se considera su peso). Con hilos largos y viento fuerte, esta fuerza no siempre es despreciable.
- $C_L$ y $C_D$ se toman constantes, cuando en realidad dependen del ángulo de ataque real de la cometa.
- El viento se asume uniforme con la altura, sin gradiente ni ráfagas.
- El hilo se trata como perfectamente flexible e inextensible.

## Estado del proyecto

- **Implementado:** equilibrio estático, catenaria con masa lineal, comparación con hilo recto, simulación sintética de vuelos y ajuste de ley de potencia.
- **Supuesto:** viento estacionario durante cada vuelo, coeficientes aerodinámicos constantes y mediciones de tensión y ángulo sin sesgo sistemático.
- **No implementado:** arrastre distribuido sobre el hilo, elasticidad, dinámica de la cometa, ráfagas, calibración experimental e intervalos de confianza.
- **Uso recomendado:** aprendizaje, exploración de sensibilidad y diseño de un experimento preliminar; no dimensionamiento de un parque eólico.

## Referencias

- Aspectos físicos elementales del vuelo de las cometas estáticas planas — Kimerius: https://www.kimerius.com/app/download/5783713555/Aspectos+f%C3%ADsicos+elementales+del+vuelo+de+las+cometas+est%C3%A1ticas+planas.pdf
- Equilibrio estático de cometas planas (LAJPE): http://www.lajpe.org/sep12/18_LAJPE_677_Juan_Suay_preprint_corr_f.pdf
- Introducción a la aerodinámica — Universidad de Cádiz (Studocu): https://www.studocu.com/es/document/universidad-de-cadiz/aerodinamica-y-aeroelasticidad/introducion-a-la-aerodinamica/6102773
- Vientos alisios y clima de Bogotá — OGA Universidad Nacional: https://ogabogota.unal.edu.co/vientos/
- Densidad del aire en función de la altitud — Wikipedia: https://es.wikipedia.org/wiki/Densidad_del_aire
- Sustentación — Wikipedia: https://es.wikipedia.org/wiki/Sustentaci%C3%B3n
- Recomendaciones para elevar cometa en Bogotá — Alcaldía de Bogotá: https://bogota.gov.co/mi-ciudad/cultura-recreacion-y-deporte/recomendaciones-para-elevar-cometa-en-bogota
- Vientos de agosto en Colombia, fenómeno natural y cultural — Radio Nacional: https://www.radionacional.co/cultura/tradiciones/vientos-de-agosto-en-colombia-un-fenomeno-natural-y-cultural
