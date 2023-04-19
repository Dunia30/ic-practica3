import math
# Constantes
E = 0.01  # Tolerancia
b = 2  # Peso exponencial
centrosSetosa = [4.6, 3.0, 4.0, 0.0]
centrosVersi = [6.8, 3.4, 4.6, 0.7]


def lecturaDeFichero():
    # Crear un diccionario vacío
    Iris_setosa = []
    Iris_versicolor=[]
    # Abrir el archivo para leer
    with open('../data/Iris2Clases.txt', 'r') as archivo:
        # Leer cada línea del archivo
        for linea in archivo:
            # Separar los elementos por coma
            elementos = linea.strip().split(',')

            # Crear la lista de elementos numéricos
            numeros = [float(x) for x in elementos[:-1]]

            if elementos[-1]=="Iris-setosa":
                Iris_setosa.append(numeros)
            else:
                Iris_versicolor.append(numeros)

    return [Iris_setosa, Iris_versicolor]


def k_medias():
    global E
    global b
    global centrosSetosa
    global centrosVersi
    salir = False
    iteracion = 1
    [Iris_setosa, Iris_versicolor] = lecturaDeFichero()

    while not salir:
        print(f'Iteración número: {iteracion}')
        # Calculamos el exponente
        exponente = 1 / (b - 1)
        # Si hay el mismo numero de elementos en las 2 clases entonces basta con resolverlo
        # para una de ellas y el resultado de la otra sera la resta de ese valor a 1
        d = []
        # Se calculan los valores de 'd' para irisSetosa
        for i in range(len(Iris_setosa)):
            res = []
            djSetosa = 0
            djVersicolor = 0

            for j in range(len(Iris_setosa[i])):

                djSetosa += math.pow(Iris_setosa[i][j] - centrosSetosa[j], 2)
                djVersicolor += math.pow(Iris_setosa[i][j] - centrosVersi[j], 2)

            res.append(djSetosa)  # valor [0] del array === Setosa
            res.append(djVersicolor)  # valor [1] del array === VersiColor
           
            d.append(res)

        # Se calculan los valores de d para irisVersicolor
        for i in range(len(Iris_versicolor)):
            res = []
            djSetosa = 0
            djVersicolor = 0
            for j in range(len(Iris_versicolor[i])):
                djSetosa += math.pow(Iris_versicolor
                                     [i][j] - centrosSetosa[j], 2)
                djVersicolor += math.pow(Iris_versicolor
                                         [i][j] - centrosVersi[j], 2)

            res.append(djSetosa)  # valor [0] del array === Setosa
            res.append(djVersicolor)  # valor [1] del array === VersiColor
            d.append(res)

        MatrizProbabilidadesK = []  # Matriz de probabilidades
        sumasDeterminantes = []
        for i in range(len(d)):
            auxi = 0

            for j in range(2):
                auxi += math.pow(1 / d[i][j], exponente)

            sumasDeterminantes.append(auxi)

        for i in range(len(d)):
            aux = []

            res = math.pow(1 / d[i][0], exponente) / sumasDeterminantes[i]

            aux.append(res)
            aux.append(1 - res)
            MatrizProbabilidadesK.append(aux)

        nuevoCentroSetosa = []
        nuevoCentroVersi = []
        for i in range(len(centrosSetosa)):  # Nuevo Centro para la clase Iris Setosa
            aux1 = 0
            aux2 = 0
            for j in range(len(Iris_setosa)):
                aux1 += math.pow(MatrizProbabilidadesK[j]
                                 [0], b) * Iris_setosa[j][i]
                aux2 += math.pow(MatrizProbabilidadesK[j][0], b)

            for j in range(len(Iris_versicolor)):
                aux1 += math.pow(MatrizProbabilidadesK[len(Iris_setosa) + j]
                                 [0], b) * Iris_versicolor[j][i]
                aux2 += math.pow(
                    MatrizProbabilidadesK[len(Iris_setosa) + j][0], b)

            nuevoCentroSetosa.append(aux1 / aux2)

        for i in range(len(centrosVersi)):  # Nuevo centro para la lase Iris Versicolor
            aux1 = 0
            aux2 = 0
            for j in range(len(Iris_setosa)):
                aux1 += math.pow(MatrizProbabilidadesK[j]
                                 [1], b) * Iris_setosa[j][i]
                aux2 += math.pow(MatrizProbabilidadesK[j][1], b)

            for j in range(len(Iris_versicolor)):
                aux1 += math.pow(MatrizProbabilidadesK[len(Iris_setosa) + j]
                                 [1], b) * Iris_versicolor[j][i]
                aux2 += math.pow(
                    MatrizProbabilidadesK[len(Iris_setosa) + j][1], b)

            nuevoCentroVersi.append(aux1 / aux2)

        salir = criterioConver(nuevoCentroSetosa, nuevoCentroVersi)

        centrosVersi = nuevoCentroVersi
        centrosSetosa = nuevoCentroSetosa
        iteracion += 1


def criterioConver(nuevoCentroSetosa, nuevoCentroVersi):
    i = 0
    aux1 = 0

    while (i < len(centrosSetosa)):  # Comprueba el centro de Iris-Setosa
        value = math.pow(nuevoCentroSetosa[i] - centrosSetosa[i], 2)
        aux1 += math.pow(nuevoCentroSetosa[i] - centrosSetosa[i], 2)

        i += 1

    if (math.sqrt(aux1) > E):
        return False  # Continua iterando
    else:
        j = 0
        aux2 = 0
        while (j < len(centrosVersi)):  # Comprueba el centro Iris-Versicolor
            aux2 += math.pow(nuevoCentroVersi[j] - centrosVersi[j], 2)
            j += 1
        if (math.sqrt(aux2) > E):
            return False  # Continua iterando

    return True  # Se acabo iterars


def resultadoKMedias(ejemplo):  # Devuelve la clase resultante del metodo de K-Medias
    resultSetosa = 0
    resultVersiColor = 0

    for i in range(len(centrosSetosa)):
        resultSetosa += math.pow(ejemplo[i] - centrosSetosa[i], 2)

    for i in range(len(centrosSetosa)):
        resultVersiColor += math.pow(ejemplo[i] - centrosVersi[i], 2)

    if (resultSetosa < resultVersiColor):
        return 'Iris-setosa'
    else:
        return 'Iris-versicolor'


k_medias()

print(f'Nuevo centro Setosa: {centrosSetosa}')
print(f'Nuevo centro Versicolor: {centrosVersi}')
