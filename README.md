# 🛳️ HUNDIR LA FLOTA

# 🎯 ¿En qué consiste?

Este es un juego por turnos en el que tú y un rival (la máquina) os enfrentáis en una batalla naval. Cada uno tiene una flota de barcos escondida en un tablero de 10x10. El objetivo es hundir todos los barcos del enemigo antes de que él hunda los tuyos.

# ⚙️ ¿Cómo funciona?

Cada jugador tiene un tablero con sus barcos y otro tablero donde marca sus disparos al enemigo.

Los barcos del rival se colocan aleatoriamente, sin solaparse ni salirse del tablero.

El jugador introduce coordenadas (fila y columna) para disparar. Si acierta, se marca con una ❌, si falla, con 💧.

El rival dispara aleatoriamente, evitando repetir casillas.

Cada vez que un disparo acierta, el juego comprueba si se ha hundido un barco completo.

El juego termina cuando una de las dos flotas ha sido completamente hundida.

# 👾 Cómo jugar

Ejecuta el archivo main.py.

Se imprimen los tableros.

Introduce las coordenadas del disparo cuando sea tu turno (por ejemplo: 3 y luego 5).

Observa los mensajes del juego para saber si acertaste o fallaste.

Gana quien hunda primero todos los barcos del oponente.

# 🧠 Lógica del código

generar_barcos_aleatorios(): coloca los barcos aleatoriamente sin solaparse.

disparar_a_lista(): gestiona el disparo del jugador y actualiza el tablero.

disparo_rival(): genera un disparo aleatorio del enemigo y actualiza el tablero.

barco_hundido() y todos_barcos_hundidos(): detectan cuándo un barco ha sido hundido.

jugar(): gestiona los turnos hasta que haya un ganador.

# 📦 Archivos principales

main.py: inicia el juego.

utils.py: contiene las funciones del juego.

variables.py: contiene variables globales (tableros, barcos...).
