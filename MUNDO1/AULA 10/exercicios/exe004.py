n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

#Calculando a média
media = (n1 + n2) / 2

#Print da média
print(f'Sua média foi {media}!')

#Condicionando a média
if media >= 6:
    print('Você foi aprovado! Parabéns!')
else:
    print('Você foi reprovado! Mas nunca é tarde para mmelhorar!')