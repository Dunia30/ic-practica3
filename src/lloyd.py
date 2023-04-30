import numpy as np

# Constantes
TOLERANCIA = 1e-10
K_MAX = 10
RAZON_APRENDIZAJE = 0.1

# Calcular centro actualizado
def calcularCentroActualizado(centro, muestra):
    return centro + RAZON_APRENDIZAJE * (muestra - centro)

# Encontrar centro mas cercano a un punto
def resultadoLloyd(punto, centroSetosa, centroVersicolor):
    centroSetosa_c = np.array(centroSetosa)
    centroVersicolor_c = np.array(centroVersicolor)

    distanciaCuadradaSetosa = np.sum(np.square(punto - centroSetosa_c))
    distanciaCuadradaVersicolor = np.sum(np.square(punto - centroVersicolor_c))

    if distanciaCuadradaSetosa <= distanciaCuadradaVersicolor:
        return "Iris-setosa"
    else:
        return "Iris-versicolor"

# Criterio de finalizacion
def criterioFinalizacion(centros, centrosActualizados):
    for i in range(len(centros)):
        diferencia = np.linalg.norm(centros[i] - centrosActualizados[i])

        if (diferencia > TOLERANCIA):
            return False

    return True


def lloyd(irisSetosa, centroSetosa, irisVersicolor, centroVersicolor):
    terminado = False
    k = 1

    centroSetosa_c = np.array(centroSetosa).T
    centroVersicolor_c = np.array(centroVersicolor).T

    while not terminado or k > K_MAX:
        centroSetosaActualizado = np.copy(centroSetosa_c)
        centroVersicolorActualizado = np.copy(centroVersicolor_c)

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
        terminado = criterioFinalizacion([centroSetosa_c, centroVersicolor_c], [
                                         centroSetosaActualizado, centroVersicolorActualizado])

        # Actualizar centro setosa
        centroSetosa_c = np.copy(centroSetosaActualizado)

        # Actualizar centro versicolor
        centroVersicolor_c = np.copy(centroVersicolorActualizado)

        return [centroSetosa_c, centroVersicolor_c]
