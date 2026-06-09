n = s = cont = 0
n = int(input("Digite um numero.[999 para parar]"))
while n != 999:
    s += n
    cont += 1
    n = int(input("Digite um numero.[999 para parar]"))
print(f"fim {s}")
print(f"{cont}")
