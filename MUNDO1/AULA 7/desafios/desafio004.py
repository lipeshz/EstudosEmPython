#Escreva um pograma que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Digite um valor em metros: '))
cent = metro * 100
mili = metro * 1000
hec = metro / 100
dam = metro / 10
dm = metro * 10

print(f'Você digitou {metro} metros, correto? De acordo com as minhas anotações, isso em centímetros deve dar... {cent} centímetros!')
print(f'Oh, você também quer saber em milímetros? Que específico... Pelos meus cálculos é mais ou menos {mili} milímetros!')
print(f'Já que você parece se interessar por esse tipo de assunto, toma a lista completa: {metro} metros em hectares é {hec}, {dam} decâmetros, {dm} decímetros')