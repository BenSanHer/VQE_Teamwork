# VQE Básico - Modelo de Heisenberg

Este proyecto implementa un algoritmo *Variational Quantum Eigensolver* (VQE) para encontrar la energía del estado fundamental de un modelo de Heisenberg de dos qubits. El repositorio contiene la definición del Hamiltoniano, distintas arquitecturas de circuitos cuánticos (*ansatz*) y la ejecución del ciclo híbrido de optimización.

## Descripción del problema

El objetivo es minimizar el valor esperado del siguiente Hamiltoniano:

$$
H = 1.0(Z_0 \otimes Z_1) + 1.0(X_0 \otimes X_1)
$$

La energía teórica mínima conocida para este modelo es **-2.0**.

## Estructura del repositorio

- **`vqeBase.ipynb`**: Cuaderno principal donde se define el Hamiltoniano, se configuran los parámetros iniciales y se ejecuta el experimento VQE, tanto de forma local como en IBM Quantum.

- **`defs.py`**: Archivo que contiene las funciones principales del proyecto:
  - `ansatz()`: Construye el circuito cuántico parametrizado con distintas arquitecturas.
  - `visualizar_ansatz()`: Genera diagramas del circuito utilizando Matplotlib.
  - `ejecutar_vqe_local()`: Ejecuta el ciclo híbrido cuántico-clásico en entorno local.
  - `enviar_job_ibm_modular()`: Permite enviar el circuito optimizado a simuladores o hardware de IBM.

## Requisitos previos

Instalar las siguientes dependencias:

```bash
pip install pennylane qiskit-ibm-runtime numpy matplotlib
