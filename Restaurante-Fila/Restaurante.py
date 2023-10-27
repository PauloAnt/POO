from Fila import Fila, FilaException

class RestauranteException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class Restaurante():
    def __init__(self, nome:str, loc:str=any):
        self.__nome = nome
        self.__loc = loc
        self.__espera = Fila(10)
        self.__preparo = Fila(10)
        self.__entrega = Fila(10)

    def __str__(self):
        return f"Nome: {self.__nome}, Localização: {self.__loc}"

    def realizarPedido(self, nome:str, pedido:str):
        if (type(pedido) == str and type(nome) == str):
            self.__espera.enfileira((nome, pedido))
            return f"<< Aguarde... você está na {self.__espera.busca((nome, pedido))}a posição no atendimento. Aguarde! >>"
        else:
            raise RestauranteException("Faça a seguinte estrutura: nome:str, pedido:str")
        
    def chamaCliente(self):
        if (self.__espera.estaVazia() or self.__espera.estaCheia()):
            raise RestauranteException("A fila deve está vázia ou cheia!")
        else:
            cliente = self.__espera.desenfileira()
            print(f"Olá, {cliente[0]}")
            print(f"Informações do pedido: {cliente[1]}")
            conf = input("Confirma o pedido (S/N)? ").upper()
            if (conf == "S"):
                self.__preparo.enfileira(cliente)
                print("Pedido realizado com sucesso!!! Vamos preparar seu prato.")
                return f"<< Seu pedido está na {self.__preparo.busca(cliente)}a posição na fila de preparo e deve estar pronto em {self.__preparo.tamanho()*20} min >>"
            else:
                return f"Pedido não confirmado, descartando..."
        
    def preparoRefeicao(self):
        if (self.__preparo.estaVazia() or self.__preparo.estaCheia()):
            raise RestauranteException("A fila de espera está vázia ou cheia!")
        else:
            pedido = self.__preparo.desenfileira()
            print(f"Pedido da vez: {pedido[1]}")
            print(f"Cliente: Sr(a) {pedido[0]}:")
            conf = input("Pedido já está pronto para entrega (S/N)? ").upper()
            if (conf == "S"):        
                self.__entrega.enfileira(pedido)
                print(f"<< Seu pedido está na {self.__entrega.busca(pedido)}a posição para entrega. É rápido, temos vários entregadores>>")
                return f"<< Total de Pedidos pendente: {self.__entrega.tamanho()} >>"
            else:
                return f"Pedido não confirmado, descartando..."

        
    def entregarPedido(self):
        if (self.__entrega.estaVazia() or self.__entrega.estaCheia()):
            raise RestauranteException("A fila de entrega está vázia ou cheia!")
        else:
            entrega = self.__entrega.desenfileira()
            print(f"Pedido do(a) Sr(a) {entrega[0]} saindo para entrega!!!")
            return f"{entrega[1]}"