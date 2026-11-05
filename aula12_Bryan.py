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


def ver_ranking():
    jogadores = carregar_dados()
    jogadores.sort(key=lambda x: x["pontuacao"], reverse=True)

    print("\n=== RANKING ===")

    posicao = 1
    for jogador in jogadores:
        print(f'{posicao} - {jogador["nome"]} - {jogador["pontuacao"]}')
        posicao += 1


def relatorio():
    jogadores = carregar_dados()

    if len(jogadores) == 0:
        print("Nenhum jogador cadastrado!")
        return

    total = 0
    maior = float("-inf")
    melhor_jogador = ""

    for jogador in jogadores:
        pontos = jogador["pontuacao"]
        total += pontos

        if pontos > maior:
            maior = pontos
            melhor_jogador = jogador["nome"]

    media = total / len(jogadores)

    print("\n=== RELATÓRIO ===")
    print(f"Pontuação média: {media:.2f}")
    print(f"Soma de todos os pontos: {total}")
    print(f"Melhor jogador: {melhor_jogador} - {maior}")


def buscar_jogador():
    nome = input('Nome do Jogador: ')
    jogadores = carregar_dados()
    encontrado = False
    for jogador in jogadores:
        if jogador['nome'].lower() == nome.lower():
            print(f'\n===JOGADOR ENCONTRADO===')
            print(f'Nome: {jogador["nome"]}')
            print(f'Pontuacao: {jogador["pontuacao"]}')
            encontrado = True
    if not encontrado:
        print('Jogador não localizado!')


while True:
    print('\n===SISTEMA DE JOGADORES===')
    print('1 - Cadastrar jogador')
    print('2 - Ranking')
    print('3 - Relatório')
    print('4 - Buscar jogador')
    print('5 - Sair')

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        cadastrar_jogador()
    elif opcao == '2':
        ver_ranking()
    elif opcao == '3':
        relatorio()
    elif opcao == '4':
        buscar_jogador()
    elif opcao == '5':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Tente novamente.')
