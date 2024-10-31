import desafio1
import desafio2
import desafio3

print(">>>>Atividade Senai PBE<<<<<<<")
escolher = input("\nEscolha abaixo: \n1- Desafio 1 (Suporte) \n2- Desafio 2 (Estacionamento) \n3- Desafio 3 (Livraria)\n4- Sair  \n")

match escolher:
    case "1":
        print("Desafio 1>>>>>>>>")
        desafio1.Inventario().menu()
    case "2":
        print("Desafio 2>>>>>>>>")
        desafio2.Estacionamento().menu()
    case "3":
        print("Desafio 3>>>>>>>>")
        desafio3.Livraria().menu()
    case "4":
        print("Até logo! Voce escolheu sair.")
        exit()
    case _:
        print("Tente novamente.")