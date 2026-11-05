
import csv

def cadastrarJogador():
    nome = input('Nome do jogador: ')
    pontuacao = input('Quantidade de pontos: ')
    idade = input('Idade: ')

    with open('jogadores.csv', 'a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, pontuacao, idade])

    print('Jogador salvo!')


def verRanking():
    try:
        with open('jogadores.csv', 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)

            print('\n=== JOGADORES ===')

            jogadores = list(leitor)

            if not jogadores:
                print('Nenhum jogador cadastrado.')
            else:
                for jogador in jogadores:
                    print(f'Nome: {jogador[0]} | Pontos: {jogador[1]} | Idade: {jogador[2]}')

    except FileNotFoundError:
        print('Nenhum jogador cadastrado ainda.')


while True:
    print('\n1 - Cadastrar jogador')
    print('2 - Ver ranking')
    print('3 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cadastrarJogador()

    elif opcao == '2':
        verRanking()

    elif opcao == '3':
        print('Saindo do sistema...')
        break

    else:
        print('Opção inválida! Tente novamente.')