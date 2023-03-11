#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de sua cidade para sabermos se nele tem "Santo": ')).capitalize().strip()
cidade = cidade.split()
print('Santo' in cidade[0:])