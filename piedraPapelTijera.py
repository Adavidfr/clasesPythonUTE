import random

print("Vas a jugar piedra papel o tijera contra el computador")
print("Para PIEDRA digita 1")
print("Para PAPEL digita 2")
print("Para TIJERA digita 3")

miEleccion = int(input("Escoge un valor: "))

if miEleccion == 1:
    print("ELEGISTE PIEDRA ")
elif miEleccion == 2:
    print("ELEGISTE PAPEL")
elif miEleccion == 3:
    print("ELEGISTE TIJERA")
else:
    print("DEBE ELIGIR UN NUMERO ENTRE 1 Y 3")

eleccionCompu = random.randint(1, 3)

if eleccionCompu == 1:
    print("LA COMPU ELIGIO PIEDRA ")
elif eleccionCompu == 2:
    print("LA COMPU ELIGIO PAPEL")
elif eleccionCompu == 3:
    print("LA COMPU ELIGIO TIJERA")

if miEleccion == 1 and eleccionCompu == 1:
    print("NADIE GANA")
elif miEleccion == 1 and eleccionCompu == 2:
    print("TE GANO LA COMPU XD")
elif miEleccion == 1 and eleccionCompu == 3:
    print("FELICIDADES LE GANASTE A LA COMPU")
elif miEleccion == 2 and eleccionCompu == 1:
    print("FELICIDADES LE GANASTE A LA COMPU")
elif miEleccion == 2 and eleccionCompu == 2:
    print("NADIE GANA")
elif miEleccion == 2 and eleccionCompu == 3:
    print("TE GANO LA COMPU XD")
elif miEleccion == 3 and eleccionCompu == 1:
    print("TE GANO LA COMPU XD")
elif miEleccion == 3 and eleccionCompu == 2:
    print("FELICIDADES LE GANASTE A LA COMPU")
elif miEleccion == 3 and eleccionCompu == 3:
    print("NADIE GANA")
