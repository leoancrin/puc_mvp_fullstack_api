# puc_mvp_fullstack_api
Repositório das APIs para o MVP desenvolvido na disciplina Desenvolvimento FullStack da Pós da PUC-Rio

## Descrição

Este repositório tem por função apresentar o código desenvolvido para uma API simples de itens colecionáveis. O objetivo é permitir ao usuário ter uma base de dados sobre os itens colecionáveis que ele possui.

### Funções da API

A API permite realizar operações CRUD tanto para os **tipos de itens** como para os próprios **itens colecionáveis**. Um tipo de item é uma classificação genérica, como livro, filme, dvd, selos etc. Já um item é por exemplo o livro Moby Dick, o filme Matrix.

Para os tipos:
* Cadastrar um tipo de item
* Consultar os tipos de itens existentes
* Alterar um tipo de item
* Deletar um tipo de item

Para os itens:
* Cadastrar um item
* Consultar os itens existentes
* Consultar os itens de um tipo específico
* Alterar um item
* Deletar um item

### Uso da API
Ela roda em ambiente local. O primeiro passo é instalar o python, podendo ser feito conforme o link abaixo para o seu ambiente (Windows, Lunix ou macOS)
> https://www.python.org/downloads/

Após basta definir seu ambiente virtual, usando as instruções desse link, na parte **Virtual environments**
> https://flask.palletsprojects.com/en/stable/installation/

Após criado seu ambiente virtual basta rodar
> pip install -r requirements.txt

Por último, basta executar o comando na pasta onde foi incluído o app.py
> flask run

Maiores dúvidas sobre o flask basta seguir esse link
> https://flask.palletsprojects.com/en/stable/quickstart/

### Regras

1. Um tipo de item somente pode ser deletado se não houver **nenhum** item cadastrado para aquele tipo. Nesse caso primeiro delete os itens vinculados e depois realize a deleção do tipo específico.
2. Outras regras e respostas podem ser consultadas pelo link, após executar a API
> http://localhost:5000/openapi/swagger

### Banco de dados
Caso o banco já esteja populado, basta deletar o arquivo `instance/database.sqlite3` que o mesmo será reconstruído na execução da API.
