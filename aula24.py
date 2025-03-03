def multiplicar(multiplo):
    def multi(numero):
        return numero * multiplo
    return multi

multiplicar_2 = multiplicar(2)
multiplicar_3 = multiplicar(3)
multiplicar_4 = multiplicar(4)

print(multiplicar_2(2))
print(multiplicar_3(2))
print(multiplicar_4(2))
