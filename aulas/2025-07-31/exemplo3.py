# programa para ler um texto, calcular
# a quantidade de vogais

texto = input('Texto: ')
qtd_vogais = 0

for s in texto:
    if s in 'aeiouAEIOU':
        qtd_vogais += 1

print(qtd_vogais)
        
