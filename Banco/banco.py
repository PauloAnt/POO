from abc import ABC, abstractmethod
from contaCorrente import ContaCorrente
from contaPoupança import ContaPoupança

class Banco(ABC):
    contaCorrente = ContaCorrente()
    def __init__(self, nome:str, datanasc:str, cpf:int, rg:int):
        assert len(str(cpf)) == 11, "O CPF deve possuir 11 dígitos."
        assert len(str(rg)) == 8, "O RG deve possuir 8 dígitos."
        self.__nome = nome
        self.__datanasc = datanasc
        self.__cpf = cpf
        self.__rg = rg

    def __str__(self):
        return str(self.__dict__)

    #Getters
    def getNome(self):
        return self.__nome
    def getDataNasc(self):
        return self.__datanasc
    def getCpf(self):
        return self.__cpf
    def getRg(self):
        return self.__rg
    
    def abrirContaCorrente(self):
        conta = self.contaCorrente.novaConta(self.getCpf())
        return conta
    def mostrarDados(self):
        return self.contaCorrente.mostrarDados(self.getCpf())
    def apagarConta(self):
        return self.contaCorrente.apagar(self.getCpf())
