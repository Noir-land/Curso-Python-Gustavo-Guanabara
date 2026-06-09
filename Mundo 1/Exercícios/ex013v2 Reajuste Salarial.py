p = float(input("Coloque o numero referente a % para o aumento:"))
s = float(input('Digite seu salario atual:R$ '))
r = p/100*s
r2 = s+r
print("Seu salario de {} com aumento de {} é correspondente a {:.2f} com aumento de {:.2f}".format(s, p, r2, r))
