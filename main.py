a = int(input("Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilátero")
    elif a == b or a == c or b == c:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não é um triângulo")
