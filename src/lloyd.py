import numpy as np
import pandas as pd

# region Funciones auxiliares

def lecturaDeFichero():
    # Crear un diccionario vacío
    Iris_setosa = []
    Iris_versicolor = []
    # Abrir el archivo para leer
    with open('../data/Iris2Clases.txt', 'r') as archivo:
        # Leer cada línea del archivo
        for linea in archivo:
            # Separar los elementos por coma
            elementos = linea.strip().split(',')

            # Crear la lista de elementos numéricos
            numeros = [float(x) for x in elementos[:-1]]

            if elementos[-1] == "Iris-setosa":
                Iris_setosa.append(numeros)
            else:
                Iris_versicolor.append(numeros)

    return [Iris_setosa, Iris_versicolor]

# endregion


# Constantes
TOLERANCIA = 1e-10
K_MAX = 10
RAZON_APRENDIZAJE = 0.1

# Inicializar los centros
centrosSetosa = [4.6, 3.0, 4.0, 0.0]
centrosVersicolor = [6.8, 3.4, 4.6, 0.7]

# Algoritmo de LLoyd
def lloyd(datos):
    terminado = False
    irisSetosa, irisVersicolor = datos
    k = 1

    while not terminado and k <= K_MAX:

        k += 1


lloyd(lecturaDeFichero())
