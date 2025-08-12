# programa para exibir

# símbolos numéricos
for i in range(10):
    numero = i
    simbolo = str(numero)
    cod_dec = ord(simbolo)
    cod_bin = bin(cod_dec)
    cod_oct = oct(cod_dec)
    cod_hex = hex(cod_dec)
    print(numero, simbolo, cod_dec, cod_bin, cod_oct, cod_hex)

# letras maiúsculas
cod_A = ord('A')
cod_Z = ord('Z')
for i in range(cod_A, cod_Z + 1):
    cod_dec = i
    simbolo = chr(cod_dec)
    cod_bin = bin(cod_dec)
    cod_oct = oct(cod_dec)
    cod_hex = hex(cod_dec)
    print(numero, simbolo, cod_dec, cod_bin, cod_oct, cod_hex)


# letras minúsculas
cod_a = ord('a')
cod_z = ord('z')
for i in range(cod_a, cod_z + 1):
    cod_dec = i
    simbolo = chr(cod_dec)
    cod_bin = bin(cod_dec)
    cod_oct = oct(cod_dec)
    cod_hex = hex(cod_dec)
    print(numero, simbolo, cod_dec, cod_bin, cod_oct, cod_hex)
