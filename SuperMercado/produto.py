class Produto():
    def __init__(self, nome:str, valor:float, qnt:int):
        assert valor > 0 or qnt > 0, "O valor e a quantidade devem ser maior que 0."
        assert type(valor) != float or type(qnt) != int, "O valor deve ser um float (1.00) e a quantidade um int (1)."
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