from flask import Flask
from flask_restful import Api
from controller.hotel import Hoteis, Hotel

app = Flask(__name__)

# Configuração do SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

# Notação para criar o banco de dados
@app.before_first_request
def cria_banco():
    banco.create_all()

# Criação de rotas para a API
api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
    