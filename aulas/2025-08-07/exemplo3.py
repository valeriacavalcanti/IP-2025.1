# programa para ler uma palavra e exibir se
# essa palavra contém apenas letras maiúsculas

palavra = input('Palavra: ')

e_maiuscula = True
for s in palavra:
    if s < 'A' or s > 'Z':
        e_maiuscula = False
        break

if e_maiuscula == True:
    print('palavra maiúscula')
else:
    print('palavra não é maiúscula')

print(palavra, palavra.isupper())
