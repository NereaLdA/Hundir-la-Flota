import numpy as np
import os
from PIL import Image

#TABLEROS:
    #creamos matriz de 10x10 "vacía"
tablero_jugador = np.full((10,10), "_")

tablero_jugador_check = np.full((10,10), "_")

tablero_rival = np.full((10,10), "_")

#LISTA BARCOS JUGADOR:
    #todos los barcos, en la demo, udaremos 2
barco_J1 = [[0,3],[0,4],[0,5],[0,6]]
barco_J2 = [[2,2],[3,2],[4,2]]
barco_J3 = [[3,4],[4,4],[5,4]]
barco_J4 = [[7,0],[7,1]]
barco_J5 = [[8,7],[8,8]]
barco_J6 = [[9,4],[9,5]]

#LISTA BARCOS JUGADOR RESUMIDA:
    #los barcos que vamos a usar en lista resumida
barcos_jugador = [barco_J1, barco_J2, barco_J3, barco_J4, barco_J5, barco_J6]


#BARCOS RIVAL:   
    #Barcos generados aleatoriamente por el rival (lista):
barcos_rival = tamanos = [[2, 2]]  #2 barcos de 2 de eslora

#Lista vacía para ir rellenado con los valores acertados hasta igualarla a la original
aciertos = []

#
aciertos_rival = []
disparos_rival_realizados = []