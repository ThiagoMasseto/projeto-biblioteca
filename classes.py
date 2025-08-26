class Livro:
    def __init__(self, titulo, autor, genero):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__emprestado = False  # já prepara p/ emprestar

    def __repr__(self):
        return f'Livro("{self.titulo}", "{self.autor}", "{self.genero}")'

    def getTitulo(self):
        return self.__titulo
    #-------------------------
    def getAutor(self):
        return self.__autor
    #-------------------------
    def getGenero(self):
        return self.__genero
    #-------------------------
    def getEmprestado(self):
        return self.emprestado
    #------------------------
    def setTitulo(self,titulo):
        self.__titulo =titulo
        return self.__titulo
    #------------------------
    def setAutor(self,autor):
        self.__autor = autor
        return self.__autor
    #-----------------------
    def setGenero(self,genero):
        self.__genero=genero
        return self.__genero