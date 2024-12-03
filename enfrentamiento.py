import random

jugador1 = input("Ingrese el nombre del jugador 1: ")
jugador2 = input("Ingrese el nombre del jugador 2: ")

input(f"{jugador1} presiona enter para lanzar el dado")

lanzamientoJugador1 = random.randint(1,6)
print(f"{jugador1} sacaste {lanzamientoJugador1}")

input(f"{jugador2} presiona enter para lanzar el dado")

lanzamientoJugador2 = random.randint(1,6)
print(f"{jugador2} sacaste {lanzamientoJugador2}")
    
if lanzamientoJugador1 > lanzamientoJugador2:
    print(f"El ganador es {jugador1}")
elif lanzamientoJugador1 < lanzamientoJugador2:
    print(f"El ganador es {jugador2}")
else:
    print(f"{jugador1} y {jugador2} empataron")