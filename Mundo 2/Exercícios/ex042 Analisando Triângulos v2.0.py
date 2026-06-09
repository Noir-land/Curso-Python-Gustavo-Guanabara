'''
Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
equilátero: todos os lados iguais
isósceles: dois lados iguais
escaleno: todos os lados diferentes
'''

a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))
if a < b + c and b < a + c and c < a + b:
    print("podem forma um triangulo", end=" ")
    if a == b == c:
        print("EQUILATERO")
    elif a != b != c != a:
        print("ESCALENO")
    else:
        print("ISOSCELE")
else:
    print("Não podem forma um triangulo")
