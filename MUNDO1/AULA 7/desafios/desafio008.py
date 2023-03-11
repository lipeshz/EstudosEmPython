#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: '))
cupom = str(input('Digite o cupom de desconto: '))
desconto = (preco * 5) / 100

print(f'Preço do produto é {preco}...')
print('Validando cupom...')
print(f'Cupom aplicado. O novo valor será de {desconto}. Deseja continuar?')
