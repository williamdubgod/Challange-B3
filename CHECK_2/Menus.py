resp = 1

menu = {}

while resp != 0:

    print("1 - LOGIN")
    print("2 - CADASTRE-SE")
    print("3 - NEWS")
    print("4 - SIMULADOR")
    print("\n")
    opc = int(input("Digite a opção desejada: "))

    if opc == 1:
        login = input("Digite o email: ")
        senha_log = input("Digite a senha: ")
        if login == email and senha_log == senha:
            print("Seja Bem-Vindo(a)")
        else:
            print("Email ou senha invalidos, tente novamente!")

    elif opc == 2:
        nome = input("Nome: ")
        celular = input("celular: ")
        email = input("Email: ")
        senha = input("senha: ")
        confirmacao_senha = input("confirmar senha: ")
        print("\n")
        if confirmacao_senha == senha:
            senha = confirmacao_senha
            print("Cadastro concluido !")
        else:
            print("Senha diferentes, tente novamnte!")
        menu[nome] = {"Nome":nome, "Email":email, "Celular":celular, "senha":senha}

    elif opc == 3:
        news_opc = int(input("Gostaria de recber novidades ? 1-SIM/2-NÂO :"))
        if news_opc != 2:
            email_news = input("Digite o email em que gostaria de receber as novidades: ")
            print("\n")
            print("email cadastrado com suecesso! ")
        else:
            print("caso mude de ideia so voltar a esse menu!")

    elif opc == 4:
        print("Efetue o login ou cadaste-se para ter acesso ao simulador")
        print("\n")
        log_simu = int(input("Digite a opção desejada 1-login/2-cadastre-se: "))


        if log_simu == 1:
            login = input("Digite o email: ")
            senha_log = input("Digite a senha: ")
            if login == email and senha_log == senha:
                print("Seja Bem-Vindo(a) ao simulador de invenstimentos!")
            else:
                print("Email ou senha invalidos, tente novamente!")
        elif log_simu == 2:
            nome = input("Nome: ")
            celular = input("celular: ")
            email = input("Email: ")
            senha = input("senha: ")
            confirmacao_senha = input("confirmar senha: ")
            print("\n")
            if confirmacao_senha == senha:
                senha = confirmacao_senha
                print("Cadastro concluido !")
                print("Seja Bem-Vindo(a) ao simulador de invenstimentos!")
            else:
                print("Senha diferentes, tente novamnte!")
            menu[nome] = {"Nome": nome, "Email": email, "Celular": celular, "senha": senha}
    print("\n")
    resp = int(input("Gostaria de continuar no menu ? 1-SIM/0-NÂO: "))
