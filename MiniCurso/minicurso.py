class MiniCurso():
    totalvagas = 0
    def __init__(self, nome:str, vagas:int=None, carga:int=None, ins:str=None):
        self.__nome = nome
        self.__vagas = vagas
        self.__carga = carga
        self.__ins = ins
        self.__aluno = []
        MiniCurso.totalvagas += vagas

    def __str__(self):
        return f"{self.__nome}/ {self.vagas} vagas/ {self.carga} horas"
    
    def addParticipante(self, nome):
        if (self.vagas > 0):
            self.__aluno.append(nome)
            return "Aluno cadastrado com sucesso!"
        return "As vagas estão esgotadas!"
    
    def vagasDisponiveis(self):
        return self.vagas - len(self.__aluno)

    @classmethod
    def totalVagasOfertadas(cls):
        return cls.totalvagas

    @property
    def vagas(self):
        return self.__vagas
    @vagas.setter
    def vagas(self, novoValor):
        self.__vagas = novoValor
        return self.__vagas
    @property
    def carga(self):
        return self.__vagas
    @carga.setter
    def carga(self, novoValor):
        self.__carga = novoValor
        return self.__carga