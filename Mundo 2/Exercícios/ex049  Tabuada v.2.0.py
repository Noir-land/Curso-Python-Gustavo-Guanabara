"""Refaça o desafio 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for
"""

print("~"*20)
n = int(input("Digite o multiplicador: "))
print("~"*15)
for c in range(1, 11):
    print(f"{n} x {c:2} = {n*c} ")
print("~"*15)
