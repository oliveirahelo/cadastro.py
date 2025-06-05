def cadastrar_nome(cadastro):
    novo_nome = input("Digite o nome da pessoa: ")
    cadastro.append(novo_nome)
    print(f"Usuario {novo_nome} foi adicionado! ")

def listar_pessoa(cadastro):
    print("\nLista de nomes cadastrados:")   
    for i, nome in enumerate(cadastro, start=1):
        print(f"{i}. {nome}")

def excluir_pessoa(cadastro):
    excluir_nome = input("Digite o nome para excluir: ")
    if excluir_nome in cadastro:
        cadastro.remove(excluir_nome)
        print(f"{excluir_nome} foi removido. ")
    else:
        print("nome nao encontrado. ")  


def menu():
    cadastro = []
    while True:
        print("\n----- Cadastro de funcionarios----------")
        print("[1] Cadastrar Pessoa")
        print("[2] Listar Pessoa")
        print("[3] Excluir Pessoa")
        print("[0]")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_nome(cadastro)
        elif opcao == '2':
            listar_pessoa(cadastro)
        elif opcao == '3':
            excluir_pessoa(cadastro)
        elif opcao == '0':          
            print("saindo...")   
            break 
        else:
            print("!!! Opção invalida. Tente novamente. !!!")

menu()            