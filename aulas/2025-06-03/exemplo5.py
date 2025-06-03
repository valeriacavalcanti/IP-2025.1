# Programa para ler 10 (dez) números inteiros. Exibir todos os números digitados.

numeros = [0] * 10

# ler os números
for i in range(10):
    numeros[i] = int(input('Número: '))

# exibir os números digitados (um por linha)
for i in range(10):
    print(numeros[i])
