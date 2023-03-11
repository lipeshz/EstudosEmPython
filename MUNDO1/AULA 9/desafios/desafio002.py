#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

if num < 0 or num > 9999:
    print('O número deve ser maior que zero e menor que 9999!')
else:
    print('Analisando...')
    print(f'O número escolhido foi {num}, e seu milhar é {m}, sua centena é {c}, sua dezena é {d} e sua unidade é {u}!')