# models/carro.py
class Carro:
    def __init__(self, placa: str, modelo: str):
        self.placa = placa
        self.modelo = modelo
        self.servicos = []  # Lista para armazenar serviços associados ao carro

# models/cliente.py
class Cliente:
    def __init__(self, nome: str):
        self.nome = nome

# models/servico.py
class Servico:
    def __init__(self, descricao: str, preco: float):
        self.descricao = descricao
        self.preco = preco

# Database class
from models import carro, cliente, Servico

class Database:
    tabelaCarros: list[carro.Carro] = []
    tabelaClientes: list[cliente.Cliente] = []
    tabelaServicos: list[Servico.Servico] = []

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

    def add_servico_a_carro(self, placa: str, servico: Servico.Servico) -> bool:
        carro = self.get_carro(placa)
        if carro:
            carro.servicos.append(servico)  # Associa o serviço ao carro
            return True
        return False

    def get_servicos_carro(self, placa: str) -> list[Servico.Servico]:
        carro = self.get_carro(placa)
        if carro:
            return carro.servicos  # Retorna os serviços associados ao carro
        return []

# Exemplo de uso do Database
if __name__ == "__main__":
    db = Database()

    # Adiciona alguns serviços
    servico1 = Servico(descricao="Troca de óleo", preco=150.0)
    servico2 = Servico(descricao="Alinhamento", preco=100.0)

    db.add_servico(servico1)
    db.add_servico(servico2)

    # Exibe serviços disponíveis
    print("Serviços disponíveis:")
    for servico in db.get_servicos():
        print(f"Serviço: {servico.descricao}, Preço: {servico.preco}")

    # Adiciona um carro
    novo_carro = Carro(placa="ABC1234", modelo="Fiesta")
    db.add_carro(novo_carro)

    # Associa um serviço ao carro
    db.add_servico_a_carro("ABC1234", servico1)

    # Exibe serviços associados ao carro
    print("\nServiços associados ao carro ABC1234:")
    for servico in db.get_servicos_carro("ABC1234"):
        print(f"Serviço: {servico.descricao}, Preço: {servico.preco}")
