
usuarios = []

while True:
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("3 - Editar")
    print("4 - Excluir")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        usuarios.append(nome)
        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        print("\nLista de usuários:")
        for i, usuario in enumerate(usuarios):
            print(f"{i} - {usuario}")

    elif opcao == "3":
        indice = int(input("Digite o índice do usuário que deseja editar: "))
        novo_nome = input("Digite o novo nome: ")
        usuarios[indice] = novo_nome
        print("Usuário atualizado com sucesso!")

    elif opcao == "4":
        indice = int(input("Digite o índice do usuário que deseja excluir: "))
        usuarios.pop(indice)
        print("Usuário excluído com sucesso!")

    elif opcao == "5":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida!")