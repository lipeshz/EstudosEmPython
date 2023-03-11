dias = int(input('Digite quantos dias você está com o carro: '))
km = float(input('Quanto KMs você percorreu?: '))

diaspag = dias * 60
kmpag = km * 0.15

print(f'Você ficou {dias} dias com o carro e foram {km:.2f} KM percorridos, você deverá pagar R${diaspag + kmpag}.')