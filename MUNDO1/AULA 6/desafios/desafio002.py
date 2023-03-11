#Crie um programa que leia algo pelo teclado e mostre seu tipo e todas as informações sobre ele.

algo = input('Digite algo: ')

print(f'O tipo de {algo} é:')
print(type(algo))

print(f'{algo} é numérico?')
print(algo.isnumeric())

print(f'{algo} é decimal?')
print(algo.isdecimal())

print(f'{algo} é alfabético?')
print(algo.isalpha())

print(f'{algo} é alfanumérico?')
print(algo.isalnum())

print(f'{algo} está em letras maiúsculas?')
print(algo.isupper())

print(f'{algo} está em letras minúsculas?')
print(algo.islower())
