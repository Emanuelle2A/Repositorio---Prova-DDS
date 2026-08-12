# Sistema de Gerenciamento de Biblioteca

Sistema em Python, feito para terminal, que controla o acervo de uma biblioteca:
cadastro de livros, empréstimos, devoluções, listagem, busca e ordenação. Os dados
ficam salvos em um arquivo CSV, então o catálogo continua existindo mesmo depois de
fechar o programa.

## Como executar

Pré-requisito: Python 3 instalado.

```bash
python3 main.py
```

O programa abre um menu no terminal. Basta digitar o número da opção desejada.
Na primeira execução, o arquivo `livros.csv` estará vazio (só com o cabeçalho);
ele vai sendo preenchido conforme você cadastra livros.

## Funcionalidades

- **Cadastrar livro**: registra título, autor, ano, ISBN e status inicial "disponível"
- **Emprestar livro**: muda o status de um livro (buscado por ISBN) para "emprestado"
- **Devolver livro**: muda o status de volta para "disponível"
- **Listar livros**: mostra todos os livros cadastrados com seus status
- **Buscar livro**: busca por título ou autor (busca parcial, sem diferenciar maiúsculas/minúsculas)
- **Ordenar listagem**: ordena por título, autor ou ano, sem alterar a ordem original da lista

## Requisitos técnicos aplicados

| Requisito | Onde está no código |

| Menu com if/elif/else | Função `main()`, dentro do laço principal |
| Repetição com while | `while programa_ativo:` em `main()`, mantém o menu ativo até a opção "Sair" |
| Funções com parâmetro e retorno (mín. 3) | `cadastrar_livro`, `buscar_livro`, `listar_livros`, `ordenar_livros`, `emprestar_livro`, `devolver_livro`, `carregar_livros`, `salvar_livros` |
| Lista de dicionários em memória | Variável `livros`, uma lista onde cada item é um dicionário representando um livro |
| Persistência em arquivo | `carregar_livros()` lê o CSV ao iniciar; `salvar_livros()` grava no CSV a cada alteração |
| Apenas biblioteca padrão | Usa somente `csv` e `os`, que já vêm com o Python |

## Estrutura do projeto

```
biblioteca-python/
main.py       # código do sistema
livros.csv    # onde o catálogo é salvo
README.md
```