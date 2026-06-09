s = float(input("Digite seu salario:"))
if s <= 1250:
    n = s + (s * 15 / 100)
else:
    n = s + (s * 10 / 100)
print(f"Seu salario antigo é R$:{s:.2f} "
      f"com o aumento agora vai ser R$:{n:.2f}")
