# Primero, pedimos al usuario que cargue los numeros a ser ordenados
lista_numeros_usuario = input('Ingrese una lista de numeros separados por barra: ')

# Lo siguiente, seria convertir lo que el usuario ingreso en una lista de numeros, dividir los caracteres por barra y por ultimo convertir en numero entero
numeros = [int(num) for num in lista_numeros_usuario.split("/")]

# Despues, ordenamos la lista de forma ascendente
numeros.sort()

# Por ultimo, mostramos la lista, ya ordenada, al usuario
print("Esta es la lista ordenada de forma ascendente: ", numeros)
