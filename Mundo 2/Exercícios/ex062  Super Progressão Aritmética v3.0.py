"""
Melhore o exercício 61, perguntando para o usuário
se ele quer mostrar mais alguns termos
O programa encerra quando ele disser que quer mostrar "0 termos"
"""

pri = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão da PA: "))
termo = pri
cont = 1
t = 0
mais = 10
while mais != 0:
    t += mais  # contador de limite
    while cont <= t:
        print(f"{termo} >", end=" ")
        termo += raz
        cont += 1
    print("FIM")
    mais = int(input("Mais quantos quer mostrar? "))
print(f"foram {t} termos")
