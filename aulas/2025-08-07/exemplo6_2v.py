# programa para ler um texto e identificar
# as palavras (tokens) e respectivas frequências


texto = input('Texto: ')
tokens = texto.split()

frequencia = {}

for token in tokens:
    if token not in frequencia:
        frequencia[token] = 1
    else:
        frequencia[token] += 1

print(frequencia)
        


