import datetime
import csv
import json

#txt
def salvar_doc(titulo):
    with open("doc.txt", "a", encoding="utf-8") as arquivo:
        agora = datetime.datetime.now()
        arquivo.write(f"{agora} - Livro Cadastrado: {titulo}\n")



biblioteca = []
categorias = ("Romance", "Novela", "Conto", "Crônica", "Fábula", "Lenda/Mito", "HQS/Mangá")

def menu():
    print("•••••••••• 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 ••••••••••")
    print("1. Cadastrar Livro")
    print("2. Listar Livros")
    print("3. Alocar Livro")
    print("4. Devolver Livro")
    print("5. Listar livros disponíveis")
    print("6. Exportar para CSV ")
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
    salvar_doc(titulo)
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
                print(f"Livro {livro['titulo']} devolvido com sucesso")
            return
        
    print("Livro não encontrado.")



def listar_livros_disponiveis():
    for livro in biblioteca:
        if livro["disponivel"] == True:
            for chave, valor in livro.items():
                print(f"{chave.capitalize()}: {valor}")



#exportar 
def exportar_cvs():
    if len(biblioteca) == 0:
        print("Nenhum livro para exportar.")
        return
    
    with open("biblioteca.csv", "w", newline="", encoding="utf-8") as arquivo:
        cabeçalho = biblioteca[0].keys()
        escritor = csv.DictWriter(arquivo, fieldnames=cabeçalho)
        escritor.writeheader()
        escritor.writerows(biblioteca)



def salvar_json():
    with open("biblioteca.json", "w", encoding="utf-8") as f:
        json.dump(biblioteca, f , indent=4)



def carregar_json():
    global biblioteca
    try:
        with open("biblioteca.json", "r", encoding="utf-8") as f:
            biblioteca = json.load(f)
        print("Dados carregados com sucesso.")
    except FileNotFoundError:
        biblioteca = []



carregar_json()



while True:
    menu()
    opcao = input("\n Escolha uma opção: ")

    if opcao == "1":
        cadastrar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        emprestar_livro()
    elif opcao == "4": 
        devolver_livro()
    elif opcao == "5":
        listar_livros_disponiveis()
    elif opcao == "6":
        exportar_cvs()
    elif opcao == "0":
        salvar_json()
        print("Até logo!")
        break
    else:
        print("Opção Inválida.")