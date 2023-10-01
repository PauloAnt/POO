from mercado import Mercado
from produto import Produto
from pessoa import Pessoa

try:

    #Criando produtos.
    chocolate = Produto("Chocolate", 10, 0)
    cereal = Produto("Cereal", 5, 30)
    refri = Produto("Refri", 5, 10)

    #Criando mercado e adicionando produtos ao mercado.
    m1 = Mercado("Carrefour")
    m1.addProduto(chocolate)
    m1.addProduto(cereal)
    m1.addProduto(refri)
    print(m1.mostrarProdutos(a))

except AssertionError as ae:
    print(ae)
except BaseException as e:
    print(f"Error! '{e}', iremos contatar ao sistema!")



try:

    #Criando clientes.
    Paulo = Pessoa("Paulo", 10)
    Julia = Pessoa("Julia", 10)

    #Criando as interações do cliente com o mercado.
    print(Paulo.qnt_dinheiro)
    print(m1.comprarProduto(Paulo, chocolate))
    print(Paulo.qnt_dinheiro)
    print()
    print(Julia.qnt_dinheiro)
    print(m1.comprarProduto(Julia, "chocolate"))
    print(m1.mostrarProdutos())

except AssertionError as ae:
    print(ae)
except BaseException as e:
    print(f"Error! '{e}', iremos contatar ao sistema!")

