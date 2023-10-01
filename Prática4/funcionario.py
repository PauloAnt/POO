from enum import Enum
from abc import ABC, abstractmethod

class Grau(Enum):
    Medio = 1 
    Superior = 2 
    Especialista = 3 
    Mestre = 4
    Doutor = 5

class Funcionario(ABC):
    def __init__(self, nome:str, salario:float, grau:Grau):
        self.__nome = nome
        assert salario >= 0
        self.__salario = salario
        self.__grau = grau

    def __str__(self):
        return f"Objeto do tipo {__name__}: {self.nome}; Salário: {self.salario}"

    @abstractmethod
    def contraCheque(self):
        return f"Salário: {self.salario}\nBonificação: Não possue"
    @abstractmethod
    def addBonificação(self):
        pass

    @property
    def nome(self) -> str:
        return self.__nome
    @property
    def salario(self) -> float:
        return self.__salario
    @property
    def grau(self) -> Grau:
        return self.__grau

class Diretor(Funcionario):
    def __init__(self, nome, salario, grau):
        super().__init__(nome, salario, grau)

    def __str__(self):
        return f"Objeto do tipo {__class__.__name__}: {self.nome}; Salário: {self.salario}"
    
    def contraCheque(self):
        return f"Salário: {self.salario}\nBonificação: {self.addBonificação()}"

    def addBonificação(self) -> float:
        bonificacao = self.salario * 0.3
        if (self.grau == Grau.Especialista):
            bonificacao *= 0.15
        elif (self.grau == Grau.Mestre):
            bonificacao *= 0.25
        elif (self.grau == Grau.Doutor):
            bonificacao *= 0.5
        return bonificacao
    
class Presidente(Funcionario):
    def __init__(self, nome, salario, grau):
        super().__init__(nome, salario, grau)

    def __str__(self):
        return f"Objeto do tipo {__class__.__name__}: {self.nome}; Salário: {self.salario}"
    
    def contraCheque(self):
        return f"Salário: {self.salario}\nBonificação: {self.addBonificação()}"

    def addBonificação(self):
        bonificacao = self.salario * 3
        if (self.grau == Grau.Doutor):
            bonificacao += self.salario * 5
        return bonificacao
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, grau):
        super().__init__(nome, salario, grau)

    def __str__(self):
        return f"Objeto do tipo {__class__.__name__}: {self.nome}; Salário: {self.salario}"

    def contraCheque(self):
        return f"Salário: {self.salario}\nBonificação: {self.addBonificação()}"

    def addBonificação(self):
        bonificacao = self.salario
        if (self.grau == Grau.Especialista):
            bonificacao *= 0.15
        elif (self.grau == Grau.Mestre):
            bonificacao *= 0.25
        elif (self.grau == Grau.Doutor):
            bonificacao *= 0.5
        return bonificacao