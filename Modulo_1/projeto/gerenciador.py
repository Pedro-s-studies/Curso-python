def adicionar_tarefa(tarefas, nome_tarefa):
    # Estrutura
    # tarefa: nome da tarefa
    # completada: indicar se essa tarefa já foi completada ou não
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("\n Lista de tarefas:")
    for index, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa["completada"] else "   "
        nome_tarefa = tarefa["tarefa"]
        
        print(f"{index}. [{status}] {nome_tarefa}")
    return
        
def atualizar_nome_tarefa(tarefas, index_tarefa, novo_nome_tarefa):
    index_ajustado = int(index_tarefa) - 1
    if (index_ajustado >= 0 and index_ajustado < len(tarefas)):
        tarefas[index_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {index_tarefa}, atualizada para {novo_nome_tarefa}")
    else:
        print(f"Índice de tarefa inválido!")
    return

def completar_tarefa(tarefas, index_tarefa):
    index_ajustado = int(index_tarefa) - 1
    if (index_ajustado >= 0 and index_ajustado < len(tarefas)):
        tarefas[index_ajustado]["completada"] = True
        print(f"Tarefa {index_tarefa} marcada como completada")
    else:
        print(f"Índice de tarefa inválido!")
    return
    
def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        # if tarefa["completada"] == True:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print(f"Tarefas completadas foram deletadas.")
    return
    
tarefas = []

while True:
    print("\n Menu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar:")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)           
        index_tarefa = input("Qual o índice da tarefa que deseja atualizar?")
        novo_nome_tarefa = input("Qual o novo nome da tarefa?")
        atualizar_nome_tarefa(tarefas, index_tarefa, novo_nome_tarefa)
    elif escolha == "4":
        ver_tarefas(tarefas)
        index_tarefa = input("Digite o número da tarefa que deseja completar:")
        completar_tarefa(tarefas, index_tarefa)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == "6":
        break

print("Programa finalizado")