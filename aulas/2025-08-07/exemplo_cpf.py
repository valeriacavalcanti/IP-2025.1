cpf = '123.456.789-00'

tokens = cpf.split('-')

numeros = tokens[0].replace('.', '')
digito = tokens[1]

print(numeros)
print(digito)
