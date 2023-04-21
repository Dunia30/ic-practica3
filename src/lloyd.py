import numpy as np

# Constantes
TOLERANCIA = 1e-10
K_MAX = 10
RAZON_APRENDIZAJE = 0.1

# Devuelve dos listas con las muestras de cada clase


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

# Devuelve los datos de ejemplo en un objeto


def analizarEjemplo(fichero):
    # Inicializar valores a devolver (punto, clase)
    ejemplo = {"punto": None, "clase": "Undefined"}
    # Abrir el archivo para leer
    with open(fichero, 'r') as archivo:
        # Leer cada línea del archivo
        for linea in archivo:
            # Separar los elementos por coma
            elementos = linea.strip().split(',')

            # Crear la lista de elementos numéricos
            numeros = [float(x) for x in elementos[:-1]]

            ejemplo["punto"] = np.array(numeros)
            ejemplo["clase"] = elementos[-1]

    return ejemplo


# Calcular centro actualizado
def calcularCentroActualizado(centro, muestra):
    return centro + RAZON_APRENDIZAJE * (muestra - centro)

# Encontrar centro mas cercano a un punto


def centroMasCercano(punto, centroSetosa, centroVersicolor):
    distanciaCuadradaSetosa = np.sum(np.square(punto - centroSetosa))
    distanciaCuadradaVersicolor = np.sum(np.square(punto - centroVersicolor))

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


# Algoritmo de LLoyd
def lloyd(irisSetosa, centroSetosa, irisVersicolor, centroVersicolor):
    terminado = False
    k = 1

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

        return [centroSetosa, centroVersicolor]


def main():
    # Configurar numpy
    np.set_printoptions(floatmode="maxprec_equal")

    # Obtener las muestras
    irisSetosa, irisVersicolor = lecturaDeFichero()

    # Inicializar los centros (como vectores verticales)
    centroSetosa = np.array([4.6, 3.0, 4.0, 0.0]).T
    centroVersicolor = np.array([6.8, 3.4, 4.6, 0.7]).T

    centroSetosaActualizado, centroVersicolorActualizado = lloyd(
        irisSetosa, centroSetosa, irisVersicolor, centroVersicolor)

    # Imprimir centros
    print("=== Centros Iniciales ===")
    print("  · Iris-setosa:", centroSetosa, sep="\t")
    print("  · Iris-versicolor:", centroVersicolor, sep="\t")
    print("=========================")

    print("=== Centros Actualizados ===")
    print("  · Iris-setosa:", centroSetosaActualizado, sep="\t")
    print("  · Iris-versicolor:", centroVersicolorActualizado, sep="\t")
    print("============================")

    # Probar ejemplos
    ejemplo1 = analizarEjemplo("../data/TestIris01.txt")
    claseEjemplo1 = centroMasCercano(
        ejemplo1["punto"], centroSetosaActualizado, centroVersicolorActualizado)
    print("=== Ejemplo1 ===")
    print("  · Resultado:", claseEjemplo1, sep="\t")
    print("  · Esperado:", ejemplo1["clase"], sep="\t")
    print("================")

    ejemplo2 = analizarEjemplo("../data/TestIris02.txt")
    claseEjemplo2 = centroMasCercano(
        ejemplo2["punto"], centroSetosaActualizado, centroVersicolorActualizado)
    print("=== Ejemplo2 ===")
    print("  · Resultado:", claseEjemplo2, sep="\t")
    print("  · Esperado:", ejemplo2["clase"], sep="\t")
    print("================")

    ejemplo3 = analizarEjemplo("../data/TestIris03.txt")
    claseEjemplo3 = centroMasCercano(
        ejemplo3["punto"], centroSetosaActualizado, centroVersicolorActualizado)
    print("=== Ejemplo3 ===")
    print("  · Resultado:", claseEjemplo3, sep="\t")
    print("  · Esperado:", ejemplo3["clase"], sep="\t")
    print("================")


main()
