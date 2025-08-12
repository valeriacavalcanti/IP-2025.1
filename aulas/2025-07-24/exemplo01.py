def menor_maior(lista: list) -> tuple:
    menor = min(lista)
    maior = max(lista)
    return menor, maior


# main

numeros = [10,20,30,40,50,60]

print(menor_maior(numeros))
