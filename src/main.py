import sys

from lloyd import lloyd, resultadoLloyd
from kMedias import k_medias, resultadoKMedias
from bayes import bayes, resultadoBayes

# Devuelve dos listas con las muestras de cada clase
def lecturaDeFichero():
    # Crear un diccionario vacío
    Iris_setosa = []
    Iris_versicolor = []
    # Abrir el archivo para leer
    with open('data/Iris2Clases.txt', 'r') as archivo:
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

            ejemplo["punto"] = numeros
            ejemplo["clase"] = elementos[-1]

    return ejemplo

# Ejecutar pruebas
def probarCentros(titulo, centroSetosaActualizado, centroVersicolorActualizado, calcularClase):
    print("===", titulo, "===")

    # Imprimir centros actualizados
    print("  === Centros Actualizados ===")
    print("    Iris-setosa:", centroSetosaActualizado, sep="\t")
    print("    Iris-versicolor:", centroVersicolorActualizado, sep="\t")
    print("  ============================")

    ejemplo1 = analizarEjemplo("data/TestIris01.txt")
    claseEjemplo1 = calcularClase(
        ejemplo1["punto"], centroSetosaActualizado, centroVersicolorActualizado)
    print("  === Ejemplo1 ===")
    print("    Resultado:", claseEjemplo1, sep="\t")
    print("    Esperado:", ejemplo1["clase"], sep="\t")
    print("  ================")

    ejemplo2 = analizarEjemplo("data/TestIris02.txt")
    claseEjemplo2 = calcularClase(
        ejemplo2["punto"], centroSetosaActualizado, centroVersicolorActualizado)
    print("  === Ejemplo2 ===")
    print("    Resultado:", claseEjemplo2, sep="\t")
    print("    Esperado:", ejemplo2["clase"], sep="\t")
    print("  ================")

    ejemplo3 = analizarEjemplo("data/TestIris03.txt")
    claseEjemplo3 = calcularClase(
        ejemplo3["punto"], centroSetosaActualizado, centroVersicolorActualizado)
    print("  === Ejemplo3 ===")
    print("    Resultado:", claseEjemplo3, sep="\t")
    print("    Esperado:", ejemplo3["clase"], sep="\t")
    print("  ================")

    ejemplo4 = analizarEjemplo("data/TestIris04.txt")
    claseEjemplo4 = calcularClase(
        ejemplo4["punto"], centroSetosaActualizado, centroVersicolorActualizado)
    print("  === Ejemplo4 ===")
    print("    Resultado:", claseEjemplo4, sep="\t")
    print("    Esperado:", ejemplo4["clase"], sep="\t")
    print("  ================")

    ejemplo5 = analizarEjemplo("data/TestIris05.txt")
    claseEjemplo5 = calcularClase(
        ejemplo5["punto"], centroSetosaActualizado, centroVersicolorActualizado)
    print("  === Ejemplo5 ===")
    print("    Resultado:", claseEjemplo5, sep="\t")
    print("    Esperado:", ejemplo5["clase"], sep="\t")
    print("  ================")

    ejemplo6 = analizarEjemplo("data/TestIris06.txt")
    claseEjemplo6 = calcularClase(
        ejemplo6["punto"], centroSetosaActualizado, centroVersicolorActualizado)
    print("  === Ejemplo6 ===")
    print("    Resultado:", claseEjemplo6, sep="\t")
    print("    Esperado:", ejemplo6["clase"], sep="\t")
    print("  ================")



    print("=" * (len(titulo) + 8))


def probarBayes(titulo, covarianzaSetosa, mSetosa, covarianzaVersicolor, mVersicolor, calcularClase):
    print("===", titulo, "===")

    # Imprimir medias
    print("  === Medias ===")
    print("    Iris-setosa:", mSetosa, sep="\t")
    print("    Iris-versicolor:", mVersicolor, sep="\t")
    print("  ============================")

    # Imprimir covarianzas
    print("  === Covarianzas ===")
    print("    Iris-setosa:", covarianzaSetosa, sep="\n")
    print("    Iris-versicolor:", covarianzaVersicolor, sep="\n")
    print("  ============================")

    ejemplo1 = analizarEjemplo("data/TestIris01.txt")
    claseEjemplo1 = calcularClase(
        ejemplo1["punto"], mSetosa, mVersicolor)
    print("  === Ejemplo1 ===")
    print("    Resultado:", claseEjemplo1, sep="\t")
    print("    Esperado:", ejemplo1["clase"], sep="\t")
    print("  ================")

    ejemplo2 = analizarEjemplo("data/TestIris02.txt")
    claseEjemplo2 = calcularClase(
        ejemplo2["punto"], mSetosa, mVersicolor)
    print("  === Ejemplo2 ===")
    print("    Resultado:", claseEjemplo2, sep="\t")
    print("    Esperado:", ejemplo2["clase"], sep="\t")
    print("  ================")

    ejemplo3 = analizarEjemplo("data/TestIris03.txt")
    claseEjemplo3 = calcularClase(
        ejemplo3["punto"], mSetosa, mVersicolor)
    print("  === Ejemplo3 ===")
    print("    Resultado:", claseEjemplo3, sep="\t")
    print("    Esperado:", ejemplo3["clase"], sep="\t")
    print("  ================")

    ejemplo4 = analizarEjemplo("data/TestIris04.txt")
    claseEjemplo4 = calcularClase(
        ejemplo4["punto"], mSetosa, mVersicolor)
    print("  === Ejemplo4 ===")
    print("    Resultado:", claseEjemplo4, sep="\t")
    print("    Esperado:", ejemplo4["clase"], sep="\t")
    print("  ================")

    ejemplo5 = analizarEjemplo("data/TestIris05.txt")
    claseEjemplo5 = calcularClase(
        ejemplo5["punto"], mSetosa, mVersicolor)
    print("  === Ejemplo5 ===")
    print("    Resultado:", claseEjemplo5, sep="\t")
    print("    Esperado:", ejemplo5["clase"], sep="\t")
    print("  ================")

    ejemplo6 = analizarEjemplo("data/TestIris06.txt")
    claseEjemplo6 = calcularClase(
        ejemplo6["punto"], mSetosa, mVersicolor)
    print("  === Ejemplo6 ===")
    print("    Resultado:", claseEjemplo6, sep="\t")
    print("    Esperado:", ejemplo6["clase"], sep="\t")
    print("  ================")

    print("=" * (len(titulo) + 8))


def main() -> int:
    # Obtener las muestras
    irisSetosa, irisVersicolor = lecturaDeFichero()

    # Inicializar los centros
    centroSetosa = [4.6, 3.0, 4.0, 0.0]
    centroVersicolor = [6.8, 3.4, 4.6, 0.7]

    # Imprimir centros
    print("=== Centros Iniciales ===")
    print("  Iris-setosa:", centroSetosa, sep="\t\t")
    print("  Iris-versicolor:", centroVersicolor, sep="\t")
    print("=========================")

    print()

    # Ejecutar K-Medias
    centroSetosaActualizado, centroVersicolorActualizado = k_medias(
        irisSetosa, irisVersicolor, centroSetosa, centroVersicolor)

    # Pruebas K-Medias
    probarCentros("Algoritmo K-Medias", centroSetosaActualizado,
                  centroVersicolorActualizado, resultadoKMedias)

    print()

    # Ejecutar Bayes
    covarianzaSetosa, mSetosa, covarianzaVeriscolor, mVersicolor = bayes(
        irisSetosa, irisVersicolor)

    # Probar Bayes
    probarBayes("Estimacion parametrica de Bayes", covarianzaSetosa,
                mSetosa, covarianzaVeriscolor, mVersicolor, resultadoBayes)

    print()

    # Ejecutar LLoyd
    centroSetosaActualizado, centroVersicolorActualizado = lloyd(
        irisSetosa, centroSetosa, irisVersicolor, centroVersicolor)

    # Pruebas LLoyd
    probarCentros("Algoritmo LLoyd", centroSetosaActualizado,
                  centroVersicolorActualizado, resultadoLloyd)

    return 0


if __name__ == '__main__':
    sys.exit(main())
