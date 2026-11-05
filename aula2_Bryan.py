#Data: 30/09  Bryan Ventura

print('1 Cadastrar Jogador')
print('2 Ver ranking')

opcao=input('Escolha uma opção')

if opcao=='1':
   nome = input('Digite seu nome: ')
   pontuacao = input('Digite sua pontuação: ')
   arquivo = open("jogadores.txt","a")
   arquivo.write(nome + "=" + pontuacao + "\n")
   arquivo.close
   print('Jogador salvo com sucesso!')

elif opcao=='2':
   arquivo = open("jogadores.txt","r")
   linhas = arquivo.readlines()
   arquivo.close()
   print('===RANKING===')
   for linha in linhas:
       print(linha)
else:
   print('Opção Inválida')