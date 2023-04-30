import numpy as np


def bayes(Iris_setosa, Iris_versicolor):
    Iris_setosa_c = np.array(Iris_setosa)
    Iris_versicolor_c = np.array(Iris_versicolor)

    suma1 = np.array([0, 0, 0, 0])
    suma2 = np.array([0, 0, 0, 0])

    for muestra_s in Iris_setosa_c:
        suma1 = np.add(suma1, muestra_s)

    for muestra_v in Iris_versicolor_c:
        suma2 = np.add(suma2, muestra_v)

    m1 = np.multiply(suma1, 1/len(Iris_setosa_c))
    m2 = np.multiply(suma2, 1/len(Iris_versicolor_c))

    # print(m1, m2)
    c1_in = np.array([])
    for i, muestra_s in enumerate(Iris_setosa_c):
        n = np.subtract(muestra_s, m1)[np.newaxis]
        t = np.subtract(muestra_s, m1)[np.newaxis].T
        t_n = np.dot(t, n)
        if i == 0:
            aux = t_n
        else:
            sum = np.add(aux, t_n)
            c1_in = sum

    c1 = np.multiply(c1_in, 1/len(Iris_setosa_c))

    c2_in = np.array([])
    for i, muestra_v in enumerate(Iris_versicolor_c):
        n = np.subtract(muestra_v, m2)[np.newaxis]
        t = np.subtract(muestra_v, m2)[np.newaxis].T
        t_n = np.dot(t, n)
        if i == 0:
            aux = t_n
        else:
            sum = np.add(aux, t_n)
            c2_in = sum

    c2 = np.multiply(c2_in, 1/len(Iris_versicolor_c))

    return [c1, m1, c2, m2]


def resultadoBayes(muestra, m_setosa, m_versicolor):
    n_m1 = np.subtract(muestra, m_setosa)[np.newaxis]
    t_m1 = np.subtract(muestra, m_setosa)[np.newaxis].T
    n_m2 = np.subtract(muestra, m_versicolor)[np.newaxis]
    t_m2 = np.subtract(muestra, m_versicolor)[np.newaxis].T
    inter_s = np.dot(n_m1, np.identity(4))
    inter_v = np.dot(n_m2, np.identity(4))
    dis_s = np.dot(inter_s, t_m1)
    dis_v = np.dot(inter_v, t_m2)
    if np.greater(dis_s, dis_v):
        return "Iris-versicolor"
    else:
        return "Iris-setosa"
