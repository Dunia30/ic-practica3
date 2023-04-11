import numpy as np

def bayes():
    data = np.loadtxt("../data/Iris2Clases.txt")
    y = data[:, -1]
    X = data[:, :-1]
    K = 2

    idx = np.where(y == 0)[0]
    X1 = X[idx, :]
    idx = np.where(y == 1)[0]
    X2 = X[idx, :]

    # Calculo de m
    m1 = np.sum(X1, axis=0) / X1.shape[0]
    m2 = np.sum(X2, axis=0) / X2.shape[0]

    # Calculo de C
    C1 = np.dot((X1 - m1).T, X1 - m1) / X1.shape[0]
    C2 = np.dot((X2 - m2).T, X2 - m2) / X2.shape[0]

    # Cargamos los 3 datos de ejemplo y comprobamos a que clase pertenece cada uno
    data = np.zeros((3, X.shape[1] + 1))
    data[:, :-1] = np.loadtxt("TestIris01.txt"), np.loadtxt("TestIris02.txt"), np.loadtxt("TestIris03.txt")
    y = data[:, -1]
    X = data[:, :-1]

    for i in range(X.shape[0]):
        verosimilitud = np.zeros(2)
        verosimilitud[0] = (1 / ( ((2*np.pi)**(X.shape[1]/2)) * (np.linalg.det(C1)**(1/2))))*np.exp((-1/2)* np.dot((X[i,:] - m1), np.dot(np.linalg.pinv(C1), (X[i,:] - m1).T)))
        verosimilitud[1] = (1 / ( ((2*np.pi)**(X.shape[1]/2)) * (np.linalg.det(C2)**(1/2))))*np.exp((-1/2)* np.dot((X[i,:] - m2), np.dot(np.linalg.pinv(C2), (X[i,:] - m2).T)))

        # normalizamos las verosimilitudes
        sumaverosimilitud = np.sum(verosimilitud)
        verosimilitud /= sumaverosimilitud

        if (verosimilitud[0] > verosimilitud[1] and y[i] == 0):
            print("is: Iris-setosa ; classified as: Iris-setosa ; \t right")
        elif (verosimilitud[0] > verosimilitud[1] and y[i] == 1):
            print("is: Iris-versicolor ; classified as: Iris-setosa ; \t wrong")
        elif (verosimilitud[0] <= verosimilitud[1] and y[i] == 1):
            print("is: Iris-versicolor ; classified as: Iris-versicolor ; \t right")
        elif (verosimilitud[0] <= verosimilitud[1] and y[i] == 0):
            print("is: Iris-setosa ; classified as: Iris-versicolor ; \t wrong")
bayes();