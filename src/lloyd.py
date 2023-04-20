import numpy as np
import pandas as pd


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


# Constantes
TOLERANCIA = 1e-10
K_MAX = 10
RAZON_APRENDIZAJE = 0.1

# Calcular centro actualizado


def calcularCentroActualizado(centro, muestra):
    return centro + RAZON_APRENDIZAJE * (muestra - centro)

# Encontrar centro mas cercano a un punto


def centroMasCercano(punto, centroSetosa, centroVersicolor):
    distanciaCuadradaSetosa = np.sum(np.square(punto - centroSetosa))
    distanciaCuadradaVersicolor = np.sum(np.square(punto - centroVersicolor))

    if distanciaCuadradaSetosa >= distanciaCuadradaVersicolor:
        return "Setosa"
    else:
        return "Versicolor"


# Criterio de finalizacion
def criterioFinalizacion(centros, centrosActualizados):
    for i in range(len(centros)):
        diferencia = np.linalg.norm(centros[i] - centrosActualizados[i])

        if (diferencia > TOLERANCIA):
            return False

    return True


# Algoritmo de LLoyd
def lloyd():
    terminado = False
    irisSetosa, irisVersicolor = lecturaDeFichero()
    k = 1

    # Inicializar los centros (como vectores verticales)
    centroSetosa = np.array([4.6, 3.0, 4.0, 0.0]).T
    centroVersicolor = np.array([6.8, 3.4, 4.6, 0.7]).T

    while not terminado or k > K_MAX:
        centroSetosaActualizado = np.copy(centroSetosa)
        centroVersicolorActualizado = np.copy(centroVersicolor)

        # Calcular centro setosa actualizado
        for muestra in irisSetosa:
            muestraVector = np.array(muestra)

            centroSetosaActualizado = calcularCentroActualizado(
                centroSetosaActualizado, muestraVector)

        # Calcular centro versicolor actualizado
        for muestra in irisVersicolor:
            muestraVector = np.array(muestra)

            centroVersicolorActualizado = calcularCentroActualizado(
                centroVersicolorActualizado, muestraVector)

        k += 1
        terminado = criterioFinalizacion([centroSetosa, centroVersicolor], [
                                         centroSetosaActualizado, centroVersicolorActualizado])

        # Actualizar centro setosa
        centroSetosa = np.copy(centroSetosaActualizado)

        # Actualizar centro versicolor
        centroVersicolor = np.copy(centroVersicolorActualizado)


# TODO: Probar ejemplos

lloyd()
