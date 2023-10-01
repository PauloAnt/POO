import random
import sqlite3

sql = sqlite3.connect("contas_banco.sql")
tab = sql.cursor()
tab.execute('''
    CREATE TABLE IF NOT EXISTS conta(
                cpf INTEGER PRIMARY KEY,
                num_conta INTEGER,
                num_cartao INTEGER,
                num_agencia INTEGER
    )
    ''')
sql.commit()

class ContaCorrente():
    def __init__(self):
        self.__num_cartao = self._CriarNumeroCartao()
        self.__num_conta = self._CriarNumeroConta()
        self.__num_agencia = 1234
        self.__saldo = 0

    def __str__(self):
        return str(self.__dict__)

    #Getters
    def getSaldo(self):
        return self.__saldo
    def getNumCartao(self):
        return self.__num_cartao
    def getNumConta(self):
        return self.__num_conta
    def getNumAgencia(self):
        return self.__num_agencia

    def _CriarNumeroConta(self):
        num = f"{random.randint(0, 9999999):07}"
        return int(num)

    def _CriarNumeroCartao(self):
        num = ''
        for i in range(4):
            num += f"{random.randint(0, 9999):04}"
            if (i != 3):
                num += " "
        return num
    
    #Ações
    def depositar(self, valor:int):
        self.__saldo += valor
        return f"Depositado: {valor}, agora você tem {self.getSaldo()}"
        
    def retirar(self, quantia:int):
        if (quantia > self.getSaldo()):
            return f"Quantia insuficiente, você possui {self.getSaldo()}"
        else:
            self.__saldo -= quantia
            return f"Retirada feito com sucesso, você possui {self.getSaldo()}"
        
    #Criação
    def novaConta(self, CPF):
        tab.execute("SELECT COUNT(*) FROM conta WHERE cpf = ?", (CPF,))
        registros = tab.fetchone()[0]
        print(registros)
        if registros == 0:
            tab.execute("INSERT INTO conta (CPF, num_conta, num_cartao, num_agencia) VALUES (?, ?, ?, ?)", (CPF, self.getNumConta(), self.getNumCartao(), self.getNumAgencia()))
            sql.commit()
            return f"Registro inserido com sucesso!"
        else:
            return f"Já existe uma conta com esse CPF."

    
    def apagar(self, CPF):
        tab.execute("DELETE FROM conta WHERE cpf = {CPF}")
        sql.commit()

    def mostrarDados(self, CPF):
        tab.execute(f"SELECT * FROM conta WHERE cpf = {CPF}")
        mostrar = tab.fetchone()
        return f"CPF: {mostrar[0]}; Conta: {mostrar[1]}; Cartão: {mostrar[2]}; Agência: {mostrar[3]}"
    
    def gerarCartão(self):
        cartao = f'''
        | Banco                    |
        | {self.getNumCartao()}   | ||
        | {self.getNumConta()}                  |
        | {self.getNumAgencia()}                     |
                '''
        return cartao
