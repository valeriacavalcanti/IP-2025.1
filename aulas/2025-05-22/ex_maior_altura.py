n = int(input('quantidade: '))
maior_altura = -1
for i in range(n):
    altura = float(input('Altura: '))
    if (altura > maior_altura):
        maior_altura = altura
print('maior altura: ', maior_altura)
