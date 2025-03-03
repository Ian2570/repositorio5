
lista_compras = []

def adicionar_item():
    item = input("Digite o item que deseja adicionar: ")
    lista_compras.append(item)
    print(f"'{item}' foi adicionado à lista!")

def apagar_item():
    if not lista_compras:
        print("A lista está vazia. Nada para apagar.")
        return
    listar_itens()
    try:
        indice = int(input("Digite o número do item que deseja apagar: ")) - 1
        if 0 <= indice < len(lista_compras):
            item_removido = lista_compras.pop(indice)
            print(f"'{item_removido}' foi removido da lista!")
        else:
            print("Número inválido. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")

def listar_itens():
    if not lista_compras:
        print("A lista está vazia.")
    else:
        print("\nItens na lista:")
        for i, item in enumerate(lista_compras, start=1):
            print(f"{i}. {item}")
        print()

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar item")
        print("2. Apagar item")
        print("3. Listar itens")
        print("4. Sair")
        opcao = input("Selecione uma opção: ")
        
        if opcao == "1":
            adicionar_item()
        elif opcao == "2":
            apagar_item()
        elif opcao == "3":
            listar_itens()
        elif opcao == "4":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Selecione uma opção válida.")

# Inicializa o programa
menu()

