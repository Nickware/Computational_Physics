# Decaimiento Radiactivo

El decaimiento radiactivo (o desintegración nuclear) es un proceso físico mediante el cual un núcleo atómico inestable pierde energía emitiendo radiación, transformándose en un núcleo más estable o incluso en un elemento diferente. Este fenómeno fue descubierto por **Henri Becquerel** en 1896, con importantes aportes de **Marie y Pierre Curie**, y **Ernest Rutherford**.

## Tipos de Decaimiento Radiactivo

- **Decaimiento Alfa (α)**
  - El núcleo emite una partícula alfa (2 protones + 2 neutrones, equivalente a un núcleo de helio-4).
  - Ejemplo (típico en núcleos pesados como uranio o plutonio):
    $$
    ^{238}_{92}\text{U} \to \text{núcleo~hijo} + \alpha
    $$

- **Decaimiento Beta (β)**
  - Un neutrón se convierte en un protón (o viceversa), emitiendo un electrón (β⁻) o un positrón (β⁺), junto con un antineutrino o neutrino.
  - **Beta negativo (β⁻):**
    $$
    n \to p^+ + e^- + \overline{\nu}_e \quad \text{(ej.: } ^{14}_6\text{C} \to \text{núcleo hijo})
    $$
  - **Beta positivo (β⁺):**
    $$
    p^+ \to n + e^+ + \nu_e \quad \text{(ej.: } ^{22}_{11}\text{Na} \to \text{núcleo hijo})
    $$
  - **Captura electrónica:** un protón captura un electrón y se convierte en un neutrón.

- **Decaimiento Gamma (γ)**
  - Un núcleo excitado libera fotones gamma de alta energía, sin alterar su número de protones o neutrones.
  - Ejemplo:
    $$
    ^{60}_{27}\text{Co}^* \to ^{60}_{27}\text{Co} + \gamma
    $$
  - Suele ocurrir tras una desintegración α o β que deja al núcleo en estado excitado.

- **Otros tipos:**
  - **Emisión de neutrones:** núcleos muy inestables liberan neutrones libres.
  - **Fisión espontánea:** núcleos pesados (como el californio-252) se dividen en dos núcleos más ligeros.

## Ley del Decaimiento Radiactivo

La tasa de desintegración sigue una **ley exponencial**:
$$
N(t) = N_0 e^{-\lambda t}
$$
- $$N(t)$$: Número de núcleos no desintegrados en el tiempo $$t$$.
- $$N_0$$: Número inicial de núcleos.
- $$\lambda$$: Constante de decaimiento (propia de cada isótopo).

La **vida media** ($$t_{1/2}$$) es el tiempo en que la mitad de los núcleos se desintegran:
$$
t_{1/2} = \frac{\ln(2)}{\lambda}
$$

## Aplicaciones

- **Medicina:** Radioterapia (ej.: cobalto-60), diagnóstico por imágenes (tecnecio-99m).
- **Energía:** Reactores nucleares (uranio-235, plutonio-239).
- **Geología/Cronología:** Datación por carbono-14 ($$t_{1/2} = 5730$$ años), datación uranio-plomo.
- **Industria:** Esterilización de alimentos, medidores de espesor.

## Riesgos

La radiación ionizante (α, β, γ) puede dañar tejidos y ADN, provocando mutaciones o enfermedades como el cáncer. Su manipulación requiere blindajes adecuados (plomo para γ, plástico para β) y estrictos protocolos de seguridad.
