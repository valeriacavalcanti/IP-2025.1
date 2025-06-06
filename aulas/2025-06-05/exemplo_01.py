def soma_valores(lista: list) -> int:
    soma = 0
    for i in range(len(lista)):
        soma = soma + lista[i]
    return soma

def media_valores(lista: list) -> float:
    return soma_valores(lista) / len(lista)

def quantidade_valores_acima_media_1(lista: list) -> int:
    qtd = 0
    for i in range(len(lista)):
        if lista[i] > media_valores(lista):
            qtd += 1
    return qtd

def quantidade_valores_acima_media_2(lista: list) -> int:
    qtd = 0
    media = media_valores(lista)
    for i in range(len(lista)):
        if lista[i] > media:
            qtd += 1
    return qtd


def menor_valor(lista: list) -> int:
    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor


def maior_valor(lista: list) -> int:
    maior = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior



# programa para ler e armazenar 8 números.

#numeros = [0] * 8
numeros = [15,2,9,26,71,21,17,2]

#for i in range(8):
#    numeros[i] = int(input(f'Número {i + 1}: '))

# soma dos elementos
print('Soma =', soma_valores(numeros))
print('Soma =', sum(numeros))

# média dos elementos
print('Média =', media_valores(numeros))

#for i in range(1_000_000):
    # quantidade de valores acima da média
 #   quantidade_valores_acima_media_1(numeros)
#    print('Quantidade acima =', quantidade_valores_acima_media_1(numeros))


# quantidade de valores acima da média
print('Quantidade acima =', quantidade_valores_acima_media_1(numeros))

# menor valor lido
print('Menor: ', menor_valor(numeros))
print('Menor: ', min(numeros))

# maior valor lido
print('Maior: ', maior_valor(numeros))
print('Maior: ', max(numeros))

