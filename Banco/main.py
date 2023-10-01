from banco import Banco

try:
    paulo = Banco("Paulo", "22/03/2005", 12345678910, 12345678)
    
except:
    print("A estrutura deve seguir o seguinte padrão, Exemplo: Fulano, 10/01/2000, 12345678910 (11 números), 12345678 (8 números)")

print(paulo)
print(paulo.abrirContaCorrente())
print(paulo.mostrarDados())
print(paulo.contaCorrente.depositar(1000))
print(paulo.contaCorrente.retirar(500))
#print(paulo.contaCorrente.gerarCartão())