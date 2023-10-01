from mercado import Mercado
from produto import Produto
from pessoa import Pessoa


#Criando produtos
chocolate = Produto("Chocolate", 10, 100)
cereal = Produto("Cereal", 5, 30)
refri = Produto("Refri", 5, 10)

#Criando mercado e adicionando produtos ao mercado
m1 = Mercado("Carrefour")
m1.addProduto(chocolate)
m1.addProduto(cereal)
m1.addProduto(refri)
print(m1.mostrarProdutos())

#Clientes
Paulo = Pessoa("Paulo", 300)
Julia = Pessoa("Julia", 5)

#Comprando
print(Paulo.qnt_dinheiro)
print(m1.comprarProduto(Paulo, chocolate))
print(Paulo.qnt_dinheiro)
print()
print(Julia.qnt_dinheiro)
print(m1.comprarProduto(Julia, chocolate))
print(m1.mostrarProdutos())