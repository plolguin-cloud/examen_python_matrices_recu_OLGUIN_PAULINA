matriz=[]
suma=0
producto=1
print("Ingrese la cantidad de filas: ")
filas= int(input())
print("Ingrese la cantidad de columnas: ")
columnas= int(input())
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        print(f"Ingrese el valor de la posición [{i}][{j}]: ")
        valor= int(input())
        matriz[i].append(valor)
print("La matriz es: ")
print(matriz)
for i in range(filas):
    for j in range(columnas):
        suma= suma + matriz[i][j]
print("La suma de todos los elementos de la matriz es: ", suma)
for i in range(filas):
    for j in range(columnas):
        producto= producto * matriz[i][j]
print("El producto de todos los elementos de la matriz es: ", producto)