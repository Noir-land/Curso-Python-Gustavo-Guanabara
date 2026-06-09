import math
num = float(input("Coloque um numero que deseja saber os angulos: "))
r1 = math.cos(math.radians(num))
r2 = math.tan(math.radians(num))
r3 = math.sin(math.radians(num))
print("O cosseno é {:.2f}\nA tangente é {:.2f}\nO Seno é {:.2f}".format(r1, r2, r3))

