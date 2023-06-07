'''
contribuition_guid
'''


import os

caminho_atual = os.getcwd()
nome_do_projeto =  os.path.basename(caminho_atual).capitalize()

cg_md = f'''# Guia de Contribuição para o Projeto {nome_do_projeto}

Obrigado por seu interesse em contribuir para o Projeto {nome_do_projeto}! Este guia fornecerá informações sobre como você pode contribuir para o projeto de forma efetiva.

## Tipos de Contribuição

Existem várias maneiras de contribuir para o Projeto {nome_do_projeto}:

1. **Correções de bugs:** Se você encontrar algum bug no projeto, sinta-se à vontade para relatar o problema por meio do sistema de rastreamento de problemas (issue tracker) do projeto. Inclua detalhes sobre o bug e, se possível, forneça um exemplo reproduzível.

2. **Melhorias de recursos:** Se você tiver ideias ou sugestões para melhorar o projeto, abra um problema (issue) descrevendo sua proposta em detalhes. Isso ajudará a iniciar uma discussão sobre a nova funcionalidade e obter feedback da comunidade.

3. **Documentação:** A documentação é uma parte essencial de qualquer projeto. Se você encontrar alguma parte da documentação que possa ser melhorada ou se quiser adicionar documentação para uma funcionalidade ausente, sinta-se à vontade para enviar um pedido de pull (pull request) com as alterações.

## Processo de Contribuição

Para contribuir para o Projeto {nome_do_projeto}, siga estes passos:

1. Crie um fork do repositório do projeto em sua própria conta do GitHub.

2. Faça um clone do seu fork para o seu ambiente local.

3. Crie uma nova branch para suas alterações:

   ```bash
   git checkout -b minha-contribuicao
'''
ind = f'''# {nome_do_projeto}

Bem-vindo ao Projeto {nome_do_projeto}!

## Descrição

O Projeto {nome_do_projeto} é um projeto de exemplo criado para demonstrar as melhores práticas de desenvolvimento.

## Funcionalidades

- Funcionalidade 1: Descrição da funcionalidade 1.
- Funcionalidade 2: Descrição da funcionalidade 2.
- Funcionalidade 3: Descrição da funcionalidade 3.

## Instalação

Para utilizar o Projeto {nome_do_projeto}, siga estas etapas:

1. Clone este repositório em sua máquina local.
   ```bash
   git clone https://github.com/eusouanderson/projeto-{nome_do_projeto}.git
'''