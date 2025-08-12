# programa para ler um símbolo e verificar
# se esse símbolo é uma letra minúscula

simbolo = input('Símbolo: ')

if simbolo >= 'a' and simbolo <= 'z':
    print('minúsculo')
else:
    print('não é minúsculo')

print(simbolo, simbolo.islower(), simbolo.isupper())
