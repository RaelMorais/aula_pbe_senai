class Estacionamento:
    def __init__(self):
        self.a=""

    def estacionar(self, tipo_veiculo):
        self.vagas_carros = 30
        self.vagas_motos = 15
        self.preco = 12.00
        self.faturamento = 0.00   
          
        if tipo_veiculo.lower() == 'carro':
            if self.vagas_carros > 0:
                self.vagas_carros -= 1
                self.faturamento += self.preco
                print("Carro estacionado com sucesso!")
            else:
                print("Não há vagas disponíveis para carros.")
        elif tipo_veiculo.lower() == 'moto':
            if self.vagas_motos > 0:
                self.vagas_motos -= 1
                self.faturamento += self.preco
                print("Moto estacionada com sucesso!")
            else:
                print("Não há vagas disponíveis para motos.")
        else:
            print("Tipo de veículo inválido. Por favor, escolha 'carro' ou 'moto'.")

    def sair(self, tipo_veiculo):
        if tipo_veiculo.lower() == 'carro':
            if self.vagas_carros < 30:
                self.vagas_carros += 1
                print("Carro saiu do estacionamento.")
            else:
                print("Não há carros estacionados.")
        elif tipo_veiculo.lower() == 'moto':
            if self.vagas_motos < 15:
                self.vagas_motos += 1
                print("Moto saiu do estacionamento.")
            else:
                print("Não há motos estacionadas.")
        else:
            print("Tipo de veículo inválido. Por favor, escolha 'carro' ou 'moto'.")

    def visualizar_faturamento(self):
        print(f"Total do faturamento até o momento: R$ {self.faturamento:.2f}")

    def menu(self):
        escolha = input("Escolha abaixo: \n1- Estacionar \n2- Sair \n3- Visualizar \n 4- Quit")
        
        match escolha:
            case '1':
                tipo_veiculo = input("Digite o tipo de veículo (carro/moto): ")
                self.estacionar(tipo_veiculo)
            case '2':
                tipo_veiculo = input("Digite o tipo de veículo que está saindo (carro/moto): ")
                self.sair(tipo_veiculo)
            case '3':
                self.visualizar_faturamento()
            case '4':
                print("Saindo do sistema.")
                exit()
            case _:
                print("Opção inválida.")
