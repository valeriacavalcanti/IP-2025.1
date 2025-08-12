# programa para ler um texto e converter
# esse texto para maiúsculo

texto = input('Texto: ')
novo_texto = ''

for s in texto:
    if s >= 'a' and s <= 'z':
        cod_maiusculo = ord(s) - 32
        simbolo_maiusculo = chr(cod_maiusculo)
        novo_texto += simbolo_maiusculo
    else:
        novo_texto += s

print(texto)
print(novo_texto)

print(texto.upper())
print(texto.lower())
