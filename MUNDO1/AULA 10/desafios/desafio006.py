#Faça um programa que leia três número e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3 and n2 > n3:
    print(f'{n1} o maior número e {n3} é o menor.')
elif n1 > n2 and n1 > n3 and n3 > n2:
    print(f'{n1} é o maior número e {n2} é o menor.')
elif n2 > n1 and n2 > n3 and n1 > n3:
    print(f'{n2} é o maior número e {n3} é o menor.')
elif n2 > n1 and n2 > n3 and n3 > n1:
    print(f'{n2} é o maior número e o {n1} é o menor.')
elif n3 > n1 and n3 > n2 and n1 > n2:
    print(f'{n3} é o maior número e o {n2} é o menor.')
elif n1 == n2 and n1 == n3 and n2 == n3:
    print('Todos os números são iguais.')
else:
    print(f'{n3} é o maior número e {n1} é o menor.')