from SemaforoTemporizado import Semaforo, Estagio


sem1 = Semaforo()
sem1.setup(5,2,5)
sem1.timer.setTime(60)
print('Semaforo 1')

while(sem1.acabar == False):
    print(sem1)
    print(sem1.exibirTempo())
    sem1.proximoEstagio()
