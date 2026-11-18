# 📘 Atividade: Persistindo Dados com SQLite

## 🎯 Objetivo

Crie um gerenciador de tarefas no terminal usando Python e `sqlite3`, a biblioteca de banco de dados incluída na biblioteca padrão. Pratique operações CRUD e mantenha os dados salvos entre diferentes execuções do programa.

## 📝 Tarefas

### 🛠️ Criar e consultar tarefas

#### Descrição

Implemente a criação do banco de dados e das funções para cadastrar e listar tarefas. Cada tarefa deve ter um identificador, um título e um estado de conclusão.

#### Requisitos
O programa concluído deve:

- Criar ou abrir um arquivo de banco de dados chamado `tarefas.db` usando `sqlite3`.
- Criar uma tabela `tarefas` com `id` inteiro como chave primária, `titulo` obrigatório e `concluida` com valor inicial falso.
- Cadastrar tarefas e listar todas as tarefas com seus dados.
- Usar parâmetros SQL nas consultas que recebem valores do usuário.

### 🛠️ Atualizar e remover tarefas

#### Descrição

Adicione opções a um menu no terminal para marcar uma tarefa como concluída ou removê-la pelo identificador.

#### Requisitos
O programa concluído deve:

- Permitir marcar como concluída uma tarefa existente.
- Permitir remover uma tarefa existente.
- Informar quando o identificador informado não corresponde a nenhuma tarefa.
- Manter as tarefas após encerrar e iniciar o programa novamente.
- Fechar corretamente as conexões com o banco de dados.
