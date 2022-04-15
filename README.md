# Python-Flask-MVC_REST-API
Aplicação REST API em Python utilizando framework Flask e padrão MVC.

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


## Exemplificação via POSTMAN

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
**url:** localhost:5000/login
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
url: localhost:5000/logout
Auth: <Bearer Token> Token = token_de_acesso
**Response:**
```json
{
    "resultado": "Usuário deslogado!"
}
```



### GET
![image](https://user-images.githubusercontent.com/40063504/163299830-4afdb361-662e-405d-9bec-923856578551.png)


### GET BY ID
![image](https://user-images.githubusercontent.com/40063504/163299859-23f3c1fd-1708-446d-ac65-3f1f56e955d6.png)


### POST
![image](https://user-images.githubusercontent.com/40063504/163299897-ac5055e8-3052-4e66-a8aa-5dac8c2017ed.png)


### PUT
![image](https://user-images.githubusercontent.com/40063504/163299968-d6af5830-6285-4c6d-9798-5f74dd5e5613.png)

![image](https://user-images.githubusercontent.com/40063504/163300027-bd8aac45-6351-4572-865c-f8858f4c60bf.png)


### DELETE
![image](https://user-images.githubusercontent.com/40063504/163300075-b2504a82-b801-4d14-8eca-3a4631bef911.png)


