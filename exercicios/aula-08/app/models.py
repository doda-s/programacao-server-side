from app import data_base

class Client(data_base.Model): # Cria o modelo de objeto para DB
    id = data_base.Column(data_base.Integer, primary_key=True)
    name = data_base.Column(data_base.String(100))
    email = data_base.Column(data_base.String(100))

    # Transforma em dicionario
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }