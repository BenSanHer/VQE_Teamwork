# VQE Básico - Modelo de Heisenberg

El objetivo principal de este proyecto consiste en implementar un algoritmo *Variational Quantum Eigensolver* (VQE) para encontrar la energía del estado fundamental en un modelo de Heisenberg para dos qubits. El repositorio contiene la definición del Hamiltoniano, diferentes arquitecturas de circuitos cuánticos (*Ansatz*) y la ejecución del ciclo híbrido de optimización.

## Descripción del Problema
El proyecto busca minimizar el valor esperado del próximo Hamiltoniano:

$H = 1.0(Z_0 \otimes Z_1) + 1.0(X_0 \otimes X_1)$

La energía teórica mínima conocida para este modelo alcanza el valor de -2.0.

## Estructura del Repositorio

* **`vqeBase.ipynb`**: Cuaderno principal de Jupyter. Aquí puedes definir el Hamiltoniano, establecer los ángulos iniciales, ejecutar el experimento VQE de forma local y conectar con el entorno de IBM Quantum.
* **`defs.py`**: Archivo central que alberga las funciones clave del proyecto:
    * `ansatz()`: Construye el circuito cuántico parametrizado. Incluye 5 opciones distintas de arquitectura para experimentar con "Expresividad vs Entrenabilidad".
    * `visualizar_ansatz()`: Renderiza diagramas visuales del circuito elegido usando Matplotlib.
    * `ejecutar_vqe_local()`: Ejecuta el ciclo híbrido cuántico-clásico completo en una máquina local mediante el optimizador de descenso de gradiente.
    * `enviar_job_ibm_modular()`: Permite autenticar y mandar el circuito final optimizado a los simuladores o computadoras cuánticas reales de IBM.

## Requisitos Previos

Para ejecutar el código correctamente, requieres instalar los próximos paquetes de Python:

* `pennylane`
* `qiskit-ibm-runtime`
* `numpy`
* `matplotlib`

## Instrucciones de Uso

### 1. Ejecución Local (Simulación)
1. Abre el documento `vqeBase.ipynb`.
2. Ejecuta las celdas en orden.
3. El código iniciará el proceso VQE usando el *Ansatz* 1. Observarás el progreso del optimizador paso a paso hasta alcanzar una energía muy cercana a -2.0 (ej. -1.99999).

### 2. Ejecución Remota (IBM Quantum)
El cuaderno de Jupyter incluye una celda comentada al final destinada a interactuar con el hardware de IBM.

> **Nota Importante:** Antes de activar esta función, debes configurar tus credenciales de IBM Quantum en tu entorno local.

Ajusta las variables globales en la última celda acorde a tus necesidades:
* `USAR_SIMULADOR_IBM = False` (Para acceder a un refrigerador cuántico real).
* `USAR_SIMULADOR_IBM = True` (Para correr simulaciones rápidas en la nube de IBM).
