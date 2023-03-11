#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas. Quantas letras ao todo (sem considerar espaços). Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).capitalize().lstrip().rstrip()
print('Analisando seu nome...')

#Minúsculas e maiúsculas
print('Seu nome com letras maiúsculas')
print(nome.upper())
print('Seu nome com letras minúsculas')
print(nome.lower())

#Quantas letras tem o nome sem considerar espaços
n = nome.replace(' ', '')
print('O tamanho do seu nome sem considerar espaços')
print(f'Seu nome é {nome} e tem {len(n)} caracteres')

#Quantas letras tem o primeiro nome
dividido = nome.split()
print(f'Seu primeiro nome é {dividido[0]} e tem {len(dividido[0])} letras')