import time
import random


class Persona():
    numeroAtleta=0
    nombrePersona=''
    equipo=''
    recCorriendo=0
    recBicicleta=0
    recNadando=0



    def __init__(self, nombrePersona, equipo, numeroAtleta):
        self.nombrePersona=nombrePersona
        self.equipo=equipo
        self.numeroAtleta=numeroAtleta
        self.recCorriendo=0
        self.recBicicleta=0
        self.recNadando=0




    def correr(self):
        while self.recCorriendo <= 20000:
            kmph=random.randrange(2000)     #Se realiza un random que se le sumara a su recorrido para que el resultado varie en todos los atletas
            self.recCorriendo = self.recCorriendo + kmph
            print(str(self.nombrePersona) + " del equipo " + str(self.equipo) + " Esta Corriendo y lleva " + str(self.recCorriendo) + " metros")
            time.sleep(0.1) #Se agrego una funcion o libreria para realizar pausas en el bucle.


    def pedalear(self):
        while self.recBicicleta <= 10000:
            kmph=random.randrange(1000)
            self.recBicicleta = self.recBicicleta + kmph
            print(str(self.nombrePersona)  + " del equipo " + str(self.equipo) +  " Esta Pedaleando y lleva " + str(self.recBicicleta) + " metros")
            time.sleep(0.1)

    def nadar(self):
        while self.recNadando <= 1000:
            kmph=random.randrange(500)
            self.recNadando = self.recNadando + kmph
            print(str(self.nombrePersona)  + " del equipo " + str(self.equipo) + " Esta Nadando y lleva " + str(self.recNadando) + " metros")
            time.sleep(0.1)



