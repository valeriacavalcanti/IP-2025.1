# programa para ler uma palavra

palavra = input('Palavra: ')
print(palavra)

for i in range(len(palavra)):
    print(i, palavra[i])

palavra[3] = 'é'

print(palavra)
