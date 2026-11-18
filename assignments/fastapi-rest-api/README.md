# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando FastAPI, praticando métodos HTTP, validação de dados com Pydantic e códigos de status. Os dados ficarão em memória e serão reiniciados quando o servidor parar.

## 📝 Tarefas

### 🛠️ Implementar operações CRUD para tarefas

#### Descrição

Complete o arquivo `starter-code.py` para criar uma API que permita listar, consultar, cadastrar, atualizar e remover tarefas. Instale FastAPI e Uvicorn com `python -m pip install fastapi uvicorn`, copie o starter code para `main.py` e inicie o servidor com `uvicorn main:app --reload`.

#### Requisitos
O programa concluído deve:

- `GET /tasks` retornar todas as tarefas, inicialmente uma lista vazia.
- `GET /tasks/{task_id}` retornar a tarefa com esse ID ou responder com status `404` se ela não existir.
- `POST /tasks` aceitar um título e um campo `completed` opcional, criar um ID único e responder com status `201`.
- `PUT /tasks/{task_id}` atualizar o título e o estado de conclusão ou responder com status `404` se a tarefa não existir.
- `DELETE /tasks/{task_id}` remover a tarefa e responder com status `204`, ou `404` se ela não existir.

Exemplo de corpo para criar uma tarefa:

```json
{
  "title": "Revisar FastAPI",
  "completed": false
}
```

### 🛠️ Validar e testar a API

#### Descrição

Use os modelos do Pydantic e a documentação interativa do FastAPI para verificar como a API valida os dados e responde às requisições.

#### Requisitos
O programa concluído deve:

- Rejeitar títulos vazios usando validação do Pydantic.
- Responder com status `422` quando o corpo de uma requisição tiver dados inválidos.
- Disponibilizar a documentação interativa em `/docs` e permitir testar nela cada endpoint implementado.
