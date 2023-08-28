class Biblioteca():
    def __init__(self):
        self.temas = ["1- Suspense","2- Romance","3- Ação","4- Infantil"]
        self.situacaotemas = {"Suspense": True, "Romance": True, "Ação": True, "Infantil": True}
    
    def mostrarTemas(self):
        print("Temas: ")
        print(self.temas)

    def situacaoLivros(self):
        print("Livros Presentes: ")
        print(self.situacaotemas)


class Usuario(Biblioteca):
    def __init__(self, nome, idade):
        super().__init__()
        self.nome = nome
        self.idade = idade
        self.livrosemprestados = []

    def pegarLivro(self, num):
        if (int(num) == 1):
            if not self.situacaotemas["Suspense"]:
                print("O livro já está emprestado.")
            else:
                self.situacaotemas["Suspense"] = False
                self.livrosemprestados.append(1)
                print("O livro de Suspense foi emprestado.")
        
        if (int(num) == 2):
            if not self.situacaotemas["Romance"]:
                print("O livro já está emprestado.")
            else:
                self.situacaotemas["Romance"] = False
                self.livrosemprestados.append(2)
                print("O livro de Romance foi emprestado.")
        if (int(num) == 3):
            if not self.situacaotemas["Ação"]:
                print("O livro já está emprestado.")
            else:
                self.situacaotemas["Ação"] = False
                self.livrosemprestados.append(3)
                print("O livro de Ação foi emprestado.")
        if (int(num) == 4):
            if not self.situacaotemas["Infantil"]:
                print("O livro já está emprestado.")
            else:
                self.situacaotemas["Infantil"] = False
                self.livrosemprestados.append(4)
                print("O livro de Infantil foi emprestado.")

    def devolverLivro(self, num):
        if int(num) == 1:
            if 1 in self.livrosemprestados:
                self.situacaotemas["Suspense"] = True
                self.livrosemprestados.remove(1)
                print("O livro de Suspense foi devolvido.")
            else:
                print("Você não tem o livro de Suspense.")
        
        if (int(num) == 2):
            if 2 in self.livrosemprestados:
                self.situacaotemas["Romance"] = True
                self.livrosemprestados.remove(2)
                print("O livro de Romance foi devolvido.")
            else:
                print("Você não tem o livro de Romance.")
        if (int(num) == 3):
            if 3 in self.livrosemprestados:
                self.situacaotemas["Ação"] = True
                self.livrosemprestados.remove(3)
                print("O livro de Ação foi devolvido.")
            else:
                print("Você não tem o livro de Ação.")
        if (int(num) == 4):
            if 4 in self.livrosemprestados:
                self.situacaotemas["Infantil"] = True
                self.livrosemprestados.remove(4)
                print("O livro de Infantil foi devolvido.")
            else:
                print("Você não tem o livro de Infantil.")


