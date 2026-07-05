# **Resumen de Modelos de Decaimiento Exponencial Aplicados**

| **Campo de Aplicación** | **Variable Principal** | **Ecuación Base** | **Parámetros Clave** | **Variables de Influencia** | **Caso de Estudio** |
|-------------------------|------------------------|-------------------|---------------------|----------------------------|---------------------|
| **Decaimiento Radiactivo** | Núcleos no desintegrados | `N(t) = N₀e^(-λt)` | λ = Constante de decaimiento<br>t₁/₂ = Vida media | Tipo de partícula (α, β, γ)<br>Energía de transición | Uranio-238 → Torio-234 |
| **Recursos Hídricos** | Disponibilidad de agua | `V(t) = V₀e^(-λt)`<br>`λ = αM + βI + γD` | α = Impacto minero<br>β = Gobernanza<br>γ = Demanda local | Hectáreas mineras (M)<br>Institucionalidad (I)<br>Crecimiento poblacional (D) | Páramo de Santurbán, Colombia |
| **Riesgo Crediticio** | Probabilidad de supervivencia | `P_surv(t) = e^(-λt)`<br>`λ = λ₀ + ΣβᵢXᵢ` | λ₀ = Riesgo base<br>βᵢ = Peso variables<br>Xᵢ = Variables macro | Desempleo<br>PIB<br>Inestabilidad política<br>Tasas de interés | Crisis Argentina 2001-2002 |
| **Riesgo de Inversión** | Valor de la inversión | `V(t) = V₀e^(-λt)`<br>`λ = λ_econ + λ_pol + λ_reg` | λ_econ = Inflación/Recesión<br>λ_pol = Inestabilidad<br>λ_reg = Riesgo regulatorio | Control cambiario<br>Default soberano<br>Cambios regulatorios | Argentina 2023-2024 |
| **Farmacocinética** | Concentración del fármaco | `C(t) = C₀e^(-kt)` | k = Constante de eliminación<br>t₁/₂ = Vida media plasmática | Función renal/hepática<br>Metabolismo | Ibuprofeno (t₁/₂ ≈ 2h) |
| **Contaminantes Ambientales** | Concentración de contaminante | `C(t) = C₀e^(-λt)` | λ = Tasa de degradación<br>t₁/₂ = Vida media ambiental | Condiciones climáticas<br>Propiedades del suelo<br>Microorganismos | Cesio-137 en suelos |

---

## **Patrones Comunes Identificados**

### **1. Estructura Matemática Universal**
```
dX/dt = -λX  →  X(t) = X₀e^(-λt)
```
Donde **X** representa la cantidad que decae y **λ** la tasa de decaimiento.

### **2. Adaptaciones para Sistemas Complejos**
- **λ constante**: Sistemas puros (decaimiento radiactivo)
- **λ(t) dinámica**: Sistemas con influencias externas
  - `λ(t) = f(variables socioeconómicas, políticas, ambientales)`

### **3. Métodos de Validación**
- **Ajuste por mínimos cuadrados** a datos experimentales
- **Estimación de parámetros** con regresión no lineal
- **Validación cruzada** con datos históricos

---

## **Limitaciones y Extensiones**

| **Modelo** | **Limitaciones** | **Extensiones Propuestas** |
|------------|------------------|---------------------------|
| **Todos** | Supone independencia de eventos | Incorporar correlaciones temporales |
| **Recursos hídricos** | No captura umbrales de colapso | Modelos con puntos de no retorno |
| **Riesgo financiero** | Asume normalidad en distribuciones | Usar distribuciones de cola pesada (Cauchy, Pareto) |
| **Contaminantes** | Ignora interacciones entre compuestos | Modelos de decaimiento acoplado |

---

## **Herramientas Computacionales Utilizadas**

- **Python**: `scipy.optimize.curve_fit`, `numpy`, `matplotlib`
- **Lenguajes históricos**: True BASIC (programa original de decaimiento)
- **Software especializado**: MODFLOW (hidrología), COPASI (bioquímica)

---

## **Principio Fundamental**

> **"El decaimiento exponencial emerge en sistemas donde la tasa de cambio es proporcional al estado actual, independientemente del dominio científico"**

Esta universalidad permite transferir metodologías entre disciplinas aparentemente no relacionadas, desde la física nuclear hasta la economía conductual.
