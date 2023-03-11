print('Qual seu nome?')
nome = str(input('Meu nome é ')).strip().capitalize()

if nome == 'Filipe':
    print('Que nome lindo você tem!')
    print('Bom-dia, Filipe!')
else:
    print('Seu nome é tão sem graça...')
print(f'Bom-dia, {nome}!')