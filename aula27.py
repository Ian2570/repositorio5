# Define a lista
numeros = [1, 2, 3, 4, 5]

# Define a função que filtra os números maiores que 2
def filtrar_maiores_que_dois(lista):
    return [numero for numero in lista if numero > 2]

# Chama a função e imprime o resultado
resultado = filtrar_maiores_que_dois(numeros)
print(resultado)
