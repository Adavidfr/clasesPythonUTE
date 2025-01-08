def sumar_matrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    resultado = [[0 for _ in range(columnas)] for _ in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = A[i][j] + B[i][j]
    
    return resultado


def restar_matrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    resultado = [[0 for _ in range(columnas)] for _ in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = A[i][j] - B[i][j]
    
    return resultado


def multiplicar_matrices(A, B):
    filas_A = len(A)
    columnas_A = len(A[0])
    columnas_B = len(B[0])
    resultado = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]
    
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                resultado[i][j] += A[i][k] * B[k][j]
    
    return resultado


def transponer_matriz(A):
    filas = len(A)
    columnas = len(A[0])
    resultado = [[0 for _ in range(filas)] for _ in range(columnas)]
    
    for i in range(filas):
        for j in range(columnas):
            resultado[j][i] = A[i][j]
    
    return resultado


# # Ejemplo de uso
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]

# Matrices 3x3 de ejemplo
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Suma de matrices:")
print(sumar_matrices(A, B))

print("Resta de matrices:")
print(restar_matrices(A, B))

print("Multiplicación de matrices:")
print(multiplicar_matrices(A, B))

print("Transposición de A:")
print(transponer_matriz(A))