#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça o programa que o ajude, lendo o nome deles e escrevendo o nome do escolhido.

import random

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

#Ele atribui o valor de todos os dados digitados em uma constante e depois cria uma variavel que sortea um dos valores atribuidos
sorteado = [aluno1, aluno2, aluno3, aluno4]

resultado = random.choice(sorteado)

print(f'Dos alunos, {aluno1}, {aluno2}, {aluno3} e {aluno4}, o vencedor foi: {resultado}!')