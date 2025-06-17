# declaração da matriz
matriz = []
for i in range(3):
    matriz.append([0] * 4) # add linhas na matriz


# percorrer todas as posições da matriz
for i in range(3): # linhas
    for j in range(4): # colunas de cada linha
        matriz[i][j] = int(input('Número: '))


# exibir todos os valores que estão na matriz
for i in range(3):
    for j in range(4):
        print(f'Na linha {i} coluna {j} tem valor {matriz[i][j]}')
