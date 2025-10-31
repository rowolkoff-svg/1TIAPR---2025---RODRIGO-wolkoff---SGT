# Sistema de Gerenciamento de Tarefas

- O Sistema de Gerenciamento de Tarefas permite cadastrar, listar, atualizar e remover tarefas, salvando os dados em um arquivo JSON para persistência. O sistema é interativo via linha de comando.
- # Cadastro de tarefas (descrição, data de vencimento, status)
- Listagem de tarefas (com opção de filtrar por status)
- Atualização de tarefas
- Remoção de tarefas
- Persistência de dados em arquivo JSON
- # projeto_tarefas/
├── tarefas.py       # Funções CRUD
├── persistencia.py  # Salvar e carregar tarefas
├── interface.py     # Interface de usuário
├── main.py          # Ponto de entrada
└── README.md        # Este arquivo
# 1. Certifique-se de ter Python 3.x instalado
2. Clone o repositório:
   git clone <URL-do-repositorio>
3. Entre na pasta do projeto:
   cd projeto_tarefas
4. Execute o sistema:
   python main.py
5. Siga o menu para cadastrar, listar, atualizar ou remover tarefas.
# Persistência de Dados
- Todas as tarefas são salvas automaticamente no arquivo `tarefas.json`.
- Ao reiniciar o sistema, as tarefas previamente cadastradas são carregadas automaticamente.

  # Códigos
- tarefas.py → Funções para criar, listar, atualizar e remover tarefas
- persistencia.py → Funções para salvar e carregar tarefas
- interface.py → Menu e interação com o usuário
- main.py → Executa o sistema

 # Observações / Melhorias Futuras
- Adicionar tarefas recorrentes
- Implementar prioridades e categorias
- Criar interface gráfica
- Validar entradas do usuário (datas, status)

#  Autor / Créditos
- Desenvolvido por: [Rodrigo WOlkoff Giorgi]
- Professor: Leonardo  
- Curso: FIAP – 1TIAPR 


 




