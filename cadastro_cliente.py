import csv  # Biblioteca para trabalhar com arquivos CSV

# Função para cadastrar clientes
# Essa função solicita as informações do cliente e as salva no arquivo "clientes.csv"
def cadastrar_clientes():
    with open("clientes.csv", mode="a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        # Verifica se o arquivo está vazio para adicionar o cabeçalho
        if arquivo.tell() == 0:
            escritor.writerow(["ID", "Nome", "Email", "Telefone"])

        # Entrada de dados
        id_cliente = input("ID do cliente: ")
        nome = input("Nome do cliente: ")
        email = input("Email do cliente: ")
        telefone = input("Telefone do cliente: ")

        # Escreve os dados no arquivo
        escritor.writerow([id_cliente, nome, email, telefone])
        print(f"Cliente {nome} cadastrado com sucesso!")

# Função para listar todos os clientes cadastrados
def listar_clientes():
    try:
        with open("clientes.csv", mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            clientes = list(leitor)

            # Verifica se há clientes cadastrados
            if len(clientes) <= 1:
                print("!! Nenhum cliente cadastrado !!")
                return

            # Exibe a lista de clientes
            print("\n=== Lista de Clientes ===")
            for cliente in clientes[1:]:
                print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]} | Telefone: {cliente[3]}")
    except FileNotFoundError:
        print("⚠️ Arquivo de clientes não encontrado. Cadastre um cliente primeiro.")

# Função para buscar um cliente pelo ID ou nome
def buscar_clientes():
    termo = input("Digite o ID ou Nome do cliente: ").strip()

    try:
        with open("clientes.csv", mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            clientes = list(leitor)

            # Procura o cliente na lista
            for cliente in clientes[1:]:
                if termo.lower() in cliente[0].lower() or termo.lower() in cliente[1].lower():
                    print(f"Cliente encontrado: {cliente}")
                    return

            print("Cliente não encontrado.")
    except FileNotFoundError:
        print("⚠️ Arquivo de clientes não encontrado. Cadastre um cliente primeiro.")

# Função para editar os dados de um cliente
def editar_clientes():
    id_cliente = input("Digite o ID do cliente que deseja editar: ").strip()

    try:
        with open("clientes.csv", mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            clientes = list(leitor)

        # Procura o cliente na lista
        for cliente in clientes[1:]:
            if cliente[0] == id_cliente:
                print(f"Cliente encontrado: {cliente}")
                cliente[1] = input("Novo nome: ") or cliente[1]
                cliente[2] = input("Novo email: ") or cliente[2]
                cliente[3] = input("Novo telefone: ") or cliente[3]

                # Salva as alterações no arquivo
                with open("clientes.csv", mode="w", newline="", encoding="utf-8") as arquivo:
                    escritor = csv.writer(arquivo)
                    escritor.writerows(clientes)  # Corrigido para `.writerows()`
                print("Cliente atualizado com sucesso!")
                return

        print("Cliente não encontrado.")
    except FileNotFoundError:
        print("⚠️ Arquivo de clientes não encontrado. Cadastre um cliente primeiro.")

# Função para excluir um cliente pelo ID
def excluir_clientes():
    id_cliente = input("Digite o ID do cliente que deseja excluir: ").strip()

    try:
        with open("clientes.csv", mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            clientes = list(leitor)

        # Procura e remove o cliente da lista
        for cliente in clientes[1:]:
            if cliente[0] == id_cliente:
                clientes.remove(cliente)

                # Salva as alterações no arquivo
                with open("clientes.csv", mode="w", newline="", encoding="utf-8") as arquivo:
                    escritor = csv.writer(arquivo)
                    escritor.writerows(clientes)

                print(f"Cliente {cliente[1]} excluído com sucesso.")
                return

        print("Cliente não encontrado.")
    except FileNotFoundError:
        print("⚠️ Arquivo de clientes não encontrado. Cadastre um cliente primeiro.")

# Menu principal - onde o usuário escolhe as opções
def menu():
    while True:
        print("\n=== Sistema de Cadastro de Clientes ===")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Editar cliente")
        print("5. Excluir cliente")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        # Condições para chamar a função correspondente
        if opcao == "1":
            cadastrar_clientes()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            buscar_clientes()
        elif opcao == "4":
            editar_clientes()
        elif opcao == "5":
            excluir_clientes()
        elif opcao == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Rodar o programa
menu()