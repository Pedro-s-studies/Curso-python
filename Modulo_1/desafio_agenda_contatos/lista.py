def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {
        "contato": nome_contato.upper(),
        "telefone": telefone_contato,
        "email": email_contato,
        "favorito": False,
    }
    contatos.append(contato)
    print(f"Contato: {nome_contato} foi adicionado com sucesso!")
    return


def ver_contatos(contatos, so_favoritos=False):
    print("\n Agenda de contatos:")
    for index, contato in enumerate(contatos, start=1):
        favorito = "⭐" if contato["favorito"] else "  "
        nome_contato = contato["contato"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]

        if so_favoritos:
            if contato["favorito"] == True:
                print(f"{index}. [{favorito}] {nome_contato} - {telefone_contato} - {email_contato}")
        else:
            print(f"{index}. [{favorito}] {nome_contato} - {telefone_contato} - {email_contato}")
    return


def atualizar_contato(contatos, index_contato, opcao, valor):
    index_ajustado = int(index_contato) - 1
    if index_ajustado >= 0 and index_ajustado < len(contatos):
        contatos[index_ajustado]["contato"] = valor.upper() if opcao == "1" else contatos[index_ajustado]["contato"]
        contatos[index_ajustado]["telefone"] = valor if opcao == "2" else contatos[index_ajustado]["telefone"]
        contatos[index_ajustado]["email"] = valor if opcao == "3" else contatos[index_ajustado]["email"]
        print(
            f"Contato {index_contato}, atualizado com sucesso!"
        )
    else:
        print(f"Índice do contato inválido!")
    return


def favoritar_contato(contatos, index_contato):
    index_ajustado = int(index_contato) - 1
    if index_ajustado >= 0 and index_ajustado < len(contatos):
        contato = contatos[index_ajustado]
        contato["favorito"] = not contato["favorito"]
        
        status = "favoritado" if contato["favorito"] else "removido dos favoritos"
        print(f"Contato {index_contato} foi {status}.")
    else:
        print(f"Índice do contato inválido!")
    return


def deletar_contato(contatos, index_contato):
    index_ajustado = int(index_contato) - 1
    if index_ajustado >= 0 and index_ajustado < len(contatos):
        del contatos[index_ajustado]
        print(f"Contato foi deletado com sucesso!")
    else:
        print(f"Índice do contato inválido!")
    return


contatos = []

while True:
    print("\n Menu da Agenda de Contatos:")
    print("1. Adicionar Contato")
    print("2. Ver Contatos")
    print("3. Ver Contatos Favoritos")
    print("4. Atualizar contato")
    print("5. Favoritar/Desfavoritar contato")
    print("6. Apagar contato")
    print("0. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar:")
        telefone_contato = input("Digite o número do contato que deseja adicionar:")
        email_contato = input("Digite o email do contato que deseja adicionar:")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        ver_contatos(contatos, True)
    elif escolha == "4":
        ver_contatos(contatos)
        index_contato = input("Qual o índice do contato que deseja atualizar?")
        
        print("\n Menu de Opções de Atualização:")
        print("1. Nome")
        print("2. Telefone")
        print("3. Email")
        opcao = input("Digite a opção que deseja atualizar")        
        valor = input("Qual o novo valor a ser editado no contato?")
        
        atualizar_contato(
            contatos, index_contato, opcao, valor
        )
        ver_contatos(contatos)
    elif escolha == "5":
        ver_contatos(contatos)
        index_contato = input("Digite o índice do contato que deseja favoritar:")
        favoritar_contato(contatos, index_contato)
    elif escolha == "6":
        index_contato = input("Digite o índice do contato que deseja apagar:")
        ver_contatos(contatos)
        deletar_contato(contatos, index_contato)
    elif escolha == "0":
        break

print("Programa finalizado")
