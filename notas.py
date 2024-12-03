notaExamen = int(input("Ingrese su nota de examen: "))

if notaExamen <= 10 and notaExamen >= 0:
    print("Es una nota válida")
    inasistencias = int(input("Ingrese cuantas veces a faltado a clases: "))
    if inasistencias < 3 and notaExamen >= 8:
        print("APROBADO")
    else:
        print("REPROBADO")

else:
    print("Solo se permiten notas entre 1 y 10") 

print("FIN DEL PROGRAMA")

