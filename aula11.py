numero = input('ensira um numero nesta linha ')

try:
#if numero.isdigit() : 
    numero_digitado = int(numero)
    print(f'Esse número é par!{numero} é {numero_digitado % 2 == 0}')

#elif numero.isdigit () :
    print(f'Esse número é impar!{numero} é {numero_digitado % 3 == 0}')
           

#elif numero.isdigit() % 3 == 0:
     #print('Esse número é impar!')

except:
     print('Isso não é número inteiro!')






