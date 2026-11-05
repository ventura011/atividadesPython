#Data: 07/10  Bryan Ventura

import csv

nome = input("Nome da pessoa jogadora: ")
pontuacao = input("Quantidade de pontos: ")
idade = input("Idade: ")

arquivo = open("jogadores.csv", "a", encoding="utf-8")

arquivo.write(f"{nome},{idade},{pontuacao}\n")
arquivo.close()

arquivo = open("jogadores.csv", "r", encoding="utf-8")

linhas = arquivo.readlines()

arquivo.close()

print("==== JOGADORES ====")

for linha in linhas:
    dados = linha.strip().split(",")

    nome = dados[0]
    pontuacao = dados[1]
    idade = dados[2]

    print(f"Nome: {nome} - " f"Idade: {idade} - " f"Pontuação: {pontuacao}")