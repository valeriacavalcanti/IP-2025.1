notas = [0] * 10
soma = 0

# ler as notas
for i in range(10):
	notas[i] = int(input('Nota: '))
	soma = soma + notas[i]

media = soma / 10

# calcular a quantidade de notas com valor acima da média
qtd = 0
for i in range(10):
	if notas[i] > media:
		qtd = qtd + 1

print(qtd)

# exibir as notas que possuem valor abaixo da média
for i in range(10):
	if notas[i] < media:
		print(notas[i])
