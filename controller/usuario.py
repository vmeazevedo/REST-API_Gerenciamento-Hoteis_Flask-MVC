from models.usuario import UserModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST


atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="O campo 'login' não pode ser deixado em branco.")
atributos.add_argument('senha', type=str, required=True, help="O campo 'senha' não pode ser deixado em branco.")

class User(Resource): 
    # Método GET BY ID
    def get(self,user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json(), 200
        return {'resultado': "Usuário não encontrado!"}, 404
    
    # Método DELETE
    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'resultado': "Erro ao deletar usuário!"}, 500
            return {'resultado': "Usuário deletado!"}, 200
        return {'resultado': "Usuário não encontrado!"}, 404

class UserRegister(Resource):
    # /cadastro
    def post(self):
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {'resultado': "Usuário já existe!"}, 400
        
        user = UserModel(**dados)
        try:
            user.save_user()
        except:
            return {'resultado': "Erro ao cadastrar usuário!"}, 500
        return {"resultado": "Usuário criado com sucesso!"}, 201

class UserLogin(Resource):
    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        
        user = UserModel.find_by_login(dados['login'])
        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'token_de_acesso': token_de_acesso}, 200
        return {'resultado': "Usuário ou senha inválidos!"}, 401


class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {'resultado': "Usuário deslogado!"}, 200