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

2.Instale as dependências necessárias.
 ```bash
   pip install -r requeriments.txt

   '''
rmd = '''# Construtor

## Descrição do Projeto
O projeto "Construtor" é uma ferramenta desenvolvida para simplificar a criação de um diretório e arquivos padrões do GitHub em um projeto Python. Ao executar o Construtor, ele criará automaticamente a estrutura de diretórios e arquivos necessários, permitindo que você comece a desenvolver seu projeto de maneira rápida e organizada.

## Funcionalidades
- Criação automática de diretórios: o Construtor cria os diretórios principais, como "src" (código-fonte), "test" (testes) e "docs" (documentação), entre outros, de acordo com as melhores práticas para projetos Python.
- Geração de arquivos padrões: além dos diretórios, o Construtor também cria arquivos padrões, como "README.md" (para documentação do projeto), "requirements.txt" (para dependências do projeto) e "LICENSE" (para especificar a licença do projeto).
- Personalização: o Construtor permite que você personalize a estrutura de diretórios e os arquivos gerados, fornecendo opções de configuração durante a execução.

## Tecnologias Utilizadas
O projeto Construtor é escrito em Python e utiliza as seguintes tecnologias:
- Python: uma linguagem de programação versátil e de alto nível, amplamente utilizada para desenvolvimento de projetos.

## Como Usar
1. Faça o download do código-fonte do projeto Construtor.
2. Certifique-se de ter o Python instalado em sua máquina.
3. Execute o arquivo `construtor.py` a partir da linha de comando.
4. Se estiver usando terminal bash instale o construtor no alias.

~~~bash
    bash run_app.sh
~~~

4. Siga as instruções fornecidas pelo Construtor para personalizar a estrutura no bash .
5. Aguarde enquanto o Construtor cria a estrutura e os arquivos do projeto.
6. Pronto! Agora você pode começar a desenvolver seu projeto Python com a estrutura e arquivos padrões já criados.

## Contribuição
Contribuições para o projeto Construtor são bem-vindas. Se você encontrou algum problema ou deseja adicionar uma nova funcionalidade, sinta-se à vontade para abrir uma issue ou enviar um pull request para o repositório no GitHub.

## Licença
O projeto Construtor é licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.'''