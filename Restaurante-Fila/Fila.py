import numpy as np

class FilaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class Fila():
    def __init__(self, size:int=10):
        self.__array = np.full(size, None)
        self.__frente = 0
        self.__fim = -1
        self.__tam = 0

    def __str__(self):
        str = 'Frente-> [ '
        frente = self.__frente
        for i in range(self.tamanho()):
            str += f'{self.__array[frente]} '
            frente = (frente + 1) % (len(self.__array))
        str += ']'
        return str

    def __len__(self):
        return abs(self.__frente - self.__fim)

    def estaVazia(self):
        if (self.__tam == 0):
            return True
        return False

    def estaCheia(self):
        if (self.__tam == len(self.__array)):
            return True
        return False

    def tamanho(self):
        return self.__tam
    
    def enfileira(self, carga):
        if (not self.estaCheia()):
            pos = self.__fim
            self.__fim = (self.__fim + 1) % len(self.__array)
            self.__array[self.__fim] = carga
            self.__tam += 1
        else:
            raise FilaException("A fila está cheia!")

    def desenfileira(self):
        if (not self.estaVazia()):
            carga = self.__array[self.__frente]
            self.__frente = (self.__frente + 1) % len(self.__array)
            self.__tam -= 1
            return carga
        else:
            raise FilaException("A fila está vázia!")

    def busca(self, carga):
        lista = list(self.__array)
        if (carga in lista):
            frente = self.__frente
            for i in range(self.tamanho()):
                if (lista[frente] == carga):
                    return i + 1
                frente = (frente + 1) % (len(self.__array))
        else:
            raise FilaException("A carga não está na fila!")
        

    def elemento(self, pos):
        if (pos >= 0 and pos <= len(self.__array)):
            return self.__array[pos - self.__frente]
        else:
            raise FilaException(f"Escolha um número de 0 a {len(self.__array) - 1}!")

    def frente(self):
        return self.__array[self.__frente]
    
    def ultimo(self):
        return self.__array[self.__fim]