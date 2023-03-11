#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

km = float(input('Digite quantos Kms você irá viajar: '))

if km <= 200:
    preco = km * 0.50
    print(f'Você irá viajar por {km:.2f}Kms e o custo será de R${preco:.2f}!')
else:
    preco = km * 0.45
    print(f'Você viajará por {km:.2f}Kms e o custo será de R${preco:.2f}!')