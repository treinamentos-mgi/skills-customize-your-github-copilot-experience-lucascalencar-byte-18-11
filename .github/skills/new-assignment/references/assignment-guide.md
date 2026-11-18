# Guia de Criação de Assignments

## Dificuldade e escopo

- Escolha um conceito principal ou um conjunto pequeno de conceitos relacionados ao objetivo da atividade.
- Ajuste a quantidade de tarefas e a complexidade dos requisitos ao nível informado pelo usuário. Se o nível ou o conceito estiver indefinido e isso mudar significativamente o escopo, pergunte antes de criar a atividade.
- Defina resultados observáveis e verificáveis. Evite requisitos vagos como "fazer um programa bom"; descreva o comportamento esperado.
- Mantenha os requisitos necessários para praticar o conceito central. Não acrescente recursos que aumentem o escopo sem contribuir para o objetivo.
- Use linguagem clara e direta, adequada a estudantes. Inclua exemplos de entrada e saída quando ajudarem a remover ambiguidades.

## Estrutura

- Crie a atividade como `assignments/<kebab-case-id>/README.md` e use `templates/assignment-template.md` como fonte de verdade.
- Preserve os títulos e a ordem das seções presentes no template. No template atual, os títulos são `# 📘 Atividade: [Título da Atividade]`, `## 🎯 Objetivo`, `## 📝 Tarefas`, `### 🛠️ [Título da Tarefa]`, `#### Descrição` e `#### Requisitos`.
- Escreva o objetivo em uma ou duas frases e descreva cada tarefa com uma ação concreta, seguida por requisitos específicos em lista.
- Não adicione seções que não existam no template, a menos que o usuário solicite.

## Quando incluir starter code

- Inclua starter code quando a configuração inicial, o código repetitivo ou uma API não familiar puder desviar a atenção do conceito que a atividade pretende ensinar.
- Não inclua starter code quando escrever o programa do zero for parte importante do objetivo de aprendizagem.
- Mantenha o starter code curto e funcional. Use comentários ou marcadores `TODO` para indicar os pontos que o estudante deve completar, sem entregar a solução.
- Adicione arquivos de dados somente quando forem necessários para concluir um requisito, e descreva claramente como devem ser usados.
- Salve starter code e dados na pasta da atividade. Registre cada arquivo como attachment usando `scripts/add-attachment.js`.
