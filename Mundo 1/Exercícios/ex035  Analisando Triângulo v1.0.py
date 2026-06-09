a = float(input("Primeira reta: "))
b = float(input("Segunda  reta: "))
c = float(input("Terceira reta: "))
if a < b + c and b < a + c and c < a + b:
    print(f"E possivel fazer um triangulo")
else:
    print("não é possivel fazer um tringulo")
