class Livro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.emprestado = False  # já prepara p/ emprestar

    def __repr__(self):
        return f'Livro("{self.titulo}", "{self.autor}", "{self.genero}")'

    def gettitulo(self):
        return self.__titulo
    #-------------------------
    def getautor(self):
        return self.__autor
    #-------------------------
    def getgenero(self):
        return self.__genero
    #------------------------
    def settitulo(self,titulo):
        self.__titulo =titulo
        return self.__titulo
    #------------------------
    def setautor(self,autor):
        self.__autor = autor
        return self.__autor
    #-----------------------
    def setgenero(self,genero):
        self.__genero=genero
        return self.__genero