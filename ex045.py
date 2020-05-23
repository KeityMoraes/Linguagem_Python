from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print ('{:=^5}'.format('ADEDONHA'))
print('[0] para pedra')
print('[1] para papel')
print('[2] para tesoura')
jogador = int(input('Digite sua jogada: '))
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('\033[0:32mJOGADOR VENCEU')
    elif jogador == 2:
        print('\033[33mJogador perdeu')
    else:
        print('Jogada invalida')
if computador == 1:
    if jogador == 0:
        print('\033[33mJogador perdeu')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('\033[0:32mJOGADOR VENCEU')
    else:
        print('Jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('\033[0:32mJOGADOR VENCEU')
    elif jogador == 1:
        print('\033[33mJogador perdeu')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')


