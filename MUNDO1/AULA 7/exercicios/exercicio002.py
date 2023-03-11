n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
soma = n1 + n2
multi = n1 * n2
divi = n1 / n2
divint = n1 // n2
pot = n1 ** n2
rest = n1 % n2

print(f'A soma entre {n1} e {n2} é {soma}, a multiplicção é {multi}, a divisão é {divi:.2f}, a divisão inteira é {divint:.2f}, a potência é {pot} e o resto da divisão é {rest}!')

# print(f'blablabla', end='') tira a quebra de linha
# print(f'bla \n blabla') quebra a linha