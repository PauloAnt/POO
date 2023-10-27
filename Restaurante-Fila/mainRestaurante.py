from Restaurante import Restaurante, RestauranteException
from Pessoa import Pessoa

# Paulo = Pessoa("Paulo")
# Julia = Pessoa("Julia")
# Alex = Pessoa("Alex")

r1 = Restaurante("Delizia di Pasta")

while True:
    try:

        print(f'''
(e) Inserir cliente na fila de atendimento.
(c) Chamar cliente em espera.
(i) Iniciar preparo da refeição.
(s) Sair com pedido para entrega.
(q) Encerrar programa.
=============================================
''')
        resposta = input("Opção: ").lower()

        if (resposta == "e"):
            nome = input("Informe seu nome: ")
            pedido = input("Faça seu pedido: ")
            print(r1.realizarPedido(nome, pedido))
        elif (resposta == "c"):
            print(r1.chamaCliente())
        elif (resposta == "i"):
            print(r1.preparoRefeicao())
        elif (resposta == "s"):
            print(r1.entregarPedido())
        elif (resposta == "q"):
            print("Encerrando programa...")
            break
    except RestauranteException as re:
        print(re)
    except BaseException as be:
        print(f"Erro desconhecido! '{be}'")