from Persona import Persona
from timeit import default_timer #Se agrego una funcion o libreria en la que cuenta el tiempo que se lleva cada metodo
listaTiempo=[]

#EQUIPO A
oscar = Persona("Oscar", "A", 23)
jorge = Persona("Jorge", "A", 24)
maria = Persona("Maria", "A", 25)

#EQUIPO B
kevin = Persona("Kevin", "B", 77)
katy = Persona("Katy", "B", 78)
alex = Persona("Alex", "B", 79)


#POR RAZONES DE TESTEO DE LA FUNCIONALIDAD EL PROGRAMA SE DEJO SOLO A 3 ALTLETAS

def iniciar():
    inicio = default_timer() #Inicio para contar el tiempo
    jorge.correr()
    jorge.pedalear()
    jorge.nadar()
    fin = default_timer() #Fin de contar el tiempo
    listaTiempo.append([fin - inicio, "Jorge"]) #Se recolectan los datos y se agregan a una lista
    print("")

    inicio = default_timer()
    katy.correr()
    katy.pedalear()
    katy.nadar()
    fin = default_timer()
    listaTiempo.append([fin - inicio, "Katy"])
    print("")


    inicio = default_timer()
    oscar.correr()
    oscar.pedalear()
    oscar.nadar()
    fin = default_timer()
    listaTiempo.append([fin - inicio, "Oscar"])
    print("")

    print("")
    print(listaTiempo) #Imprime en pantalla los tiempos de cada uno de los atletas para verificar la veracidad de las posiciones
    print("")
    listaTiempo.sort() #Se ordenan los datos por medio del tiempo y se muestran en pantalla las posiciones
    print("TABLA DE POSICIONES")
    print("\n".join(str(i[1]) for i in listaTiempo))


import os
import sys

def clear():
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")


def menu():
    opcion = 0

    while opcion != 4:

        print("TRIATLON OPLIMPICO 2020")
        print("1. Iniciar Carrera")
        print("2. Salir")
        opcion = int(input("Digite Opcion: "))

        if opcion == 1:
            iniciar()
            os.system("PAUSE")
            clear()


        elif opcion == 2:
            print("USTED HA SALIDO DEL PROGRAMA")
            sys.exit()



menu()
