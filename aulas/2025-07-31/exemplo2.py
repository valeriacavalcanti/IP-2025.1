# programa para ler um texto, calcular
# a quantidade de vogais

texto = input('Texto: ')
qtd_vogais = 0

for e in texto:
    if e == 'a' or e == 'e' or e == 'i' or e == 'o' or e == 'u':
        qtd_vogais += 1

print(qtd_vogais)
        
