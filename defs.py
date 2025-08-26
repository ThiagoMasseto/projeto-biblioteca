import os
import time
from classes import Livro
dicionario={
    1 : Livro ( titulo = "Duna", autor = "Frank Herbert", genero = "Ficção Cientifica"),
    2 : Livro ( titulo = "Neuromancer", autor = "William Gibson", genero = "Ficção Cientifica"),
    3 : Livro ( titulo = "Fundação", autor = "Isaac Asimov", genero = "Ficção Cientifica"),
    4 : Livro ( titulo = "Snow Crash", autor = "Neal Stephenson", genero = "Ficção Cientifica"),
    5 : Livro ( titulo = "Admiravel Mundo Novo", autor = "Aldous Huxley", genero = "Ficção Cientifica"),
    6 : Livro ( titulo = "A máquina do tempo", autor = "H. G. Wells", genero = "Ficção Cientifica"),
    7 : Livro ( titulo = "O Senhor dos Anéis: A Sociedade do Anel", autor = "J. R. R. Tolkien", genero = "Fantasia"),
    8 : Livro ( titulo = "As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-Roupa", autor = "C. S. Lewis", genero = "Fantasia"),
    9 : Livro ( titulo = "A Canção de Gelo e Fogo: A Guerra dos Tronos", autor = "George R. R. Martin", genero = "Fantasia"),
    10 : Livro ( titulo = "Mistborn: O Império Final", autor = "Brandon Sanderson", genero = "Fantasia"),
    11 : Livro ( titulo = "O Nome do Vento", autor = "Patrick Rothfuss",genero = "Fantasia"),
    12 : Livro ( titulo = "Harry Potter e a Pedra Filosofal", autor = "J. K. Rowling", genero = "Fantasia"),
    13 : Livro ( titulo = "A Roda do Tempo: O Olho do Mundo", autor = "Robert Jordan", genero = "Fantasia"),
    14 : Livro ( titulo = "Orgulho e Preconceito", autor = "Jane Austen", genero = "Romance"),
    15 : Livro ( titulo = "Anna Kariênina", autor = "Liev Tolstói", genero = "Romance"),
    16 : Livro ( titulo = "Dom Casmurro", autor = "Machado de Assis", genero = "Romance"),
    17 : Livro ( titulo = "O Morro dos Ventos Uivantes", autor = "Emily Brontë", genero = "Romance"),
    18 : Livro ( titulo = "Cem Anos de Solidão", autor = "Gabriel García Márquez", genero = "Romance"),
    19 : Livro ( titulo = "E o Vento Levou", autor = "Margaret Mitchell", genero = "Romance"),
    20 : Livro ( titulo = "O Silêncio dos Inocentes", autor = "Thomas Harris", genero = "Suspense"),
    21 : Livro ( titulo = "Assassinato no Expresso do Oriente", autor = "Agatha Christie", genero = "Suspense"),
    22 : Livro ( titulo = "O Colecionador de Ossos", autor = "Jeffery Deaver", genero = "Suspense"),
    23 : Livro ( titulo = "Garota Exemplar", autor = "Gillian Flynn", genero = "Suspense"),
    24 : Livro ( titulo = "O Iluminado", autor = "Stephen King", genero = "Suspense"),
    25 : Livro ( titulo = "Dragão Vermelho", autor = "Thomas Harris", genero = "Suspense"),
}
#-------------------------------------------------
def adicionar_livro():
    print("Para adicionar um livro, preencha as seguintes informações:")
    titulo=input("Nome do livro -->").capitalize()
    autor=input("Autor -->").capitalize()
    genero=input("Genero -->").capitalize()
    novo_id = max(dicionario.keys()) + 1
    novo_livro=Livro(titulo, autor, genero)
    dicionario[novo_id]= novo_livro
    print(f"Novo livro adicionado com sucesso! Está localizado na Id {novo_id}")
    time.sleep(2)
    os.system("cls")
#-------------------------------------------------
def remover_livro():
    print("Remover livro")
    remover_id=int(input("Digite o id:"))
    del dicionario[remover_id]
    os.system("cls")
    print(f"Livro {remover_id} removido com sucesso! ")
    os.system("pause")
#-------------------------------------------------
def emprestar_livro():
    id_livro = int(input("Digite o ID do livro que deseja emprestar: "))
    
    if id_livro in dicionario:
        livro = dicionario[id_livro]
        if not livro.emprestado:  # verifica se já não está emprestado
            livro.emprestado = True
            print(f'Livro "{livro.getTitulo()}" emprestado com sucesso!')
        else:
            print(f'O livro "{livro.getTitulo()}" já está emprestado.')
    else:
        print("ID não encontrado!")

    os.system("pause")
    os.system("cls")

#-------------------------------------------------
def devolver_livro():
    id_livro = int(input("Digite o ID do livro que deseja devolver: "))
    
    if id_livro in dicionario:
        livro = dicionario[id_livro]
        if livro.getEmprestado():
            livro.setEmprestado(False)
            print(f'Livro "{livro.getTitulo()}" devolvido com sucesso!')
        else:
            print(f'O livro "{livro.getTitulo()}" não estava emprestado.')
    else:
        print("ID não encontrado!")

    os.system("pause")
    os.system("cls")

#-------------------------------------------------
def listar_autor():
    autor_busca = input("Digite o nome do autor que deseja buscar: ").strip()

    encontrados = False
    for id_livro, livro in dicionario.items():
        # Compara ignorando maiúsculas/minúsculas
        if livro.getAutor().lower() == autor_busca.lower():
            print(f"ID: {id_livro} | Título: {livro.getTitulo()} | Gênero: {livro.getGenero()}")
            encontrados = True

    if not encontrados:
        print(f"Não foram encontrados livros do autor {autor_busca}.")

    os.system("pause")
    os.system("cls")

#-------------------------------------------------
def listar_genero():
    while True:
        escolha_genero = int(input(
            "Selecione o gênero que você deseja listar os livros:\n"
            "0 --> Sair\n"
            "1 --> Ficção Científica\n"
            "2 --> Fantasia\n"
            "3 --> Romance\n"
            "4 --> Suspense\n--> "
        ))

        if escolha_genero == 0:
            break

        # Mapeando a escolha para o nome do gênero
        mapa_genero = {
            1: "Ficção Cientifica",
            2: "Fantasia",
            3: "Romance",
            4: "Suspense"
        }

        genero_selecionado = mapa_genero.get(escolha_genero)
        if not genero_selecionado:
            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE")
            os.system("pause")
            os.system("cls")
            continue

        # Listando livros do gênero escolhido
        encontrados = False
        for id_livro, livro in dicionario.items():
            if livro.getGenero() == genero_selecionado:
                print(f"ID: {id_livro} | Título: {livro.getTitulo()} | Autor: {livro.getAutor()}")
                encontrados = True

        if not encontrados:
            print(f"Não há livros cadastrados no gênero {genero_selecionado}.")

        os.system("pause")
        os.system("cls")


#-------------------------------------------------
def listar_todos():
    for id_livro, livro in dicionario.items():
        print(f"ID: {id_livro} | Título: {livro.getTitulo()} | Autor: {livro.getAutor()} | Gênero: {livro.getGenero()}")
    os.system("pause")
#-------------------------------------------------
def listar_emprestado():
    encontrados = False
    for id_livro, livro in dicionario.items():
        if livro.getEmprestado():
            print(f"ID: {id_livro} | Título: {livro.getTitulo()} | Autor: {livro.getAutor()}")
            encontrados = True
    if not encontrados:
        print("Nenhum livro está emprestado.")
    
    os.system("pause")
    os.system("cls")

#-------------------------------------------------
def editar_livro():
    id_livroeditado = int(input("Digite a ID do livro que deseja editar: "))

    if id_livroeditado in dicionario:
        livro = dicionario[id_livroeditado]

        print(f"\nLivro atual: {livro.getTitulo()} | {livro.getAutor()} | {livro.getGenero()}")

        novo_titulo = input("Novo título (pressione Enter para manter): ")
        novo_autor = input("Novo autor (pressione Enter para manter): ")
        novo_genero = input("Novo gênero (pressione Enter para manter): ")

        if novo_titulo.strip(): #strip remove espaço em branco
            livro.titulo = novo_titulo
        if novo_autor.strip():
            livro.autor = novo_autor
        if novo_genero.strip():
            livro.genero = novo_genero

        print("\nLivro atualizado com sucesso!")
        print(f"Novo cadastro: {livro.getTitulo()} | {livro.getAutor()} | {livro.getGenero()}")
    else:
        print("ID não encontrado!")

    os.system("pause")
    os.system("cls")

#-------------------------------------------------