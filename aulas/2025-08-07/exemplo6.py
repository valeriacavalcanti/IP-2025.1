# programa para ler um texto e identificar
# as palavras (tokens) e respectivas frequências


texto = input('Texto: ')
tokens = texto.split()

tokens_distintos = []
freq_tokens_distintos = []

for token in tokens:
    if token not in tokens_distintos:
        tokens_distintos.append(token)
        freq_tokens_distintos.append(1)
    else:
        posicao = tokens_distintos.index(token)
        freq_tokens_distintos[posicao] += 1
    #print(token)

print(tokens_distintos)
print(freq_tokens_distintos)
