def encontrar_minimo_maximo(lista):
    if not lista:
        return None, None  

    minimo = maximo = lista[0]  
    for numero in lista:
        if numero < minimo:
            minimo = numero
        if numero > maximo:
            maximo = numero

    return minimo, maximo


lista_numeros = [12, 45, 6, 78, 23, 9, 67]
minimo, maximo = encontrar_minimo_maximo(lista_numeros)

print("El número más pequeño es:", minimo)
print("El número más grande es:", maximo)