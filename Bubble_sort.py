
class BubbleSort:
    def __init__(self, lista):
        n = len(lista)
        for i in range(n - 1): #El rango se emplea para definir donde empiza y acaba esa variable
                               #La i controla las veces que tengo que hacer el bucle y hasta que
                               #posicion llego comparando

            for j in range(n - 1 - i): #n - 1 - i se utiliza para que no vuelva a hacer operaciones innecesarias
                                       #En este caso - i le dice que no vuelva a la posicion que ha llegado en
                                       #el anterior bucle (podria ser prescindible, pero se emplea para no volver
                                       #a hacer una comparación que ha hecho antes, para determinar que numero es
                                       #más grande)

                if lista[j] > lista[j + 1]: #Compara un numero en la posicion j con el siguiente (j + 1)

                    aux = lista[j + 1] #Empleo aux para guardar el elemento que quiero cambiar, para que
                                       #no se pierda

                    lista[j + 1] = lista[j] #Copio el elemento grande (j) por en la posicion del
                                            #elemento pequeño (j + 1) por lo que en la posicion j
                                            #la tengo que cambiar con lo que tenia en j + 1

                    lista[j] = aux #Sustituyo en la posicion j el elemento que he guardado antes (j + 1)

        self.sorted_list = lista #Almaceno la lista ordenada en la variable sorted_list, es una variable del
                                 #objeto

