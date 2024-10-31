class Livraria:
    def __init__(self):
        self.a = ""

    def visualizar_livros(self):
        self.livros = {
            "Python use a cabeça": 10,
            "Introdução ao Python": 3,
            "Harry Potter e a pedra filosofal": 2,
            "Harry Potter e o Enigma do príncipe": 4,
            "Harry Potter e as relíquias da morte": 15
        }
        print("\nLivros disponíveis para empréstimo:")
        for titulo, quantidade in self.livros.items():
            print(f"{titulo}: {quantidade} disponível(s)")

    def emprestar_livro(self, titulo):
        if titulo in self.livros:
            if self.livros[titulo] > 0:
                self.livros[titulo] -= 1
                print(f"Você emprestou: {titulo}. Boa leitura!")
            else:
                print(f"Desculpe, não há cópias disponíveis de '{titulo}'.")
        else:
            print(f"Livro '{titulo}' não encontrado na livraria.")

    def devolver_livro(self, titulo):
        if titulo in self.livros:
            self.livros[titulo] += 1
            print(f"Você devolveu: {titulo}. Obrigado!")
        else:
            print(f"Livro '{titulo}' não encontrado na livraria.")

    def menu(self):
        
        escolha = input("Escolha abaixo \n1- Visualizar \n2- Emprestimo \n3- Devolução \n4- Sair ")
        match escolha:
            case "1":
                self.visualizar_livros()
            case "2":
                titulo = input("Digite o título do livro que deseja emprestar: ")
                self.emprestar_livro(titulo)
            case "3":
                titulo = input("Digite o título do livro que deseja devolver: ")
                self.devolver_livro(titulo)
            case "4":
                print("Saindo do sistema. Até logo!")
                exit()
            case _:
                print("Opção inválida.")
