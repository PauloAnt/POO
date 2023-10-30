from Restaurante import Restaurante, RestauranteException
from Pessoa import Pessoa
from Pedido import Pedido

# Paulo = Pessoa("Paulo")
# Julia = Pessoa("Julia")
# Alex = Pessoa("Alex")

r1 = Restaurante("Delizia di Pasta")
conta_cliente = 0
while True:
    try:

        print(f'''
(e) Inserir cliente na fila de atendimento.
(c) Chamar cliente em espera.
(i) Iniciar preparo da refeição.
(s) Sair com pedido para entrega.
(q) Encerrar programa.
=============================================
Fila de espera: {r1.espera}
Fila de preparo: {r1.preparo}
Fila de entrega: {r1.entregar}
''')
        resposta = input("Opção: ").lower()

        if (resposta == "e"):
            conta_cliente += 1
            print(r1.inserirCliente(conta_cliente))
        elif (resposta == "c"):
            nome = input("Informe seu nome: ")
            comida = input("Faça seu pedido: ")
            # if (type(comida) != str or (type(nome) != str)):
            #     raise RestauranteException("O nome e o pedido devem ser do tipo str!")
            # else:
            pedido = Pedido(comida)
            print(r1.realizarPedido(nome, pedido))
        elif (resposta == "i"):
            print(r1.preparoRefeicao())
        elif (resposta == "s"):
            print(r1.entregarPedido())
        elif (resposta == "q"):
            print("Encerrando programa...")
            break
    except RestauranteException as re:
        print(re)
    except AssertionError as ae:
        print(ae)
    except BaseException as be:
        print(f"Erro desconhecido! '{be}'")
    except:
        print("Erro desconhecido, iremos tratar em breve!")