"""
Aluguel de carros:
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
"""

d = float(input("Dias de uso:"))
k = float(input("KM percorrido: "))
r = (d*60) + (k*0.15)
print("O valor a pagar é R${}".format(r))
