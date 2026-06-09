s = 0
con = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c  # OU s += c
        con = con + 1  # OU con += 1
print(f"A soma de todos os {con} é igual a {s}")
