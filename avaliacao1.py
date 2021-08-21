numero = int(input())

retorno = "True"
casa = 10000
aux = 0
if numero // casa < 10:
    for i in range(1, 6):
        valor = int(numero // casa % 10)
        casa = casa // 10

        if (i == 2) and (valor ** 4) % 3 != 0:
            retorno = "False"
        if (i == 4) and (valor ** 4) % 3 != 0:
            retorno = "False"
        if i == 3 and (valor == 0 or valor == 1):
            retorno = "False"
        if i == 3 or i == 5:
            aux += valor
        if i == 5 and aux <= 3:
            retorno = "False"
        if i == 1:
            if valor == 2 or valor == 5 or valor == 9:
                retorno = "True"
            else:
                retorno = "False"
else:
    retorno = "False"


print(retorno)
