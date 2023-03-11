#JOIN junta as palavras com algum caractere ou sem espaços

frase = 'Curso em Vídeo Python'
frase = frase.split() #Separa a frase em blocos de letras e palavras
frase = '-'.join(frase) #Junta os blocos de palavras com '-'
print(frase)
