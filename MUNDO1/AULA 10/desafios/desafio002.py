#Escreva um pograma que leia a velocidade de um carro.

#Se ele ultrapassar 80km/h, mostre uma maensagem dizendo que ele foi multado.

#A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep

vel = float(input('Digite a velocidade do carro e verificaremos se ele será multado ou não: '))

dif = vel - 80
cobrar = dif * 7

if vel <= 80:
    print('Analisando...')
    sleep(2)
    print('O motorista seguiu as leis de trânsito e não será multado.')
else:
    print('Analisando...')
    sleep(2)
    print(f'O motorista ultrapassou a velocidade limite em {dif}Km/h e será cobrado R${cobrar:.2f}!')