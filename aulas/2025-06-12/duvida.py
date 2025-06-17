st = input()
cartas = []
naipes = []
#lista = list(st)

for i in range(0, len(st), 3):
    carta = st[i:i+2]
    naipe = st[i+2]
    cartas.append(carta)
    naipes.append(naipe)
    #print(carta, naipe)

print(cartas)
print(naipes)
