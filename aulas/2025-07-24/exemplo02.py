pessoas = []

for i in range(2):
    p = {}

    p['nome'] = input('Nome: ')
    p['idade'] = int(input('Idade: '))
    p['cpf'] = input('CPF: ')

    pessoas.append(p)

# exibir os dados de TODAS as pessoas
for i in range(len(pessoas)):
    print(pessoas[i]['nome'])

# procurar os dados de "primei  ra" e exibir
for i in range(len(pessoas)):
    if pessoas[i]['nome'] == 'primeira':
        print(pessoas[i])
