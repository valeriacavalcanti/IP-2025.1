# programa para ler um texto e
# converter para MAIÚSCULO.

texto = input('Texto: ')
novo_texto = ''

for s in texto:
    if s >= 'a' and s <= 'z':
        cod_dec = ord(s)
        cod_mai = cod_dec - 32
        novo_s = chr(cod_mai)
    else:
        novo_s = s
    
    novo_texto += novo_s

print(novo_texto)
