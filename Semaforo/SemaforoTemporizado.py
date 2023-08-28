from enum import Enum # importação obrigatória para criar a enumeração
from Temporizador import Temporizador
import time

class Estagio(Enum):
    Verde = 1
    Amarelo = 2
    Vermelho = 3

class Semaforo:
    def __init__(self, estado_inicial:Estagio = Estagio.Vermelho): # construtor
        self.estadoAtual = estado_inicial
        self.timer = Temporizador()
        self.acabar = False
        self.tempo_transicao = {Estagio.Vermelho:10, \
                                Estagio.Amarelo: 2, \
                                Estagio.Verde: 10}

    def __str__(self):
        saida = f'''
          +-----+
          | ({"X" if self.estadoAtual == Estagio.Vermelho else " "}) |
          | ({"X" if self.estadoAtual == Estagio.Amarelo else " "}) |
          | ({"X" if self.estadoAtual == Estagio.Verde else " "}) |
          +-----+
        '''
        return saida
    
    def exibirTempo(self):
        tempo_de_transicao = self.tempo_transicao[self.estadoAtual]
        for i, j in zip(range(self.timer.tempo, 0, -1), range(tempo_de_transicao, 0, -1)):
            print(j, "segundos")
            if j == 1:
                print(i, "segundos")
            time.sleep(1)
            if i == 1:
                self.acabar = True

        
    def setup(self, tempo_verde:int, tempo_amarelo:int, tempo_vermelho:int):
        '''
        Método que permite atribuir o tempo em segundos desejado
        para os estágios do semáforo.

        Argumentos
        --------------------
        tempo_verde (int): tempo de permanência no estágio "verde"
        tempo_amarelo (int): tempo de permanência no estágio "amarelo"
        tempo_vermelho (int): tempo de permanência no estágio "vermelho"
        '''
        self.tempo_transicao[Estagio.Vermelho] = tempo_vermelho
        self.tempo_transicao[Estagio.Amarelo] = tempo_amarelo
        self.tempo_transicao[Estagio.Verde] = tempo_verde

    def proximoEstagio(self):
        '''
        Realiza a transição do estágio atual para o próximo estágio
        da cadeia
        '''
        if (self.estadoAtual == Estagio.Vermelho):
            self.estadoAtual = Estagio.Verde
            return 
        elif (self.estadoAtual == Estagio.Amarelo):
            self.estadoAtual = Estagio.Vermelho
            return 
        elif (self.estadoAtual == Estagio.Verde):
            self.estadoAtual = Estagio.Amarelo
            return 
        
'''
    def start(self, estado_inicial:int):   
        Inicia a simulacao do funcionamento do semáforo
        pass
'''

        







