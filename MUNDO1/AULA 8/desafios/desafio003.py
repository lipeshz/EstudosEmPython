#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

num = float(input('Digite um valor em graus: '))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))

print(f'O valor digitado foi {num:.2f} e seu seno é {sen:.2f}, seu cosseno é {cos:.2f} e sua tangente {tan:.2f}')