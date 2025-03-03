nome = input('Ensira um nome?')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print ('seu nome é muito curto')
    
    elif tamanho_nome >=5 and tamanho_nome <=6:
        print ('seu nome é médio')

    else:
        print('seu nome é muito grande')

else:
    print('digite mais de uma letra')
