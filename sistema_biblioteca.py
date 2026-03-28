"""
-A importância de organizar dados na memória utilizando listas, tuplas e dicionários.
-Como listas em Python são estruturas mutáveis e como adicionar elementos usando métodos como append e insert.
-Que tuplas são imutáveis, acessíveis por índices, e não permitem a modificação de seus elementos.
-Dicionários em Python são mutáveis, utilizam pares chave-valor e permitem o acesso rápido aos seus elementos.
-O uso do loop for para iterar sobre listas, tuplas e dicionários.
-A modificação e reordenação de listas através da atribuição de novos valores aos índices.
-Que tentativas de alterar tuplas resultam em erro devido à sua natureza imutável.
-A utilização do método items() para iterar sobre pares chave-valor em dicionários."""

biblioteca = []
categorias = ("Romance", "Novela", "Conto", "Crônica", "Fábula", "Lenda/Mito", "HQS/Mangá")

def menu():
    print("••••••••••𝐖𝐄𝐋𝐂𝐎𝐌𝐄••••••••••")
    print("1. Cadastrar Livro")
    print("2. Listar Livros")
    print("3. Alocar Livro")
    print("4. Devolver Livro")
    print("5. Listar livros disponíveis")
    print("0. Sair")

    

def cadastrar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))

    print(f"Categorias disponíveis: {categorias}")
    categoria = input("Categoria: ")

    while categoria not in categorias:
        print("Categoria inválida. Tente novamente!")
        categoria = input("Categoria: ")

    livro = {
        "id": len(biblioteca)+1,
        "titulo":titulo,
        "autor": autor,
        "ano":ano,
        "disponivel": True
    }

    biblioteca.append(livro)
    print("Livro cadastrado com sucesso. ✅")


def listar_livros():
    if len(biblioteca) == 0:
        print("Nenhum livro cadastrado.")
        return
    
    for livro in biblioteca:
        print(30 * "•")
        for chave, valor in livro.items():
            print(f"{chave.capitalize()}: {valor}")
        print(30 * "•")

def emprestar_livro():

    titulo = input("Título: ")

    for livro in biblioteca:
        if titulo.lower() == livro['titulo'].lower():
            if livro["disponivel"] == False:
                print("Este livro está emprestado.")
            else:
                livro["disponivel"] = False
                print(f"Livro {livro['titulo']} alocado com sucesso. ✅")  
            return
            
                    
def devolver_livro():

    titulo = input("Título: ")

    for livro in biblioteca:
        if titulo.lower() == livro['titulo'].lower():
            if livro["disponivel"] == True:
                print("Este livro não está emprestado.")
            else:
                livro["disponivel"] = True
                print(f"Livro {livro['titulo']}devolvido com sucesso")
            return
        
    print("Livro não encontrado.")

def listar_livros_disponiveis():
        for livro in biblioteca:
            if livro["disponivel"] == True:
                for chave, valor in livro.items():
                    print(f"{chave.capitalize()}: {valor}")

while True:
    menu()
    opcao = input("\n Escolha uma opção: ")

    if opcao == 1:
        cadastrar_livro()
    elif opcao == 2:
        listar_livros()
    elif opcao == 3:
        emprestar_livro()
    elif opcao == 4: 
        devolver_livro()
    elif opcao == 5:
        listar_livros_disponiveis()
    elif opcao == 0:
        print("Até logo!")
        break
    else:
        print("Opção Inválida.")