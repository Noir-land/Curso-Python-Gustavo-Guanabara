peso = float(input("Quantos kg:"))
altura = float(input("Sua altura em metros: "))
resultado = peso / (altura * altura)
print(f"Seu IMC é de {resultado:.1f}")
if resultado <= 18.5:
    print("ABAIXO DO PESO")
elif resultado <= 25:
    print("PESO IDEAL")
elif resultado <= 30:
    print("SOBREPESO")
elif resultado <= 40:
    print("OBSIDADE")
else:
    print("OBESIDADE MORBIDA")
