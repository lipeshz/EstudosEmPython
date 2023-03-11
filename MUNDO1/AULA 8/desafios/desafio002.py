#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento de sua hipotenusa.

import math

cad = float(input('Escreva o valor do cateto adjacente: '))
cop = float(input('Digite o valor do cateto oposto: '))
hip = math.hypot(cad, cop)

print(f'A soma dos quadrados dos catetos é igual a soma do quadrado da hipotenusa, ou seja, {cad} ao quadrado é {cad} e {cop} ao quadrado é {cop}. Sendo assim, o comprimento da hipotenusa é de {hip:.2f}')

#Outra forma de fazer.
#cad = float(input('Escreva o valor do cateto adjacente: '))
#cop = float(input('Digite o valor do cateto oposto: '))
#hip = (cad ** 2 + cop ** 2) ** (1/2)

#print(hip)