from funcionario import *

try:
    func1 = Diretor("Paulo", 2000, Grau.Superior)
    func2 = Gerente("Julia", 1000, Grau.Doutor)
    func3 = Presidente("Elizabeth", 10000, Grau.Doutor)
except AssertionError:
    print("ERROR! -> O salário não pode ser negativo")
    print("Encerrando...")

dados = [(func1.__class__.__name__, func1.nome , func1.salario),
         (func2.__class__.__name__, func2.nome , func2.salario), 
         (func3.__class__.__name__, func3.nome , func3.salario)]

largura = 10
cabecalho = "{:<{}} {:<{}} {:<{}} {:<{}}".format("Objeto |", largura, "Funcionário |", largura, "Grau de Instrução |", largura, "Salário Base |", largura)
print(cabecalho)
print("=" * ((largura * 6) - 1))
for linha in dados:
    print(f"{linha[0]:<{largura}} {linha[1]:<{largura}} {linha[2]:<{largura}}")