# importa o módulo 'os' para interagir com o sistema operacional.
import os

# Importa o módulo 'time' para pausar a execução do programa.
import time

# Importa todas as funções do arquivo 'defs.py'
from defs import *



os.system("cls")

print(50 * "-")
print("Sistema Biblioteca do TI".center(50))
print(50 * "-")

time.sleep(3)

# O programa só será encerrado quando o usuário escolher a opção de saída (opção 0).
while True:

    escolha = None

    os.system("cls")

    print(50 * "-")
    print("Sistema Biblioteca do TI".center(50))
    print(50 * "-")

    
    print("\nSeja bem vindo a biblioteca! Selecione a opção que deseja!")

    print("1 -> Adcionar Livro")
    print("2 -> Remover Livro")
    print("3 -> Listar Todos os Livros")
    print("4 -> Listar Livros por Autor")
    print("5 -> Listar Livros por Genero")
    print("6 -> Listar Livros Emprestados")
    print("7 -> Editar detalhes do Livro")
    print("8 -> Editar Livro")
    print("9 -> Devolver Livro")
    print("0 -> Sair do Software")


    try:
    # Solicita ao usuário que digite um número e o converte para um inteiro
        escolha = int(input("-->"))

    except ValueError:

        print("")





    time.sleep(1)
    os.system("cls")


    if escolha == 1:
        os.system("cls")
        # Se a escolha for 1, a função 'adicionar_livro()' é chamada para adicionar um novo livro.
        adicionar_livro()
    elif escolha == 2:
        os.system("cls")
        # Se a escolha for 2, a função 'remover_livro()' é chamada para excluir um livro.
        remover_livro()
    elif escolha == 3:
        os.system("cls")
        # Se a escolha for 3, a função 'listar_todos()' é chamada para exibir todos os livros.
        listar_todos()
    elif escolha == 4:
        os.system("cls")
        # Se a escolha for 4, a função 'listar_autor()' é chamada para buscar livros por autor.
        listar_autor()
    elif escolha == 5:
        os.system("cls")
        # Se a escolha for 5, a função 'listar_genero()' é chamada para listar livros por gênero.
        listar_genero()
    elif escolha == 6:
        os.system("cls")
        # Se a escolha for 6, a função 'listar_emprestado()' é chamada para exibir os livros emprestados.
        listar_emprestado()
    elif escolha == 7:
        os.system("cls")
        # Se a escolha for 7, a função 'editar_livro()' é chamada para modificar um livro existente.
        editar_livro()
    elif escolha == 8:
        os.system("cls")
        # Se a escolha for 8, a função 'emprestar_livro()' é chamada para alterar o status de um livro.
        emprestar_livro()
    elif escolha == 9:
        os.system("cls")
        # Se a escolha for 9, a função 'devolver_livro()' é chamada para alterar o status do livro de volta para disponível.
        devolver_livro()
    elif escolha == 0:
        print("Saindo...")
        time.sleep(1)
        os.system("cls")
        # Se a escolha for 0, o comando 'break' é executado para sair do loop 'while'
        # e, consequentemente, encerrar o programa.
        break
    else:
        # Se a escolha não for nenhuma das opções válidas (0-9), uma mensagem de erro é exibida.
        print("Numero inválido, tente novamente!")
        # Pausa o programa por 1.5 segundos para que o usuário possa ler a mensagem de erro.
        time.sleep(1.5)
        os.system("cls")
