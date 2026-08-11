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
 