# Persistencia.py
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

