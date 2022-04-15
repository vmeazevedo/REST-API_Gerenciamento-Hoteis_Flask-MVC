# REST-API_Gerenciamento-Hoteis_Flask-MVC
Aplicação REST API de gerenciamento de informações cadastrais de hoteis em Python utilizando Framework Flask e padrão MVC com controle de cadastro de usuário, login e logout.

![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/10.11.0) [![Twitter Follow](https://img.shields.io/twitter/follow/vmeazevedo.svg?style=social)](https://twitter.com/vmeazevedo) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Vinícius_Azevedo%20-blue)](https://www.linkedin.com/in/vin%C3%ADcius-azevedo-45180ab2/)

![Star](https://img.shields.io/github/stars/vmeazevedo/Python-Flask-MVC_REST-API?style=social)
![Fork](https://img.shields.io/github/forks/vmeazevedo/Python-Flask-MVC_REST-API?label=Fork&style=social)

## Requirements

```sh
pip install -r requirements.txt
```

## Exemplo de utilização

1. Clone o repositório para sua máquina

   ``
   git clone https://github.com/vmeazevedo/Python-Flask-MVC_REST-API
   ``
2. Execute o arquivo python ``app.py``.
3. Abra o POSTMAN e importe a collection ``REST_API.postman_collection.json``, localizada na pasta 'collection_postman'.
4. Execute a Request de Cadastro conforme documentação abaixo para criar um id de usuário.
5. Execute a Request de Login para que o token seja gerado validando assim suas requests.
6. Siga a documentação abaixo para executar as requisições e verificar onde se faz necessário o uso de seu token.
7. Após a utilização execute a Request de Logout para invalidar seu token de sessão.


## Exemplificação via POSTMAN - Usuários

### Cadastro
**url:** localhost:5000/cadastro
```json
{
    "login": "usuario",
    "senha": "senha_cadastro" 
}
```
**Response:**
```json
{
    "resultado": "Usuário criado com sucesso!"
}
```

### Login
**url:** localhost:5000/login </br>
**Body:**
```json
{
    "login": "usuario",
    "senha": "senha_cadastro" 
}
```
**Response:**
```json
{
    "token_de_acesso": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MDA0MDY4OCwianRpIjoiODV"
}
```

### Logout
**url:** localhost:5000/logout </br>
**Auth:** <Bearer Token> Token = token_de_acesso </br>
**Response:**
```json
{
    "resultado": "Usuário deslogado!"
}
```

### Get User by Id
**url:** localhost:5000/usuario/{user_id} </br>
**Response:**
```json
{
    "user_id": user_id,
    "login": "usuario"
}
```

### Delete User by iD
**url:** localhost:5000/usuario/{user_id} </br>
**Response:**
```json
{
    "resultado": "Usuário deletado!"
}
```

## Exemplificação via POSTMAN - Hoteis
### GET
**url:** localhost:5000/hoteis </br>
**Response:** </br>
```json
{
        "hoteis": [
        {
            "hotel_id": "delta",
            "nome": "Delta Hotel",
            "estrelas": 5.9,
            "diaria": 720.0,
            "cidade": "São Paulo"
        },
        {
            "hotel_id": "charlie",
            "nome": "Charlie Hotel",
            "estrelas": 5.9,
            "diaria": 720.0,
            "cidade": "São Paulo"
        }
    ]
}
```

### GET Hotel by Id
**url:** localhost:5000/hoteis/{hotel_id} </br>
**Response:** </br>
```json
{
    "hotel_id": "charlie",
    "nome": "Charlie Hotel",
    "estrelas": 5.9,
    "diaria": 720.0,
    "cidade": "São Paulo"
}
```

### POST
**url:** localhost:5000/hoteis/{hotel_id} </br>
**Auth:** <Bearer Token> Token = token_de_acesso </br>
**Body:** </br>
```json
{
    "nome": "Charlie Hotel",
    "estrelas": 5.9,
    "diaria": 720.0,
    "cidade": "São Paulo"
}
```
**Response:**
```json
{
    "hotel_id": "charlie",
    "nome": "Charlie Hotel",
    "estrelas": 5.9,
    "diaria": 720.0,
    "cidade": "São Paulo"
}
```

### PUT
**url:** localhost:5000/hoteis/{hotel_id} </br>
**Auth:** <Bearer Token> Token = token_de_acesso </br>
**Body:** </br>
```json
{
    "nome": "Charlie ALTERADO Hotel",
    "estrelas": 4.9,
    "diaria": 320.0,
    "cidade": "São Paulo"
}
```
**Response:**
```json
{
    "hotel_id": "charlie",
    "nome": "Charlie ALTERADO Hotel",
    "estrelas": 4.9,
    "diaria": 320.0,
    "cidade": "São Paulo"
}
```

### DELETE
**url:** localhost:5000/hoteis/{hotel_id} </br>
**Auth:** <Bearer Token> Token = token_de_acesso </br>
**Response:**
```json
{
    "resultado": "Hotel deletado!"
}
```
