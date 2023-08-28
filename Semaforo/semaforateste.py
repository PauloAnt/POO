import time

class Semaforo():
    def __init__(self):
        self.cores = {"Vermelho": True, "Amarelo": False, "Verde": False}
        self.tempo_total = 60
        self.tempo_estagio = {"Tempo_vermelho": 7, "Tempo_amarelo": 3, "Tempo_verde": 7}

    def __str__(self):
        saida = f'''
          +-----+
          | ({"X" if self.cores["Vermelho"] else " "}) |
          | ({"X" if self.cores["Amarelo"] else " "}) |
          | ({"X" if self.cores["Verde"] else " "}) |
          +-----+
        '''
        return saida
    
    def proximoEstagio(self):
        if (self.cores["Vermelho"]):
            self.cores["Vermelho"] = False
            self.cores["Verde"] = True
            return 
        elif (self.cores["Amarelo"]):
            self.cores["Amarelo"] = False
            self.cores["Vermelho"] = True
            return 
        elif (self.cores["Verde"]):
            self.cores["Verde"] = False
            self.cores["Amarelo"] = True
            return  
            
    def Temporizador(self):
            print(self.tempo_total, "segundos")
            time.sleep(1) 
            if (self.cores["Vermelho"]):
                self.tempo_total -= 7
                for i in range(self.tempo_estagio["Tempo_vermelho"], 0, -1):
                    print(i, "segundos")
                    time.sleep(1)  
            elif (self.cores["Amarelo"]):
                self.tempo_total -= 3
                for i in range(self.tempo_estagio["Tempo_amarelo"], 0, -1):
                    print(i, "segundos")
                    time.sleep(1)  
            elif (self.cores["Verde"]):
                self.tempo_total -= 7
                for i in range(self.tempo_estagio["Tempo_verde"], 0, -1):
                    print(i, "segundos")
                    time.sleep(1)