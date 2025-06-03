# Programa para ler VÁRIOS números inteiros. O programa deve encerrar ao ser digitado o valor
# 0 (zero).

# Exibir todos os números digitados.

numeros = []
#qtd = 0

# ler os números

num = int(input('Número: '))
while num != 0:
    numeros.append(num)
#    qtd += 1
    num = int(input('Número: '))

# exibir todos os números digitados (um por linha)
for i in range(len(numeros)):
    print(numeros[i])
