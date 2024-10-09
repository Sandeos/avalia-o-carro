from datetime import datetime
import re

class Carro:
    def _init_(self, nome_cliente, nome_carro, modelo_ano, placa, quilometragem, proxima_revisao, tipo_servico):
        self.nome_cliente = nome_cliente
        self.nome_carro = nome_carro
        self.modelo_ano = modelo_ano
        self.placa = placa
        self.quilometragem = quilometragem
        self.proxima_revisao = proxima_revisao
        self.tipo_servico = tipo_servico

    def mostrar_informacoes(self):
        print(f"\nNome do Cliente: {self.nome_cliente}")
        print(f"Nome do Carro: {self.nome_carro}")
        print(f"Modelo e Ano: {self.modelo_ano}")
        print(f"Placa: {self.placa}")
        print(f"Quilometragem Atual: {self.quilometragem} km")
        print(f"Próxima Revisão: {self.proxima_revisao.strftime('%d/%m/%Y')}")
        print(f"Tipo de Serviço: {self.tipo_servico}")

# Funções de validação
def validar_placa(placa):
    return bool(re.match(r'^[A-Z]{3}\d[A-Z]{4}$', placa)) or bool(re.match(r'^[A-Z]{3}\d{4}[A-Z]{1}$', placa))

def validar_proxima_revisao(proxima_revisao):
    """A data da próxima revisão deve ser posterior à data atual."""
    try:
        proxima = datetime.strptime(proxima_revisao, "%d/%m/%Y")
        hoje = datetime.now()
        return proxima > hoje  # Verifica se a data da próxima revisão é maior que a data atual
    except ValueError:
        return False

# Função para validar a quilometragem (odômetro)
def validar_quilometragem(quilometragem):
    return 1 <= quilometragem <= 999999  # Quilometragem entre 1 e 999.999

# Função para coletar dados do cliente e do carro
def coletar_dados_oficina():
    print("Bem-vindo à Oficina Brasão!")

    nome_carro = input("Digite o nome do carro: ")
    modelo_ano = input("Digite o modelo e o ano do carro (formato: Modelo/Ano): ")
    
    placa = input("Digite a placa do carro (formato: ABC1234 ou ABC1D23): ").upper()

    if validar_placa(placa):
        # Aqui, você pode verificar se a placa já está cadastrada (simulando um banco de dados)
        placa_cadastrada = False  # Mude para True se a placa já estiver cadastrada
        if placa_cadastrada:
            print("Placa já cadastrada. Prosseguindo para a próxima parte.")
        else:
            print("Você é um novo cliente. Vamos fazer seu cadastro.")
            nome_cliente = input("Digite o nome do cliente: ")
            return coletar_dados_novo_cliente(nome_cliente, nome_carro, modelo_ano, placa)
    else:
        print("Placa inválida! O cadastro não pode ser realizado.")
        print("Você é um novo cliente. Vamos fazer seu cadastro.")
        nome_cliente = input("Digite o nome do cliente: ")
        return coletar_dados_novo_cliente(nome_cliente, nome_carro, modelo_ano, placa)

def coletar_dados_novo_cliente(nome_cliente, nome_carro, modelo_ano, placa):
    while True:
        quilometragem = int(input("Digite a quilometragem atual do carro: "))
        if validar_quilometragem(quilometragem):
            break
        else:
            print("Quilometragem inválida! Digite um valor entre 1 e 999.999.")

    while True:
        proxima_revisao = input("Digite a data da próxima revisão (dd/mm/yyyy): ")
        if validar_proxima_revisao(proxima_revisao):
            break
        else:
            print("Erro: A data da próxima revisão deve ser uma data futura. Por favor, insira uma data válida.")

    print("\nTipos de serviço disponíveis:")
    print("1. Revisão geral")
    print("2. Troca de óleo")
    print("3. Troca de peças")
    print("4. Troca de pneus")
    print("5. Serviço de freios")
    print("6. Limpeza de injetores")
    print("7. Troca de bateria")

    while True:
        tipo_servico_opcao = input("Escolha o tipo de serviço (digite o número correspondente): ")
        if tipo_servico_opcao in ['1', '2', '3', '4', '5', '6', '7']:
            tipo_servico = ["Revisão geral", "Troca de óleo", "Troca de peças", "Troca de pneus", 
                            "Serviço de freios", "Limpeza de injetores", "Troca de bateria"][int(tipo_servico_opcao) - 1]
            break
        else:
            print("Opção inválida! Por favor, escolha um número válido.")

    return Carro(nome_cliente, nome_carro, modelo_ano, placa, quilometragem, datetime.strptime(proxima_revisao, "%d/%m/%Y"), tipo_servico)

# Exemplo de uso
carro = coletar_dados_oficina()
if carro:
    carro.mostrar_informacoes()