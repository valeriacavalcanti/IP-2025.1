# programa para ler um texto, calcular
# a quantidade de consoantes

texto = 'ifpb IFPB 123 !!'
qtd_consoantes = 0

for s in texto:
    if (s >= 'A' and s <= 'Z') or (s >= 'a' and s <= 'z'):
        if s not in 'aeiouAEIOU':
            qtd_consoantes += 1

print(qtd_consoantes)
        
