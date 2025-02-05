import numpy as np

#Crear una lista de números
lista = [1, 2, 3, 4, 5]

print("Comprensión de listas para generar una nueva lista con cuadrados")
cuadrados = [x**2 for x in lista]
print(cuadrados) 

 # Salida: [1, 4, 9, 16, 25]

print("----------------------------------------------")

print("Crear un array de NumPy a partir de una lista")
array = np.array([1, 2, 3, 4, 5])
print(array)  
# Salida: [1 2 3 4 5]

print("Crear una matriz 2D")
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)

# Salida:
# [[1 2 3]
#  [4 5 6]]


print("----------------------------------------------")

print("Operaciones con Arrays")

print("Sumar un escalar a todos los elementos")
array2 = array + 10
print(array2)  
# Salida: [11 12 13 14 15]

print("Multiplicación elemento a elemento")
array3 = array * 2
print(array3)  
# Salida: [ 2  4  6  8 10]

print("----------------------------------------------")

print("Indexación y Slicing en Arrays")

print("Acceder a elementos individuales")
print(array[0])  
# Salida: 1

print("Seleccionar un subconjunto (slice)")
print(array[1:4])  
# Salida: [2 3 4]

print("----------------------------------------------")

print("Transposición de matrices")
matriz_transpuesta = matriz.T
print(matriz_transpuesta)
# Salida:
# [[1 4]
#  [2 5]
#  [3 6]]

print("----------------------------------------------")

print("Multiplicación de matrices")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
producto = np.dot(A, B)
print(producto)
# Salida:
# [[19 22]
#  [43 50]]