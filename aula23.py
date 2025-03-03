
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero #* total
        #print(numero, total)
    return total

multiplicação = multiplicar(3, 20, 3, 1, 5)
print(multiplicação)

def par_impar(numero):
    
    multiplo_de_dois = numero % 2 == 0 
    
    if multiplo_de_dois:
        return f'{numero} é par'
    
    else:
        return f'{numero} é impar'

print(par_impar(multiplicação))
    