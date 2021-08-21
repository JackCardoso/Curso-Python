def soma_pares(distancia):
    contador = 0
    soma = 0
    while contador < distancia:
        if contador % 2 == 0:
            soma += contador
        contador = contador + 1
    return soma + 1


distanciaAlvo = int(input())
combustivel = int(input())


if distanciaAlvo >= 0 and combustivel >= 0:
    for distanciaAtual in range(1, distanciaAlvo + 1):

        consumo = distanciaAlvo / soma_pares(distanciaAtual)
        if combustivel < consumo or combustivel < 0:
            break

        combustivel = float(combustivel - consumo)
        print(int(distanciaAtual), int(combustivel))
else:
    exit()
