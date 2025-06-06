nomes = []

while True:
	nome = input('Digite um nome: ')
	
	if nome == 'fim':
		break

	nomes.append(nome)


# exibir os nomes
for i in range(len(nomes)):
	print(nomes[i])
