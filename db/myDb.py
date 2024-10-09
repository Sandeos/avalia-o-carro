from models import carro, cliente, Servico

class Database:
    tabelaCarros: list[carro.Carro] = []
    tabelaClientes: list[cliente.Cliente] = []
    tabelaServicos: list[Servico.Servico]= []
    

    def __init__(self):
        pass

    def add_carro(self, novoCarro: carro.Carro) -> bool:
        for c in self.tabelaCarros:
            if c.placa == novoCarro.placa:
                return False
        self.tabelaCarros.append(novoCarro)
        return True
            

    def get_carro(self, placa: str) -> carro.Carro:
        for c in self.tabelaCarros:
            if c.placa == placa:
                return c
        return None


    def add_cliente(self, novoUsuario: cliente.Cliente) -> bool:
        self.tabelaClientes.append(novoUsuario)
        return True
    

    def get_usuarios(self) -> list[cliente.Cliente]:
        return self.tabelaClientes
    
    def get_carros(self) -> list[carro.Carro]:
        return self.tabelaCarros
    
    def add_servico(self, novoServico: Servico.Servico) -> bool:
        self.tabelaServicos.append(novoServico)
        return True

    def get_servicos(self) -> list[Servico.Servico]:
        return self.tabelaServicos

    