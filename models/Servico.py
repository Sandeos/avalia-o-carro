from .carro import Carro

class Servico:
    def __init__(self, carro:Carro, tipoServico, data):
        self.carro = carro
        self.tipoServico = tipoServico
        self.data = data