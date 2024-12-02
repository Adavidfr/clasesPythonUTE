#Paranetro Posicional
def saludar(nombre,edad):
    print(f"Hola, {nombre}. tienes {edad} años.") 

saludar("Pedro",24)

#Parametro por defecto
def descripcion(nom,ocupacion="Estudiantes"):
    print(f" {nom} es {ocupacion}")
    
descripcion("Juan")
descripcion("Peter","Ingeniero")    
    
#Parametro con palabra clave

def mostrar_info(nomb,ed,ciudad):
    print(f"Nombre: {nomb}, Edad: {ed}, Ciudad: {ciudad}")

mostrar_info(ed=29, ciudad="Quito", nomb="Marta")

#parametro con Agumento  *Args  **Kawrgs 

def sumar(*numeros):
    total=sum(numeros)
    print(f"La suma es: {total}")

def mostrar_datos(**datos):
    for clave,valor in datos.items():
       print(f"{clave}: {valor}")
    
sumar(1,2,3,4,5,6,7,8,9)
mostrar_datos(nombre="Laura", edad=15,ciudad="Quito")

# Aqui se usa el Args
def suma(*args):
    return sum(args)

print(suma(1,2,3))

#Aqui se usa el Kwargs

def mostrar_dato(**kwargs):
    for clave, Value in kwargs.items():
        print(f"{clave}, {Value}")
        
mostrar_dato(nombre="Michael", ciudad="Ibarra",edad=54,estatura=21,peso=23)
