#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()
print('Quantas vezes aparece a letra "A"')
print(frase.count('A'))
print('Em que posição ela aparece pela primeira vez?')
print(frase.find('A') +1)
print('Em que posição ela aparece pela última vez?')
print(frase.rfind('A') +1) #Procura letras da direita para esquerda