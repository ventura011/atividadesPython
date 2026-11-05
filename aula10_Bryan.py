import json

def carregar_dados():
    try:
        with open("jogadores.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_dados(jogadores):
    with open("jogadores.json", "w", encoding="utf-8") as arquivo:
        json.dump(jogadores, arquivo, indent=4, ensure_ascii=False)

def cadastrar_jogador():
    jogadores = carregar_dados()

    nome = input("Nome do jogador: ")
    idade = int(input("Idade: "))
    pontuacao = int(input("Pontuação: "))

    jogador = {
        "nome": nome,
        "idade": idade,
        "pontuacao": pontuacao
    }

    jogadores.append(jogador)
    salvar_dados(jogadores)

    print("Jogador cadastrado com sucesso!")

cadastrar_jogador()