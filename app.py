from db import myDb;
from models import cliente, carro

bancoDados = myDb.Database()

def cadastrar_revisao():
    placa:str = input("Digite a placa do carro: ")
    carroCadastrado = bancoDados.get_carro(placa)
    if carroCadastrado is None:
        print("Carro não cadastrado.")
            


def cadastar_carro():
    placa = input("Digite a placa do carro: ")

    if bancoDados.get_carro(placa) is not None:
        print("Erro: Carro já cadastrado.")
        return None
    
    modelo = input("Digite o modelo do carro: ")
    ano = input("Digite o ano do carro: ")
    quilometragem = input("Digite a quilometragem do carro: ")
    cliente = cadastrar_cliente()

    if(cliente is None): return None

    novoCarro = carro.Carro(modelo, ano, placa, quilometragem, cliente)
    if bancoDados.add_carro(novoCarro):
        print("Carro cadastrado com sucesso!")
    else:
         print("Erro: Carro já cadastrado.")



def cadastrar_cliente() -> cliente.Cliente:
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    novoCliente = cliente.Cliente(nome, telefone)
    if bancoDados.add_cliente(novoCliente):
        print("Cliente cadastrado com sucesso!")
        return novoCliente
    else:
        print("Erro: Cliente já cadastrado.")
        return None

def cadastrar_servico() -> cadastrar_revisao:
    



cadastar_carro()
cadastar_carro()
print(bancoDados.get_carros())
print(bancoDados.get_usuarios())
