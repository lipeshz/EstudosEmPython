#Desenvolva um programa que leia o comprimento de três retase dia gao usuário se elas podem ou não formar um triângulo.

base = int(input('Digite o valor da base: '))
e = int(input('Digite o valor do lado esquerdo: '))
d = int(input('Digite o valor do lado direito: '))

if base < e + d and e < base + d and d < base + e:
    print(f'Com os lado {base}, {e}, {d} é possível formar um triângulo.')
else:
    print(f'Com as medidas {base}, {e} e {d} não é possível formar um triângulo.')