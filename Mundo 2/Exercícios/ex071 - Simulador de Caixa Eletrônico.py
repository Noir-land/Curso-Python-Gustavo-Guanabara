sacar = int(input("Quanto deseja sacar ? R$:"))
total = sacar
nota = 50
cont = 0
while True:
    if total >= nota:
        total -= nota
        cont += 1
    else:
        if cont > 0:
            print(f"total de {cont} de notas de R$ {nota}")
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        cont = 0
        if total == 0:
            break
