#SPLIT divide a frase de acordo com o espaços

frase = 'Curso em Vídeo Python'

print(frase.split()) #Veja que a divisão acontece de acordo com os espaços da frase. Dessa forma reiniciando a contagemd e caracteres: C sendo 0 da primeira palavra e E sendo o 0 da segunda palavra e a contagem de palavras começa no 0, sendo 'Curso' = 0 e 'em' = 1.

dividido = frase.split()
print(dividido[0][1]) #Retorna a letra 1 da palavra 0