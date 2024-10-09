from .cliente import Cliente

class Carro:
    def __init__(self, modelo, ano, placa, quilometragem, cliente: Cliente):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.cliente = cliente
        self.quilometragem = quilometragem