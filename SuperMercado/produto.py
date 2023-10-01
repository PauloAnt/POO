class Produto():
    def __init__(self, nome, valor, qnt):
        self.__nome = nome
        self.__valor = valor
        self.__qnt = qnt

    @property
    def nome(self):
        return self.__nome
    @property
    def valor(self):
        return self.__valor
    @property
    def qnt(self):
        return self.__qnt