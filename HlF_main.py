import numpy as np
import random
from HlF_variables import *
from HlF_utils import *
import os
from PIL import Image
import time


#TABLEROS:
    #diseñamos los 3 tableros vacíos

imprimir_tableros()

#IMPRIMIR LOS TABLEROS CON LOS BARCOS:
generar_y_colocar_barcos()
  


#Pedir al jugador que meta coordenadas de disparo:
f = int(input("Introduce la fila (número del 0 al 9): "))
c = int(input("Introduce la columna (número del 0 al 9): "))

# Llamamos a la función de disparo
disparar_a_lista(f, c, barcos_rival, tablero_jugador_check, aciertos)


#llamar a jugar
jugar()
   
#en esta version dejar barcos metidos a mano. Incluir que imprima el tablero del rival

#hacerme una guia de todas las variables y qué son/como se usan
