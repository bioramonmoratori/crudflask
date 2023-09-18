# Desafio Stemis

Bem vindo ao Desafio Stemis!

Este desafio compreende uma das etapas do processo seletivo para a vaga de estagiário em backend.

O desafio consiste na criação de uma API REST usando Python Flask, com simples funções de CRUD, para alguma aplicação interessante e relevante, da sua escolha. Por exemplo, você pode criar um catálogo de produtos, um carrinho de compras, uma gestão de usuários, um sistema de avaliação de serviços (o projeto pode ser algo simples, mas quanto melhor o projeto, mais você se destaca). O importante é que a sua API seja funcional e compreenda as 4 principais operações.

Nunca se esqueça, uma boa API é uma API documentada.

Para conhecer mais sobre a Stemis acesse o nosso [site](https://www.stemis.com.br).

Para ficar informado sobre futuros processos seletivos, siga a gente no Instagram [@stemis.tec](https://www.instagram.com/stemis.tec)

# API Biblioteca de Livros

Biblioteca de Livros com possibilidade de cadastrar livros, listar autores e acompanhar o status dos livros. 
As requisições podem ser realizadas através da URL [http://146.235.38.15:5000/](http://146.235.38.15:5000/)

## [/livros](http://146.235.38.15/livros):
- ID (Integer)
- Título (String)
- Data de Publicação (Date)
- ISBN (String)
- Estoque (Enum) -> `DISPONIVEL`, `RESERVADO`, `VENDIDO`
- Lista de Autores (List) -> Relacionamento com Tabela de Autores

#### Listar Coleção de Livros `/livros` `GET`
#### Cadastrar Livro `/livros` `POST`
```
{
    "titulo": "O Pequenoo Principe",
    "isbn": "2546545634",
    "dataDePublicacao": "2023-03-03",
    "autores":[1, 2],
    "estoque": "DISPONIVEL"
}
```
`STATUS 201 - Criado`
```
{
    "livro": {
        "autores": [1, 2],
        "dataDePublicacao": "2023-03-03",
        "estoque": "DISPONIVEL",
        "id": 3,
        "isbn": "2546545634",
        "titulo": "O Pequenoo Principe"
    },
    "mensagem": "Livro criado com sucesso"
}
```
#### Obter Livro Pelo ID `/livros/{ID}` `GET`

#### Editar Livro Pelo ID `/livros/{ID}` `PUT`
```
{
    "id": 3,
    "titulo": "O Pequenoo Principe",
    "isbn": "2546545634",
    "dataDePublicacao": "2023-03-03",
    "autores":[],
    "estoque": "DISPONIVEL"
}
```
#### Deletar Livro Pelo ID `/livros/{ID}` `DELETE`

## [/autores](http://146.235.38.15/autores):
- ID (Integer)
- Nome (String)

#### Listar Autores `/autores` `GET`
#### Cadastrar Autor `/autores` `POST`
```
  "nome": "Fulano"
```
#### Obter Autor Pelo ID `/autores/{ID}` `GET`
#### Editar Autor Pelo ID `/autores/{ID}` `PUT`
#### Deletar Autor Pelo ID `/autores/{ID}` `DELETE`
