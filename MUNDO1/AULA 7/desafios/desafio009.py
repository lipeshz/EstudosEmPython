#Fça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com um aumento de 15%.

perfil = str(input('Digite seu nome de usuário: '))
senha = str(input('Digite sua senha: '))
salario = float(input('Digite seu salário: '))
aumento = (15 * salario / 100) + salario

print('Entrando...')
print(f'Bem-vindo, {perfil}!')
print(f'Parabéns! Você recebeu um aumento de 15%!! Seu antigo salário de {salario} foi convertido para {aumento}!!')
