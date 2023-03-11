#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: '))
nome = nome.split()
print(nome[0] + ' ' + nome[-1])