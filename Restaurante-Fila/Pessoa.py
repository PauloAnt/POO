class Pessoa():
    def __init__(self, nome:str, idade:int=-1):
        self.__nome = nome
        self.__idade = idade
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade