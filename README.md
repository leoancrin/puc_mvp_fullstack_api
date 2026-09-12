# puc_mvp_fullstack_api
Repositório das APIs para o MVP desenvolvido na disciplina Desenvolvimento FullStack da Pós da PUC-Rio

## Descrição

Este repositório tem por função apresentar o código desenvolvido para uma API simples de itens colecionáveis. O objetivo é permitir ao usuário ter uma base de dados sobre os itens colecionáveis que ele possui.

### Funções da API

A API permite realizar operações CRUD tanto para os **tipos de itens** como para os próprios **itens colecionáveis**.

Para os tipos:
* Cadastrar um tipo de item
* Consultar os tipos de itens existentes
* Alterar um tipo de item
* Deletar um tipo de item

Para os itens:
* Cadastrar um item
* Consultar os itens existentes
* consultar os itens de um tipo específico
* Alterar um item
* Deletar um item

#### Regras

1. Um tipo de item somente pode ser deletado se não houverem **nenhum** item cadastrado para aquele tipo

### Uso da API
Ela roda em ambiente local. O primeiro passo é instalar o python, podendo ser feito conforme o link abaixo para o seu ambiente (Windows, Lunix ou macOS)
> https://www.python.org/downloads/

Após basta definir seu ambiente virtual, usando as instruções desse link, na parte **Virtual environments**
> https://flask.palletsprojects.com/en/stable/installation/

Após criado seu ambiente virtual basta rodar
> pip install -r requirements.txt

Por último, basta executar o comando na pasta onde foi incluído o diretório
> flask run

Maiores dúvidas sobre o flask basta seguir esse link
> https://flask.palletsprojects.com/en/stable/quickstart/
