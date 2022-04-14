from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}
    
class Hotel(Resource): 
    # Criando meus argumentos
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="O campo nome é obrigatório!") 
    argumentos.add_argument('estrelas', type=float, required=True, help="O campo estrelas é obrigatório!") 
    argumentos.add_argument('diaria') 
    argumentos.add_argument('cidade') 

    def get(self,hotel_id):
        # Procurando o hotel no array de hoteis.
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json(), 200
        return {'resultado': "Hotel não encontrado!"}, 404
        

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'resultado': "Hotel já existe!"}, 400

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'resultado': "Erro ao salvar hotel!"}, 500
        return hotel.json(), 201
        
        
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()  
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            try:
                hotel_encontrado.save_hotel()
            except:
                return {'resultado': "Erro ao atualizar hotel!"}, 500
            return hotel_encontrado.json(), 200
        
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'resultado': "Erro ao salvar hotel!"}, 500
        return hotel.json(), 201
       
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'resultado': "Erro ao deletar hotel!"}, 500
            return {'resultado': "Hotel deletado!"}, 200
        return {'resultado': "Hotel não encontrado!"}, 404

