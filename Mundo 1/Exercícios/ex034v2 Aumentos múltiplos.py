"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de R$ 15%.
"""

s = float(input("Digite seu salario:"))
if s <= 1250:
    n = s + (s * 15 / 100)
else:
    n = s + (s * 10 / 100)
print(f"Seu salario antigo é R$:{s:.2f} "
      f"com o aumento agora vai ser R$:{n:.2f}")
