d = int(input("Distancia a percorrer em Km: "))
p = d * 0.50
p2 = d * 0.45
if d <= 200:
    print("Valor a pagar R$:{}".format(p))
else:
    print("O valor a pagar é {}".format(p2))
