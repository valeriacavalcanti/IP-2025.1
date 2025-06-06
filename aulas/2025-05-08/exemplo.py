# media aritmetica
def media_aritmetica(valor1: int, valor2: int, valor3: int) -> float:
    media = (valor1 + valor2+ valor3) / 3
    return media

# media ponderada
def media_ponderada(valor1: int, valor2: int, valor3: int) -> float:
    media = (valor1 * 2 + valor2 *3 + valor3 * 5) / 10
    return media

# maior
def maior(valor1: float, valor2: float) -> float:
    if (valor1 > valor2):
        return valor1
    else:
        return valor2

# situacao
def situacao(valor: float) -> str:
    if valor >= 70:
        return "Aprovado"
    else:
        return "Reprovado"


def me_diga_se_passei(valor1: float, valor2: float, valor3: float) -> bool:
    media1 = media_aritmetica(valor1, valor2, valor3)
    media2 = media_ponderada(valor1, valor2, valor3)
    media_final = maior(media1, media2)
    if situacao(media_final) == 'Aprovado':
        return True
    else:
        return False
                      


## main
nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))

print(me_diga_se_passei(nota1, nota2, nota3))

