numeros = [0] * 4

# Ler e armazenar os números no vetor
for i in range(4):
    numeros[i] = int(input('Número: '))

# Exibir os elementos que estão armazenados no vetor
print(numeros)

# Exibir os elementos (um por vez) que estão armazenados no vetor
for i in range(4):
    print(i, numeros[i])
