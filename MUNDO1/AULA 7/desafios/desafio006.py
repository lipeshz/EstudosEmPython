#Crie um programa que leia o quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere: US$1.00 = R$3.27

n1 = float(input('Digite o valor depositado: '))
dolar = n1 / 3.27

print(f'O valor depositado foi {n1} reais. Você pode comprar {dolar:.2f} dólares.')