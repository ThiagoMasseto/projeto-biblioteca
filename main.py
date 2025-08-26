import os
import time
from defs import *
while True:
    print("Seja bem vindo a biblioteca! Selecione a opção que deseja!\n" \
        "0-Sair\n1-Adicionar livro\n2-Remover livro\n3-Listar todos os livros\n4-Listar livro por autor\n5-listar livro por genero\n6-Listar livros emprestados\n7-Editar detalhes do livro\n8-Emprestar Livro\n9-Devolver Livro")
    escolha=int(input("-->"))
    time.sleep(1)
    os.system("cls")
    if escolha == 1:
        adicionar_livro()
    elif escolha == 2:
        remover_livro()
    elif escolha == 3:
        listar_todos()
    elif escolha == 4:
        pass
    elif escolha == 5:
        listar_genero()
    elif escolha == 6:
        listar_emprestado()
    elif escolha == 7:
        editar_livro()
    elif escolha == 8:
        emprestar_livro()
    elif escolha == 9:
        devolver_livro()
    elif escolha == 0:
        break
    else:
        print("Numero inválido, tente novamente!")
        time.sleep(1.5)