from semaforateste import Semaforo

semaforo = Semaforo()


while (semaforo.tempo_total >= 0):
    print(semaforo)
    semaforo.Temporizador()
    semaforo.proximoEstagio()  
