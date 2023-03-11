#RSTRIP remove o espaços da direita (r = right)

frase = '   Aprenda Python  '

print(frase)
print(frase.rstrip()) #Veja que os espaços vazios da direita sumiram
print(frase.rstrip().lstrip()) #Jumção para remover os espaços do inicio e o fim da frase, veja que a frase encostou na borda no terminal