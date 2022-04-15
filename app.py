from flask import Flask, jsonify
from flask_restful import Api
from controller.hotel import Hoteis, Hotel
from controller.usuario import User, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)

# Configuração SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Configuração da autenticação JWT
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
# Configuração do JWT Blacklist
app.config['JWT_BLACKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)

# Notação para criar o banco de dados
@app.before_first_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blocklist_loader
def verifica_blacklist(self,token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'resultado': 'Token de acesso inválido!'}), 401

# Criação de rotas para a API
api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')


if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
    