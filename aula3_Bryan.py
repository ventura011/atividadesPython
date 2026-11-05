#Data: 01/10  Bryan Ventura

def cadastrarJogador():
    nome = input("Nome: ")
    pontuacao = input("Pontuação: ")

    arquivo = open("jogadores.txt", "a")
    arquivo.write(nome + " - " + pontuacao + "\n")
    arquivo.close()

    print("Jogador salvo com sucesso!")


def verRanking():
    arquivo = open("jogadores.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    print("=== RANKING ===")

    for linha in linhas:
        print(linha, end="")


while True:
    print()
    print("1 - Cadastrar")
    print("2 - Ver ranking")
    print("3 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        cadastrarJogador()

    elif opcao == "2":
        verRanking()

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida")