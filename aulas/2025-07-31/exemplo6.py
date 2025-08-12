# programa para conhecer a tabela ascii

print('símbolos numéricos')
cod_0 = ord('0')
cod_9 = ord('9')
for cod_dec in range(cod_0, cod_9 + 1):
    simbolo = chr(cod_dec)
    cod_bin = bin(cod_dec)
    print(cod_dec, cod_bin, simbolo)
        
print('símbolos - letras maiúsculas')
cod_A = ord('A')
cod_Z = ord('Z')
for cod_dec in range(cod_A, cod_Z + 1):
    simbolo = chr(cod_dec)
    cod_bin = bin(cod_dec)
    print(cod_dec, cod_bin, simbolo)


print('símbolos - letras minúsculas')
cod_a = ord('a')
cod_z = ord('z')
for cod_dec in range(cod_a, cod_z + 1):
    simbolo = chr(cod_dec)
    cod_bin = bin(cod_dec)
    print(cod_dec, cod_bin, simbolo)
