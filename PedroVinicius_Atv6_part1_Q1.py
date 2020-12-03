from random import randint
from time import sleep

lista = ("Pedra", "Papel", "Tesoura")

computador = randint(0,2)

jg1 = int(input('''Escolha uma opcao para se jogar: 
[0] Pedra
[1] Papel
[2] Tesoura
 
Digite sua escolha: '''))

print("JO\n")
sleep(1)
print("KEN\n")
sleep(1)
print("POOH!!!\n")

print("-="*20)
print("O computador escolheu: {}".format(lista[computador]))
print("O jogador escolheu: {}".format(lista[jg1]))
print("-="*20)

if computador == 0:
    if jg1 == 0:
        print("Empate!")
    elif jg1 == 1:
        print("Jogador perdeu")
    elif jg1 == 2:
        print("Computador venceu")
    else:
        print("Operacao invalida")