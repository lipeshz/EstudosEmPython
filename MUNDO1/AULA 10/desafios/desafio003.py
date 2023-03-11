#Crie um progrram que leia um númmero inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número e iremos verificar se ele é PAR ou ÍMPAR: '))

resto = num % 2 #% Cálcula o resto da divisão

if resto == 0:
    print(f'Pelos meus cálculos, {num} é par, pois o resto de sua divisão por 2 é {resto}!')
else:
    print(f'O número digitado foi {num}, que pelos meus cálculos é ímpar pois o resto de sua divisão por 2 é {resto}')