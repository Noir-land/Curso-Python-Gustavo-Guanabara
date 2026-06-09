ini = int(input("Digite o primeiro termo: "))
raz = int(input("Razão: "))
dt = ini + (10-1) * raz
for c in range(ini, dt+raz, raz):
    print(f"{c}", end=">>")
print("Acabou")
