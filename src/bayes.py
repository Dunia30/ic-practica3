import numpy as np

def bayes():
    [Iris_setosa, Iris_versicolor] = lecturaDeFichero()
    suma1=np.array([0,0,0,0])
    suma2=np.array([0,0,0,0])

    for muestra_s in Iris_setosa:
        suma1 = np.add(suma1,muestra_s)
        

    for muestra_v in Iris_versicolor:
        suma2 = np.add(suma2,muestra_v)
    
    m1=np.multiply(suma1, 1/len(Iris_setosa))
    m2=np.multiply(suma2, 1/len(Iris_versicolor))
  
    # print(m1, m2)
    c1_in=np.array([])
    for i,muestra_s in enumerate(Iris_setosa):
        n=np.subtract(muestra_s,m1)[np.newaxis]
        t=np.subtract(muestra_s,m1)[np.newaxis].T
        t_n=np.dot(t,n)
        if i==0:
            aux=t_n
        else:
            sum=np.add(aux,t_n)
            c1_in=sum

    c1=np.multiply(c1_in,1/len(Iris_setosa))

    c2_in=np.array([])
    for i,muestra_v in enumerate(Iris_versicolor):
        n=np.subtract(muestra_v,m2)[np.newaxis]
        t=np.subtract(muestra_v,m2)[np.newaxis].T
        t_n=np.dot(t,n)
        if i==0:
            aux=t_n
        else:
            sum=np.add(aux,t_n)
            c2_in=sum
    
    c2=np.multiply(c2_in,1/len(Iris_versicolor))
    


    for i,muestra_s in enumerate(Iris_setosa):
        n_m1=np.subtract(muestra_s,m1)[np.newaxis]
        t_m1=np.subtract(muestra_s,m1)[np.newaxis].T
        n_m2=np.subtract(muestra_s,m2)[np.newaxis]
        t_m2=np.subtract(muestra_s,m2)[np.newaxis].T
        inter_s=np.dot(n_m1,np.identity(4))
        inter_v=np.dot(n_m2,np.identity(4))
        dis_s=np.dot(inter_s,t_m1)
        dis_v=np.dot(inter_v,t_m2)
        if  np.greater(dis_s , dis_v):
            print("Iris_versicolor")
        else:
            print("Iris_setosa")

    for i,muestra_v in enumerate(Iris_versicolor):
        n_m1=np.subtract(muestra_v,m1)[np.newaxis]
        t_m1=np.subtract(muestra_v,m1)[np.newaxis].T
        n_m2=np.subtract(muestra_v,m2)[np.newaxis]
        t_m2=np.subtract(muestra_v,m2)[np.newaxis].T
        inter_s=np.dot(n_m1,np.identity(4))
        inter_v=np.dot(n_m2,np.identity(4))
        dis_s=np.dot(inter_s,t_m1)
        dis_v=np.dot(inter_v,t_m2)
        if np.greater(dis_s , dis_v):
            print("Iris_versicolor")
        else:
            print("Iris_setosa")

   


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

        Iris_setosa=np.array(Iris_setosa)
        Iris_versicolor=np.array(Iris_versicolor)
    return [Iris_setosa, Iris_versicolor]

bayes()

