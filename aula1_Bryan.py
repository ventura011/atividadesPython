#Data/30/09  Bryan Ventura

nome = input("Digite seu nome: ")
pontuacao = input("Digite sua pontuação: ")


arquivo = open("jogadores.txt", "a")

arquivo.write(nome + "-" + pontuacao  +  "\n")

arquivo.close ()


print("Jogador salvo com sucesso")