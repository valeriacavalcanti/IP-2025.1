# programa para ler um texto e substituir
# todos os espaços em branco por asterisco

texto = input('Texto: ')
novo_texto = ''

for s in texto:
    if s == ' ':
        novo_texto += '*'
    else:
        novo_texto += s

print(texto)
print(novo_texto)
print(texto.replace(' ','*'))
