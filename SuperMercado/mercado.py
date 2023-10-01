from produto import Produto
from pessoa import Pessoa

class Mercado():
    estoque = {}
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    @classmethod
    def addProduto(cls, produto: Produto):
        chave = produto.nome
        if chave not in cls.estoque:
            cls.estoque[chave] = {
                "Valor": produto.valor,
                "Quantidade": produto.qnt
            }
        return cls.estoque[chave]
    
    @classmethod
    def comprarProduto(cls, pessoa: Pessoa, produto:Produto):
        nome = produto.nome
        if cls.estoque[nome]["Valor"] > 0 and pessoa.qnt_dinheiro > cls.estoque[nome]["Valor"]:
            cls.estoque[nome]["Quantidade"] -= 1 
            pessoa.qnt_dinheiro -= produto.valor
            return cls.estoque[nome]
        elif pessoa.qnt_dinheiro < cls.estoque[nome]["Valor"]:
            return f"Saldo insuficiente."
        else:
            return f"O produto não está mais disponível."
        
    def mostrarProdutos(self):
        return Mercado.estoque


