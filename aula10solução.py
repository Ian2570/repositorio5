nome = input('qual o seu nome ')
idade = input ('qual a sua idade ')

if nome and idade:
    print(f'o seu nome é {nome}')
    print(f'a sua idade é {idade}')

if ' ' in nome:
    print(f'Seu nome tem espaço')
else:
    print(f'Seu nome não tem espaço')
    
print(f'O seu nome tem {len (nome)}')
print(f'Seu nome invertido é {nome[::-1]}')