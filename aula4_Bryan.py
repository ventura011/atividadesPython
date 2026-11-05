#Data: Bryan Ventura 07/10

def cadastrarJogador():
    nome = input("Digite seu nome: ")
    pontuacao = input("Digite a sua pontuação: ")
    arquivo=open("jogadores.txt","a",encoding="utf-8")
    arquivo.write(nome + " - " + pontuacao + "\n")
    arquivo.close()

    print("Jogador salvo com sucesso!")



def verRanking():
    jogadores = []
    arquivo = open("jogadores.txt","r", encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()

    print('===RANKING===')

    for linha in linhas:
        partes = linha.strip().split(" - ")

        nome = partes[0]
        pontuacao = int(partes[1])

        jogadores.append((nome, pontuacao))

    jogadores.sort(key=lambda x:x[1],reverse=True)

    posicao = 1

    for jogador in jogadores:
        print(posicao, " - ", jogador[0]," - ", jogador[1])
        posicao += 1
        
while True:
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