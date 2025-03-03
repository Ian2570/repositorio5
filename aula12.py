horas = input ('Qual hora é agora:')

try:

    horario = float(horas)
    if horario >= 0 and horario <= 11:
        print ('bom dia')

    elif horario >= 12 and horario <=17:
        print('boa tarde')
    
    elif horario >= 18 and horario <=23:
        print ('boa noite')


     
except:

    print('isso não é um horário')