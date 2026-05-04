import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt
from qiskit_ibm_runtime import QiskitRuntimeService
'''
Index:
A) Del Ansatz
    A.1) Definir varios Ansatz
    A.2) Visualización del Ansatz
B) Del VQE
    B.1) VQE
C) Del Envío a IBM Quantum
    C.1) Enviar el circuito a IBM consumiendo las variables globales de configuración.
'''


##############################
# A) Del Anzatz 
    #A.1) Defirnit varios Ansatz
def ansatz(params, opcion=1):
    """
    Construir el circuito cuántico parametrizado (el Ansatz de Rayleigh-Ritz).
    
    Entradas:
        params (array-like): Lista o tensor con los ángulos a inyectar en las compuertas.
        opcion (int): Selector numérico (1 al 5) para cambiar la arquitectura del circuito.
        
    Salidas:
        Ninguna. (Aplicar las compuertas in-place en el QNode actual).
        
    Qué hace:
        Aplicar operaciones unitarias a los qubits. Contiene 5 arquitecturas distintas
        para experimentar con el concepto de "Expresividad vs Entrenabilidad".
        La Opción 1 es capaz de generar el entrelazamiento necesario para llegar 
        a la energía de -2.0 según la literatura.
    """
    if opcion == 1:
        qml.RY(params[0], wires=0)
        qml.RY(params[1], wires=1)
        qml.CNOT(wires=[0, 1])
        
    elif opcion == 2:
        qml.RY(params[0], wires=0)
        qml.RY(params[1], wires=1)
        
    elif opcion == 3:
        qml.RX(params[0], wires=0)
        qml.RZ(params[1], wires=1)
        qml.CNOT(wires=[0, 1])
        
    elif opcion == 4:
        qml.RY(params[0], wires=0)
        qml.RX(params[1], wires=1)
        qml.CZ(wires=[0, 1])
        qml.RY(params[0], wires=1)
        
    elif opcion == 5:
        qml.CNOT(wires=[0, 1])
        qml.RY(params[0], wires=0)
        qml.RY(params[1], wires=1)

    # A.2) Visualización del Ansatz
def visualizar_ansatz(opcion_ansatz=1):
    """
    Dibujar la arquitectura del circuito cuántico seleccionado.
    
    Entradas:
        opcion_ansatz (int): El número de Ansatz (1 al 5) que quiero visualizar.
        
    Salidas:
        Mostrar un gráfico renderizado con Matplotlib.
    """
    # Necesitar un dispositivo y un QNode "de mentira" solo para poder dibujarlo
    dev_dibujo = qml.device("default.qubit", wires=2)
    
    @qml.qnode(dev_dibujo)
    def circuito_dummy(params):
        ansatz(params, opcion=opcion_ansatz)
        # El retorno no importar para el dibujo, solo poner una medición cualquiera
        return qml.expval(qml.PauliZ(0)) 
    
    # Crear unos ángulos arbitrarios solo para que el dibujante tenga qué mostrar
    angulos_ejemplo = np.array(["i", "j"])
    
    print(f"Arquitectura del Ansatz Opción {opcion_ansatz}")
    fig, ax = qml.draw_mpl(circuito_dummy, decimals=2)(angulos_ejemplo)
    plt.show()


##############################
# B) Del VQE
    # B.1) VQE
def ejecutar_vqe_local(Hamiltonian, angles, opcion_ansatz=1, pasos=50, tasa_aprendizaje=0.1):
    """
    Ejecutar el ciclo híbrido cuántico-clásico completo en mi computadora local.
    
    Entradas:
        Hamiltonian (qml.Hamiltonian): Objeto Hamiltoniano de pennylane que define el problema a resolver.
        angles (array-like): Los ángulos iniciales para el Ansatz.
        opcion_ansatz (int): Qué circuito usar (por defecto 1).
        pasos (int): Número de iteraciones del descenso de gradiente (por defecto 50).
        tasa_aprendizaje (float): El step-size del optimizador (por defecto 0.1).
        
    Salidas:
        params (tensor): Los ángulos theta finales que minimizan la energía.
        
    Qué hace:
        1. Crear un simulador cuántico local de 2 qubits.
        2. Definir la función de costo (energía esperada).
        3. Instanciar el optimizador GradientDescentOptimizer.
        4. Iterar ajustando los parámetros para minimizar la energía.
        5. Imprimir el progreso de la optimización.
    """
    dev = qml.device("default.qubit", wires=2)
    @qml.qnode(dev)
    def funcion_costo(params):
        ansatz(params, opcion=opcion_ansatz)
        # Usar exactamente el parámetro que entró a la función
        return qml.expval(Hamiltonian) 
    
    opt = qml.GradientDescentOptimizer(stepsize=tasa_aprendizaje)
    # Asignar la variable directamente, sin paréntesis
    params = angles 
    
    print(f"Iniciando VQE Local (Ansatz {opcion_ansatz})")
    print(f"Energía Inicial: {funcion_costo(params):.5f}")
    
    for i in range(pasos):
        params, energia = opt.step_and_cost(funcion_costo, params)
        if (i + 1) % 10 == 0:
            print(f"Paso {i + 1:2d} | Energía: {energia:.5f} | Ángulos: {params.numpy()}")
            
    print(f"Energía Final Optimizada: {energia:.5f}\n")
    return params


##############################
# C) Del Envío a IBM Quantum
    # C.1) Enviar el circuito a IBM
def enviar_job_ibm_modular(params_optimizados, opcion_ansatz=1):
    '''
    Envía el circuito cuántico a IBM Quantum. No corre perse VQE, solo verifica 
    la enegía de la configuración final que obtuvimos localmente.'''

    print("Autenticando con IBM Quantum...")
    try:
        # Usar el formato obligatorio: "ibm-q/open/main" o "tu-org/tu-proyecto/tu-hub"
        service = QiskitRuntimeService()
        print("Buscando el backend menos ocupado...")
        backend_ideal = service.least_busy(
            operational=True,
            simulator=USAR_SIMULADOR_IBM,
            min_num_qubits=MIN_QUBITS_REQUERIDOS
        )
        print(f"Hardware asignado: {backend_ideal.name}")  # ← Mostrar el backend seleccionado

        # Construir el dispositivo remoto de PennyLane
        dev_remote = qml.device(
            'qiskit.remote', 
            wires=MIN_QUBITS_REQUERIDOS, 
            backend=backend_ideal,
            shots=SHOTS_MEDICION
        )
        H = definir_hamiltoniano()

        @qml.qnode(dev_remote)
        def circuito_ibm(params):
            ansatz(params, opcion=opcion_ansatz)
            return qml.expval(H)

        print(f"Enviando el Ansatz {opcion_ansatz} a la fila de {backend_ideal.name}...")  # ← Indicar el envío al backend
        energia_medida = circuito_ibm(params_optimizados)
        print(f"¡Job Completado!")
        print(f"Energía medida: {energia_medida:.5f}")

    except Exception as e:
        print(f"Error en la ejecución remota: {e}")
