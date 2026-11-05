
import csv
import os


def cadastrarJogador():
    nome = input('Nome do jogador: ')
    
    while True:
        try:
            pontuacao = int(input('Quantidade de pontos: '))
            if pontuacao < 0:
                print('A pontuação não pode ser negativa.')
                continue
            break
        except ValueError:
            print('Digite uma pontuação válida.')

    while True:
        try:
            idade = int(input('Idade: '))
            if idade <= 0:
                print('Digite uma idade válida.')
                continue
            break
        except ValueError:
            print('Digite uma idade válida.')

    with open('jogadores.csv', 'a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, pontuacao, idade])

    print('Jogador salvo com sucesso!')


def verJogadores():
    if not os.path.exists('jogadores.csv'):
        print('Nenhum jogador cadastrado.')
        return

    with open('jogadores.csv', 'r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)

        print('\n=== JOGADORES ===')

        encontrou = False

        for linha in leitor:
            if len(linha) != 3:
                continue

            nome, pontuacao, idade = linha
            print(f'Nome: {nome} - Idade: {idade} - Pontuação: {pontuacao}')
            encontrou = True

        if not encontrou:
            print('Nenhum jogador cadastrado.')


def verRanking():
    jogadores = []

    if not os.path.exists('jogadores.csv'):
        print('Nenhum jogador cadastrado.')
        return

    with open('jogadores.csv', 'r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if len(linha) != 3:
                continue

            nome = linha[0]

            try:
                pontuacao = int(linha[1])
                idade = int(linha[2])
            except ValueError:
                continue

            jogadores.append([nome, pontuacao, idade])

    jogadores.sort(key=lambda x: x[1], reverse=True)

    print('\n=== RANKING ===')

    if not jogadores:
        print('Nenhum jogador cadastrado.')
        return

    posicao = 1

    for jogador in jogadores:
        print(
            f'Posição: {posicao} - '
            f'Nome: {jogador[0]} - '
            f'Pontuação: {jogador[1]}'
        )
        posicao += 1


while True:
    print('\n=== MENU ===')
    print('1 - Cadastrar Jogador')
    print('2 - Ver Jogadores')
    print('3 - Ver Ranking')
    print('4 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cadastrarJogador()
    elif opcao == '2':
        verJogadores()
    elif opcao == '3':
        verRanking()
    elif opcao == '4':
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida! Tente novamente.')
