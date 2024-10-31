class Inventario:
    def __init__(self):
        self.a = ""
    def mostrar_quantidade(self):
        self.equipamentos = {
            'Computadores': 10,
            'Teclados': 10,
            'Mouse': 10,
            'Coletores': 10,
            'Monitores': 10,
            'Balanças': 10,
            'Leitores óticos': 10
        }
        print("\nQuantidade atual de equipamentos:")
        for equipamento, quantidade in self.equipamentos.items():
            print(f"{equipamento}: {quantidade}")

    def adicionar_equipamento(self, tipo, quantidade):
        if tipo in self.equipamentos:
            self.equipamentos[tipo] += quantidade
            print(f"{quantidade} {tipo} adicionados com sucesso!")
        else:
            print("Tipo de equipamento não encontrado.")

    def remover_equipamento(self, tipo, quantidade):
        if tipo in self.equipamentos:
            if self.equipamentos[tipo] >= quantidade:
                self.equipamentos[tipo] -= quantidade
                print(f"{quantidade} {tipo} removidos com sucesso!")
            else:
                print(f"Quantidade insuficiente de {tipo} para remoção.")
        else:
            print("Tipo de equipamento não encontrado.")

    def menu(self):
        escolha = input("Escolha abaixo: \n 1- Visualizar \n2- Adicionar \n3- Remover \n4- Sair")
        match escolha:
            case'1':
                self.mostrar_quantidade()
            case '2':
                tipo = input("Digite o tipo de equipamento a adicionar: ")
                quantidade = int(input("Digite a quantidade a adicionar: "))
                self.adicionar_equipamento(tipo, quantidade)
            case '3':
                tipo = input("Digite o tipo de equipamento a remover: ")
                quantidade = int(input("Digite a quantidade a remover: "))
                self.remover_equipamento(tipo, quantidade)
            case '4':
                print("Saindo do sistema.")
                exit()
            case _:
                print("Opção inválida.")

