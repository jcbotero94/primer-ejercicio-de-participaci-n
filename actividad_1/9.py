def generar_numeros_pares(inicio, fin):
    numeros_pares = []
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:  # Si el número es divisible por 2, es par
            numeros_pares.append(numero)
    return numeros_pares

# Generar lista de números pares entre 1 y 100
numeros_pares = generar_numeros_pares(1, 100)

print("Lista de números pares entre 1 y 100:")
print(numeros_pares)