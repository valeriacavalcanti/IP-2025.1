cidades = [''] * 4
votos = [0] * 4
votos_invalidos = 0

# gravar os nomes das cidades
for i in range(4):
    cidades[i] = input('Nome da cidade: ')

# ler os votos
for i in range(6):
    nome_cidade = input('Informe seu voto: ')
    if nome_cidade in cidades:
        indice = cidades.index(nome_cidade)
        votos[indice] = votos[indice] + 1
    else:
        votos_invalidos += 1

# exibir resultado da votação
for i in range(4):
    if votos[i] > 1:
        print(f'{cidades[i]} teve {votos[i]} votos')
    elif votos[i] == 1:
        print(f'{cidades[i]} teve {votos[i]} voto')
    else:
        print(f'{cidades[i]} não foi votada')

print(f'Votos inválidos: {votos_invalidos}')
