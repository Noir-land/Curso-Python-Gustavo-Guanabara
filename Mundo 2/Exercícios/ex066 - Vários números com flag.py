"""
Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar 999,
que é a condição de parada (flag).
No final, mostre quantos números foram digitados
e qual foi a acc entre eles (desconsiderando o flag)
"""

n = s = cont = 0
while True:
    n = int(input("Digite um numero.[999 para parar]"))
    if n == 999:
        break
    cont += 1
    s += n
print(f"fim {s}")
print(f"{cont}")
