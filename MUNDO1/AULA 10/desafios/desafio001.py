#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuárrio tentar descobrir qual foi o número escolhido pelo computador.

#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

n = random.randint(0, 5)
resp = int(input('Tente adivinhar qual número foi esolhido pelo computador de 0 a 5: '))

if resp < 0 or resp > 5:
    print('A resposta deve ser maior que 0 e menor que 5! Tente novamente!')
elif resp != n:
    print('Processando...')
    sleep(3)
    print(f'Você errou! A resposta era {n}! Tente novamente!')
else:
    print('Processando...')
    sleep(3)
    print(f'Você acertou! Parabéns! A resposta realmente era {n}!')