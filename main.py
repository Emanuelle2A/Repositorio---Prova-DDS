import csv
import os
# Sistema de Biblioteca - estrutura inicial (menu + loop)
 
livros = []
 
 
def exibir_menu():
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar listagem")
    print("7 - Sair")
 
 
def main():
    programa_ativo = True
    while programa_ativo:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
 
        if opcao == "1":
            print("(cadastrar - em construção)")
        elif opcao == "2":
            print("(emprestar - em construção)")
        elif opcao == "3":
            print("(devolver - em construção)")
        elif opcao == "4":
            print("(listar - em construção)")
        elif opcao == "5":
            print("(buscar - em construção)")
        elif opcao == "6":
            print("(ordenar - em construção)")
        elif opcao == "7":
            print("Encerrando o programa. Até logo!")
            programa_ativo = False
        else:
            print("Opção inválida.")
 
 
if __name__ == "__main__":
    main()
 # Sistema de Biblioteca - adiciona cadastro de livros
 
livros = []
 
 
def cadastrar_livro(livros):
    print("\n--- Cadastro de novo livro ---")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano = input("Ano de publicação: ").strip()
    isbn = input("Código/ISBN: ").strip()
 
    if titulo == "" or isbn == "":
        print("Título e ISBN são obrigatórios.")
        return False
 
    for livro in livros:
        if livro["isbn"] == isbn:
            print("Já existe um livro com esse ISBN.")
            return False
 
    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponível",
    }
    livros.append(novo_livro)
    print(f'Livro "{titulo}" cadastrado.')
    return True
 
 
def exibir_menu():
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar listagem")
    print("7 - Sair")
 
 
def main():
    programa_ativo = True
    while programa_ativo:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
 
        if opcao == "1":
            cadastrar_livro(livros)
        elif opcao == "2":
            print("(emprestar - em construção)")
        elif opcao == "3":
            print("(devolver - em construção)")
        elif opcao == "4":
            print(livros)  # provisório, ainda sem função de listagem formatada
        elif opcao == "5":
            print("(buscar - em construção)")
        elif opcao == "6":
            print("(ordenar - em construção)")
        elif opcao == "7":
            print("Encerrando o programa. Até logo!")
            programa_ativo = False
        else:
            print("Opção inválida.")
 
 
if __name__ == "__main__":
    main()
 # Sistema de Biblioteca - adiciona empréstimo e devolução
 
livros = []
 
 
def cadastrar_livro(livros):
    print("\n--- Cadastro de novo livro ---")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano = input("Ano de publicação: ").strip()
    isbn = input("Código/ISBN: ").strip()
 
    if titulo == "" or isbn == "":
        print("Título e ISBN são obrigatórios.")
        return False
 
    for livro in livros:
        if livro["isbn"] == isbn:
            print("Já existe um livro com esse ISBN.")
            return False
 
    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponível",
    }
    livros.append(novo_livro)
    print(f'Livro "{titulo}" cadastrado.')
    return True
 
 
def emprestar_livro(livros, isbn):
    for livro in livros:
        if livro["isbn"] == isbn:
            if livro["status"] == "emprestado":
                print("Livro já está emprestado.")
                return False
            livro["status"] = "emprestado"
            print(f'Empréstimo registrado: "{livro["titulo"]}".')
            return True
 
    print("Livro não encontrado.")
    return False
 
 
def devolver_livro(livros, isbn):
    for livro in livros:
        if livro["isbn"] == isbn:
            if livro["status"] == "disponível":
                print("Livro já estava disponível.")
                return False
            livro["status"] = "disponível"
            print(f'Devolução registrada: "{livro["titulo"]}".')
            return True
 
    print("Livro não encontrado.")
    return False
 
 
def exibir_menu():
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar listagem")
    print("7 - Sair")
 
 
def main():
    programa_ativo = True
    while programa_ativo:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
 
        if opcao == "1":
            cadastrar_livro(livros)
        elif opcao == "2":
            isbn = input("ISBN do livro a emprestar: ").strip()
            emprestar_livro(livros, isbn)
        elif opcao == "3":
            isbn = input("ISBN do livro a devolver: ").strip()
            devolver_livro(livros, isbn)
        elif opcao == "4":
            print(livros)  # provisório, ainda sem função de listagem formatada
        elif opcao == "5":
            print("(buscar - em construção)")
        elif opcao == "6":
            print("(ordenar - em construção)")
        elif opcao == "7":
            print("Encerrando o programa. Até logo!")
            programa_ativo = False
        else:
            print("Opção inválida.")
 
 
if __name__ == "__main__":
    main()