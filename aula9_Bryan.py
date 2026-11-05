import json

jogador = {
    "nome": "Nathan",
    "idade": 49,
    "pontuacao": 1500
}

jogadores = []

jogadores.append(jogador)


with open('jogadores.json', 'w', encoding='utf-8') as arquivo:
    json.dump(jogadores, arquivo, indent=4)

with open('jogadores.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

for jogador in dados:
    print(f'Nome: {jogador["nome"]}')
    print(f'Pontuação: {jogador["pontuacao"]}')