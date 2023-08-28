from pooBibliotecaLivros import Biblioteca, Usuario

library = Biblioteca()
Paulo = Usuario("Paulo", 18)
Julia = Usuario("Jula", 18)

library.mostrarTemas()
library.situacaoLivros()

Paulo.pegarLivro(1)
Julia.pegarLivro(2)

Paulo.devolverLivro(1)
Paulo.pegarLivro(2)
library.situacaoLivros()
print(Paulo.livrosemprestados)

Julia.pegarLivro(4)
Julia.devolverLivro(2)