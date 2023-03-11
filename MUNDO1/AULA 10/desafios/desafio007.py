#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

#Para salários superiores a R$1.250,00 calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário: '))

if salario <= 1250:
    aumento = (15 * salario / 100) + salario #Cálculo de aumento

    print(f'Seu salário foi de R${salario:.2f} para R${aumento:.2f}!')
else:
    aumento = (10 * salario / 100) + salario

    print(f'Seu salário foi R${salario:.2f} para aumento R${aumento:.2f}!')