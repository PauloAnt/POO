class Pessoa():
    def __init__(self, nome:str, qnt_dinheiro:float):
        self.__nome = nome
        self.__qnt_dinheiro = qnt_dinheiro

    @property
    def nome(self):
        return self.__nome
    @property
    def qnt_dinheiro(self):
        return self.__qnt_dinheiro
    @qnt_dinheiro.setter
    def qnt_dinheiro(self, novovalor):
        self.__qnt_dinheiro = novovalor