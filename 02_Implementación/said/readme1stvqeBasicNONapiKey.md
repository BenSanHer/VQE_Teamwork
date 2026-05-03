# VQE Modular con PennyLane + IBM Quantum

## Descripción

Implementar un algoritmo **Variational Quantum Eigensolver (VQE)** de forma modular utilizando PennyLane. Resolver el estado fundamental de un Hamiltoniano simple y posteriormente ejecutar el circuito tanto en simulación local como en hardware cuántico real (IBM Quantum).

---

## Objetivo

Construir un flujo completo que permita:

- Definir un Hamiltoniano
- Diseñar distintos Ansatz
- Optimizar parámetros con un método clásico
- Visualizar circuitos
- Ejecutar resultados en hardware real

---

## Hamiltoniano

Trabajar con el siguiente Hamiltoniano:

\[
H = Z_0 Z_1 + X_0 X_1
\]

El valor esperado mínimo teórico (estado fundamental) es:

\[
E_0 = -2.0
\]

---

## Estructura del Proyecto

### 1. Definir el Hamiltoniano

Construir el operador utilizando `qml.Hamiltonian`.

---

### 2. Inicializar parámetros

Generar valores iniciales para los ángulos del circuito variacional.  
Elegir valores distintos al óptimo para forzar el proceso de optimización.

---

### 3. Diseñar el Ansatz

Implementar múltiples arquitecturas de circuitos:

- Opción 1: Con entrelazamiento (CNOT) → alcanza el óptimo
- Otras opciones: Variaciones sin suficiente expresividad

Explorar el tradeoff:

> **Expresividad vs Entrenabilidad**

---

### 4. Ejecutar VQE local

Construir el loop híbrido:

1. Crear dispositivo cuántico (`default.qubit`)
2. Definir función de costo
3. Usar `GradientDescentOptimizer`
4. Iterar optimización
5. Monitorear energía

---

### 5. Visualizar circuitos

Mostrar el Ansatz en:

- Formato texto (terminal)
- Formato gráfico (Matplotlib)

---

### 6. Ejecutar en hardware real (IBM)

Enviar el circuito optimizado a IBM Quantum:

- Autenticar con `QiskitRuntimeService`
- Seleccionar backend menos ocupado
- Ejecutar con mediciones reales (`shots`)
- Obtener energía experimental

---

## Flujo de Ejecución

```python
params_buenos = ejecutar_vqe_local(opcion_ansatz=1, pasos=50)

visualizar_ansatz(opcion_ansatz=1)

enviar_job_ibm_modular(
    params_optimizados=params_buenos,
    opcion_ansatz=1
)