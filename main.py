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
# Sistema de Biblioteca - adiciona listagem, busca e ordenação
 
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
 
 
def listar_livros(livros):
    if len(livros) == 0:
        print("\nNenhum livro cadastrado.")
        return 0
 
    print(f"\n--- Catálogo ({len(livros)} livro(s)) ---")
    for livro in livros:
        print(
            f'"{livro["titulo"]}" - {livro["autor"]} ({livro["ano"]}) '
            f'| ISBN: {livro["isbn"]} | Status: {livro["status"]}'
        )
    return len(livros)
 
 
def buscar_livro(livros, termo, criterio="titulo"):
    termo = termo.lower().strip()
    resultados = []
 
    for livro in livros:
        if termo in livro[criterio].lower():
            resultados.append(livro)
 
    return resultados
 
 
# ordena sem alterar a lista original (usa lambda pra dizer qual campo comparar)
def ordenar_livros(livros, criterio):
    if criterio == "ano":
        return sorted(livros, key=lambda livro: int(livro["ano"]))
    return sorted(livros, key=lambda livro: livro[criterio].lower())
 
 
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
            listar_livros(livros)
        elif opcao == "5":
            criterio = input("Buscar por (titulo/autor): ").strip().lower()
            if criterio not in ("titulo", "autor"):
                criterio = "titulo"
            termo = input("Digite o termo de busca: ").strip()
            resultados = buscar_livro(livros, termo, criterio)
            listar_livros(resultados)
        elif opcao == "6":
            criterio = input("Ordenar por (titulo/autor/ano): ").strip().lower()
            if criterio not in ("titulo", "autor", "ano"):
                print("Critério inválido, usando 'titulo'.")
                criterio = "titulo"
            listar_livros(ordenar_livros(livros, criterio))
        elif opcao == "7":
            print("Encerrando o programa. Até logo!")
            programa_ativo = False
        else:
            print("Opção inválida.")
 
 
if __name__ == "__main__":
    main()