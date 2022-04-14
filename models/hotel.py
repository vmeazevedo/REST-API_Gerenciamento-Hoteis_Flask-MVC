from sql_alchemy import banco

class HotelModel(banco.Model):
    # Nome da tabela
    __tablename__ = 'hoteis'

    # Cria as colunas da tabela
    hotel_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(40))

    # Função inicial 
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    # Função de retorno json
    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }
    
    @classmethod
    # Função para buscar no banco via query de select by id
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        if hotel:
            return hotel
        return None

    # Função para salvar no banco	
    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()
    
    # Função para atualizar no banco
    def update_hotel(self, nome, estrelas, diaria, cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
    
    # Função para deletar do banco
    def delete_hotel(self):
        banco.session.delete(self)
        banco.session.commit()
