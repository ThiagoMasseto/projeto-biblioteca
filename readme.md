
-----

# Gerenciador de Biblioteca em Python

Este é um sistema de gerenciamento de biblioteca simples e funcional, desenvolvido em Python. Ele permite que você organize, catalogue e gerencie o status de empréstimo de livros de maneira eficiente através de uma interface de console interativa.

## 🚀 Funcionalidades

O sistema oferece uma gama completa de funcionalidades para o gerenciamento de livros:

  * **Adicionar Livro**: Cadastre um novo livro na biblioteca, informando o título, autor e gênero.
  * **Remover Livro**: Exclua um livro do catálogo permanentemente, utilizando seu ID exclusivo.
  * **Emprestar e Devolver Livro**: Altere o status de empréstimo de um livro, marcando-o como "emprestado" ou "disponível".
  * **Editar Detalhes do Livro**: Modifique as informações de um livro existente (título, autor ou gênero) a qualquer momento.
  * **Listagem Completa**: Visualize todos os livros do acervo, com seus respectivos IDs, títulos, autores e gêneros.
  * **Listagem Filtrada**: Busque e liste livros com base em critérios específicos:
      * Por **Autor**: Encontre todos os livros de um autor.
      * Por **Gênero**: Liste todos os livros de um gênero específico.
      * Por **Status**: Visualize apenas os livros que estão atualmente emprestados.

## 📁 Estrutura de Arquivos

O projeto é modular e está organizado em três arquivos principais para melhor clareza e manutenção:

  * `classes.py`: Define a classe **`Livro`**, que é a representação de um livro no sistema. Contém atributos para título, autor, gênero e o status de empréstimo, além de métodos para acessá-los e modificá-los (getters e setters).
  * `defs.py`: Contém todas as funções (métodos) que executam as operações do sistema, como `adicionar_livro()`, `remover_livro()`, `emprestar_livro()`, etc. Isso mantém a lógica de negócio separada da interface do usuário.
  * `main.py`: O arquivo principal que inicializa o programa. Ele importa as funções e a classe dos outros arquivos, exibe o menu interativo no console e gerencia o fluxo de execução com base na escolha do usuário.

## ⚙️ Como Usar

### Pré-requisitos

Você precisa ter o Python 3.x instalado em sua máquina.

### Instalação

Não há necessidade de instalação de bibliotecas externas. Basta clonar ou baixar os arquivos do projeto para uma pasta local.

### Execução

1.  Abra o terminal ou prompt de comando.
2.  Navegue até o diretório onde você salvou os arquivos do projeto.
3.  Execute o seguinte comando para iniciar o programa:

<!-- end list -->

```bash
python main.py
```

4.  Siga as instruções exibidas no menu para interagir com o gerenciador da biblioteca. O catálogo já vem com 25 livros pré-cadastrados para você testar todas as funcionalidades imediatamente.

## 📝 Licença

Este projeto é de código aberto e está disponível sob a licença **MIT**. Sinta-se à vontade para usar, modificar e distribuir.
