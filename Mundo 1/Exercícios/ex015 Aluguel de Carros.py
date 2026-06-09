d = float(input("Quantos dias o carro foi alugado ? "))
k = float(input("Quantos Km o carro percoreu? "))
r = d * 60
r2 = k * 0.15
print("Toral a pagar \033[1;32mR$ {:.2f}".format(r + r2))
