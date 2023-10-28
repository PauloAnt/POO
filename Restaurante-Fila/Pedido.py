class Pedido():
    def __init__(self, pedido:str):
        assert type(pedido) == str, "O pedido deve ser composta por palavras."
        self.__pedido = pedido

    def __str__(self):
        return f"{self.__pedido}"

    @property
    def pedido(self)-> str:
        return self.__pedido
    
    @pedido.setter
    def pedido(self, novoPedido)->str:
        self.__pedido = novoPedido
        return self.__pedido
