# Programa para ler 8 números inteiros.
# Ao final, calcular e exibir:
# - soma dos números lidos
# - maior valor lido
# - menor valor lido
# - média dos números lidos
# - Todos os números digitados (do último até o primeiro)

numeros = [0] * 4
soma = 0

for i in range(4):
    numeros[i] = int(input('Número: '))
    soma = soma + numeros[i]

media = soma / 4
maior = numeros[0]
menor = numeros[0]

for i in range(1, 4):
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]

print(soma)
print(maior)
print(menor)
print(media)

for i in range(3, -1, -1):
    print(numeros[i])





    
