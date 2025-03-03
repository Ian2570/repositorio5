#while True:

numero_1 = input('digite um número?')
numero_2 = input('digite um número?')
operador = input('digite um operador +-/*')
numero_adcionado = None
operadores_permitidos = "+-/*"
try:
    numero_1_flot = float(numero_1)
    numero_2_flot = float(numero_2)

except:

    numero_adcionado = None

if numero_adcionado is None:

    print=('Este erro não deveria acontecer')
    continue

    operadores_permitidos = "+-/*"

if operador not in operadores_permitidos:
    print=('operador inválido')
    continue

if len(operador) > 1:
    print('digite apenas um operador')
    continue

if operador == '+':
        print=(numero_1_flot + numero_2_flot)

if operador == '-':
        print=(numero_1_flot - numero_2_flot)


if operador == '/':
        print=(numero_1_flot / numero_2_flot)

    
if operador == '*':
        print=(numero_1_flot * numero_2_flot)




sair=input('Quer sair? [s]im: ').lower().startswith('s')

    #if sair is True:
        #break