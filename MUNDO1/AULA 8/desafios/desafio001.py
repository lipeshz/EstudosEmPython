#Crie um programa que leia um número inteiro qualquer pelo teclado e mostre sua porção inteira na tela.
import math

num = float(input('Digite um número ponto flutuante: '))
inteiro = math.trunc(num)

print(f'O número {num} truncado é {inteiro}.')
#print(f'O número {num} truncado é {int(num)}')