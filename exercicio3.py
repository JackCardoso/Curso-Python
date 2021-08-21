
valor = int(input())

while valor > 0:

    print(int(valor//100))
    valor = int(valor % 100)

    print(int(valor//50))
    valor = int(valor % 50)

    print(int(valor//25))
    valor = int(valor % 25)

    print(int(valor//10))
    valor = int(valor % 10)

    print(int(valor//5))
    valor = int(valor % 5)

    print(int(valor//1))
    valor = int(valor % 1)


