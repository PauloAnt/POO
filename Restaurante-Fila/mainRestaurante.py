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
            r1.inserirCliente(conta_cliente)
            print(f"<< Aguarde... você está na {r1.espera.busca(conta_cliente)}a posição no atendimento. Aguarde! >>")

        elif (resposta == "c"):
            nome = input("Informe seu nome: ")
            comida = input("Faça seu pedido: ")
            print(f"Olá, {nome}")
            print(f"Informações do pedido: {comida}")
            conf = input("Confirma o pedido (S/N)? ").upper()
            if (conf == "S" or conf == "SIM" or conf == "SI" or conf == "YES"):
                pedido = Pedido(nome, comida)
                r1.realizarPedido(pedido)
                print("Pedido realizado com sucesso!!! Vamos preparar seu prato.")
                print(f"<< Seu pedido está na {r1.preparo.busca(pedido)}a posição na fila de preparo e deve estar pronto em {r1.preparo.tamanho()*20} min >>")
            else:
                print(f"Pedido não confirmado, descartando...")

        elif (resposta == "i"):
            first_pedido = r1.preparo.elemento(1)
            print(f"Pedido da vez: {first_pedido.pedido}")
            print(f"Cliente: Sr(a) {first_pedido.nome}:")
            conf = input("Pedido já está pronto para entrega (S/N)? ").upper()
            if (conf == "S"):        
                r1.preparoRefeicao()
                print(f"<< Seu pedido está na {r1.entrega.busca(1)}a posição para entrega. É rápido, temos vários entregadores>>")
                print(f"<< Total de Pedidos pendente: {r1.entrega.tamanho()} >>")
            else:
                print(f"Pedido não confirmado, descartando...")
        elif (resposta == "s"):
            print(f"Pedido do(a) Sr(a) {r1.entrega.busca(1)} saindo para entrega!!!")
            r1.entregarPedido()
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