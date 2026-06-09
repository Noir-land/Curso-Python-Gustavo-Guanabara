"""
Aluguel de carros:
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
"""


d = float(input("Quantos dias o carro foi alugado ? "))
k = float(input("Quantos Km o carro percoreu? "))
r = d * 60
r2 = k * 0.15
print("Toral a pagar \033[1;32mR$ {:.2f}".format(r + r2))
