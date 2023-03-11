

frase = 'Curso em Vídeo Python'
frase1 = frase.replace('Python', 'Android')
print(frase.replace('Python', 'Android')) #Substitui a palavra 'Python' por 'Android'

#Encontrando a posição

print(frase.find('Android')) #Retorna -1, pois para alterar o valor e dizer que realmente existe, precisamos de uma outra vairável para guardar o valor alterado
print(frase1.find('Android')) #Vairável que recebe o valor alterado e retorna sua posição

#Verificando se existe

print('Android' in frase) #Retorna False pois não existe 'Android' em 'frase'
print('Android' in frase1) #Retorna True pois existe 'Android' na variável com valor alterado ('frase1')
