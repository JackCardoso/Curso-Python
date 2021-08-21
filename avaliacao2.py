
mapa = [["INICIO", "O", "O", "X"], ["X", "PORTA 3", "O", "PORTA 1"], ["X", "X", "PORTA 2", "X"]]


entrada = ""
linha = 0
coluna = 0
anterior = linha, coluna
atual= linha, coluna

keys = 'E, D, B, C, e, d, b, c'
while mapa[linha][coluna] == "O" or mapa[linha][coluna] == "INICIO":
    entrada = input().strip()

    if entrada in keys:
        maisAnteior= anterior
        anterior = linha, coluna

        if entrada == "E" or entrada == "e":
            coluna -=1
        if entrada == "D" or entrada == "d":
            coluna +=1
        if entrada == "B" or entrada == "b":
            linha += 1
        if entrada == "C" or entrada == "c":
            linha -= 1
        if mapa[linha][coluna] == "PORTA 1":
            print("P1")
            break
        if mapa[linha][coluna] == "PORTA 2":
            print("P2")
            break
        if mapa[linha][coluna] == "PORTA 3":
            print("P3")
            break
        if (linha < 0) or (coluna < 0) or (linha > 3) or ( coluna > 4):
            print("E")
            break
        if mapa[linha][coluna] == "X":
            print("X")
            break
        if maisAnteior == (linha, coluna):
            print("V")
    else:
        print("E")
        break