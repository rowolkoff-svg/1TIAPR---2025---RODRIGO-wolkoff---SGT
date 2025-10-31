# Codigos
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



