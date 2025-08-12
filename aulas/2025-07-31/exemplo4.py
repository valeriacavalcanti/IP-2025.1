# programa para ler um texto, calcular
# a quantidade de dígitos numéricos

texto = input('Texto: ')
qtd_numeros = 0

for s in texto:
    if s in '0123456789':
        qtd_numeros += 1

print(qtd_numeros)
        
