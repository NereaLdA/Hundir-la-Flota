import numpy as np
import random
from HlF_variables import *
import os
from PIL import Image
import time



    
#TABLEROS:
    # diseñamos e imprimimos los 3 tableros vacíos
def imprimir_tableros(): 
    global tablero_jugador
    global tablero_jugador_check
    global tablero_rival
    
    print("TABLERO JUGADOR")
    print(tablero_jugador)

    print("TABLERO JUGADOR CHECK")
    print(tablero_jugador_check)

    print("TABLERO RIVAL")
    print(tablero_rival)



#COLOCAR BARCOS:
    #función para colocar los barcos del jugador y el rival
def colocar_barco(barco, tablero):
    for i in barco:
        for j in i:
            tablero[j[0], j[1]] = "⛴️"
    return tablero



#GENERACIÓN BARCOS RIVAL:
    #de manera aleatoria, sin que se salgan ni se pisen. Con esloras definidas("tamanos").
    #recibe una lista de tamaños de barcos y devuelve una lista de barcos colocados
def generar_barcos_aleatorios(tamanos_barcos):
    barcos = [] #ir guardando los barcos generados
    posiciones_ocupadas = [] #guardar las coordenadas ya ocupadas

    for tam in tamanos_barcos: #recorremos el tamaño (casillas) del barco
        colocado = False

        while not colocado:
            orientacion = random.choice(['H', 'V']) #elige entre h y v
            posiciones = [] #posiciones guarda las coordenadas del barco que estamos intentando colocar.
                            #Si es válido (no choca), se guarda en la lista de barcos.
                            #Luego posiciones se vacía y se vuelve a usar para el siguiente barco

            if orientacion == 'H':
                fila = random.randint(0, 9)
                col = random.randint(0, 10 - tam)
                    #Horizontal: elegimos una fila entre 0 y 9, y una columna que deje sitio 
                    #para el barco.
                    #Ejemplo: si tam = 4, y el tablero tiene 10 columnas, col puede ir de 0 a 6
                    #(porque 6 + 3 = 9 → cabe).
                for i in range(tam):
                    posiciones.append([fila, col + i]) #Vamos sumando columnas para crear el barco.
            else: #Al revés que lo que acabamos de hacer
                fila = random.randint(0, 10 - tam)
                col = random.randint(0, 9)
                for i in range(tam):
                    posiciones.append([fila + i, col])

            # Verificamos si las posiciones están libres
            libre = True
            for pos in posiciones: #Recorremos cada casilla del barco nuevo.
                if pos in posiciones_ocupadas:
                    libre = False #Si alguna ya está ocupada, libre = False y no colocamos el barco aún.
                    break

            # Si están libres, añadimos el barco y marcamos sus posiciones
            if libre:
                barcos.append(posiciones)
                for pos in posiciones:
                    posiciones_ocupadas.append(pos)
                colocado = True

    return barcos #devuelve la lista de barcos


#VER LOS BARCOS DEL RIVAL PARA LA DEMO:
def generar_y_colocar_barcos():
    #COLOCAR BARCOS JUGADOR:
    global tablero_jugador #global es para llamar a las variables que están definidas fuera de las funciones
    tablero_jugador = np.full((10,10), "_")
    tablero_jugador = colocar_barco(barcos_jugador,tablero_jugador)
    
    #IMPRIMIR TABLERO JUGADOR CON BARCOS:
    print("TABLERO JUGADOR CON BARCOS")
    print(tablero_jugador)



    global tablero_rival, barcos_rival
    tablero_rival = np.full((10,10), "_")
    tamanos = [2, 2, 2, 3, 3, 4]
    barcos_rival = generar_barcos_aleatorios(tamanos)
    tablero_rival = colocar_barco(barcos_rival, tablero_rival)

    


#MOSTRAR IMAGEN:    
    #contestar hundimiento con imagen:
def mostrar_imagen(nombre_archivo):
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(ruta_script, 'img', nombre_archivo)

    if os.path.exists(ruta_completa):
        img = Image.open(ruta_completa)
        img.show()
    else:
        print(f"Imagen no encontrada en: {ruta_completa}")


#DISPARO JUGADOR: 

def imprimir_tablero(tablero, nombre="Tablero"):
    print(f"\n{nombre}")
    for fila in tablero:
        print(fila)

def barco_hundido(barco, aciertos): 
    return all(pos in aciertos for pos in barco)

def disparar_a_lista(f, c, barcos_rival, tablero_jugador_check, aciertos):
    
    if 0 <= f < 10 and 0 <= c < 10:
        disparo = [f, c] #coordenadas disparo
        
        for i, barco in enumerate(barcos_rival): #recorremos todos los barcos
            if disparo in barco: #comprobamos si le ha dado (coincide con la lista barco
                if disparo not in aciertos: 
                    aciertos.append(disparo) #si no estaba ya, lo añadimos
                    tablero_jugador_check[f][c] = '💥'
                    print("💥💥 ¡Tocado! 💥💥")

                    if barco_hundido(barco, aciertos): #llama a función
                        print(f"🚢🚢 ¡Barco hundido! 🚢🚢")
                        mostrar_imagen('portaaviones.png')  # Ruta de la imagen
                else:
                    print("Ya habías acertado aquí.")
                break
        else:
            if tablero_jugador_check[f][c] == '_': #comprobar que no habíamos disparado ya
                print("💧💧 Agua... 💧💧")
                tablero_jugador_check[f][c] = '💧'
            else:
                print("Ya habías disparado aquí.")
    else:
        print("❌ Coordenadas fuera del tablero.")
    imprimir_tablero(tablero_jugador_check, "Disparos realizados")



#DISPARO RIVAL:
def disparo_rival(barcos_jugador, tablero_jugador, aciertos_rival):
    global disparos_rival_realizados #guarda todos los disparos que ha hecho el rival, para no repetir.
    while True:
        f = random.randint(0, 9)
        c = random.randint(0, 9)
        disparo = [f, c]

        # Evitar repetir disparos
        if disparo not in disparos_rival_realizados:
            disparos_rival_realizados.append(disparo)
            break

    print(f"\n🤖🤖 El rival dispara a ({f}, {c})... 🤖🤖")
    time.sleep(3)  

    for i, barco in enumerate(barcos_jugador):
        if disparo in barco: #revisar cada barco del jugador
            if disparo not in aciertos_rival: #comprueba si la coordenada del disparo está en ese barco
                aciertos_rival.append(disparo)
                tablero_jugador[f][c] = '💥'
                print("💥 ¡El rival ha tocado tu barco!")

                if barco_hundido(barco, aciertos_rival): #comprueba si todas las casillas del barco han sido tocadas.
                    print(f"⚓⚓ ¡El rival ha hundido tu barco! ⚓⚓")

            else:
                print("El rival ya había acertado aquí.")
            break
    else: #entra si el rival no acierta
        print("💧💧 El rival ha fallado. 💧💧")
        if tablero_jugador[f][c] == "_":
            tablero_jugador[f][c] = "💧"

    imprimir_tablero(tablero_jugador, "Tu tablero (después del disparo del rival)")



#FIN DEL JUEGO:
def todos_barcos_hundidos(barcos, aciertos):
    return all(barco_hundido(barco, aciertos) for barco in barcos) #all devuelve True si todos son True



#TURNOS:
    #lógica del juego
def jugar():
    global barcos_rival
    global tablero_jugador_check
    global aciertos
    global barcos_jugador
    global tablero_jugador
    global aciertos_rival
   
    while True:
        # TURNO JUGADOR
        try:
            f = int(input("\n🎯 Tu turno - Introduce la fila (0-9): "))
            c = int(input("🎯 Introduce la columna (0-9): "))
            disparar_a_lista(f, c, barcos_rival, tablero_jugador_check, aciertos) #,odifica el tablero check

            if todos_barcos_hundidos(barcos_rival, aciertos):
                print("\n🎉🎉🎉 ¡Has ganado! Todos los barcos del rival han sido hundidos.🎉🎉🎉")
                break
        except ValueError:
            print("❌ Formato inválido.")
            continue

        # TURNO RIVAL
        disparo_rival(barcos_jugador, tablero_jugador, aciertos_rival) #a dónde dispara
        if todos_barcos_hundidos(barcos_jugador, aciertos_rival):
            print("\n💀💀💀 Has perdido. El rival ha hundido todos tus barcos. 💀💀💀")
            break

