#Codigos
tarefas.py
def criar_tarefa(tarefas, descricao, vencimento, status="pendente"):
    tarefa = {"descricao": descricao, "vencimento": vencimento, "status": status}
    tarefas.append(tarefa)
    return tarefas

def listar_tarefas(tarefas, status=None):
    if status:
        return [t for t in tarefas if t["status"] == status]
    return tarefas

def atualizar_tarefa(tarefas, index, descricao=None, vencimento=None, status=None):
    if descricao:
        tarefas[index]["descricao"] = descricao
    if vencimento:
        tarefas[index]["vencimento"] = vencimento
    if status:
        tarefas[index]["status"] = status
    return tarefas

def remover_tarefa(tarefas, index):
    tarefas.pop(index)
    return tarefas

#persistencia.py
import json

def salvar_tarefas(tarefas, arquivo="tarefas.json"):
    with open(arquivo, "w") as f:
        json.dump(tarefas, f, indent=4)

def carregar_tarefas(arquivo="tarefas.json"):
    try:
        with open(arquivo, "r") as f:
            tarefas = json.load(f)
    except FileNotFoundError:
        tarefas = []
    return tarefas

#interface.py
from tarefas import criar_tarefa, listar_tarefas, atualizar_tarefa, remover_tarefa
from persistencia import salvar_tarefas, carregar_tarefas

def menu():
    print("\n=== Sistema de Gerenciamento de Tarefas ===")
    print("1. Cadastrar tarefa")
    print("2. Listar tarefas")
    print("3. Atualizar tarefa")
    print("4. Remover tarefa")
    print("5. Sair")
    return input("Escolha uma opção: ")

def executar():
    tarefas = carregar_tarefas()
    
    while True:
        opcao = menu()
        
        if opcao == "1":
            desc = input("Descrição: ")
            venc = input("Data de vencimento (YYYY-MM-DD): ")
            tarefas = criar_tarefa(tarefas, desc, venc)
            salvar_tarefas(tarefas)
        
        elif opcao == "2":
            for i, t in enumerate(tarefas):
                print(f"{i}: {t['descricao']} | {t['vencimento']} | {t['status']}")
        
        elif opcao == "3":
            idx = int(input("Índice da tarefa: "))
            desc = input("Nova descrição (ou enter para manter): ")
            venc = input("Nova data de vencimento (ou enter para manter): ")
            status = input("Novo status (pendente, em andamento, concluída ou enter para manter): ")
            tarefas = atualizar_tarefa(tarefas, idx, descricao=desc or None, vencimento=venc or None, status=status or None)
            salvar_tarefas(tarefas)
        
        elif opcao == "4":
            idx = int(input("Índice da tarefa a remover: "))
            tarefas = remover_tarefa(tarefas, idx)
            salvar_tarefas(tarefas)
        
        elif opcao == "5":
            break
        
        else:
            print("Opção inválida. Tente novamente.")
