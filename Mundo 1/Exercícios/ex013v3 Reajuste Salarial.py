s = float(input("Digite o seu salario: R$ "))
p = float(input("Digite a % para aplicar visualizar o novo salario: "))
print("Seu salario é de {} com o reajuste de {}% é igual a {}".format(s, p, (p/100*s+s)))
