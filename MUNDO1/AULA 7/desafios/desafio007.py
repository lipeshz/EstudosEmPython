#Faça um programa que leia a altura e a largura de uma parede em metros, calcule sua área e a quantidade de tinha necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados.

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da mesma parede: '))
tamanho = altura * largura
tinta = tamanho / 2

print(f'Sua parede tem {altura} metros de altura e {largura} metros de largura. Com {tamanho} metros quadrados. Para pintá-la por completo será nescessário {tinta} litro(s) de tinta.')