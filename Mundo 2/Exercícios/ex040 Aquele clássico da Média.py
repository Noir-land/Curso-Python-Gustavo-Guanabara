n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
res =  (n1+n2) / 2
if res <= 6.9 and res > 5:
    print("O aluno tirou {:.1f} e {:.1f}, ficando de RECUPERAÇÃO por sua media ser {:.1f}".format(n1, n2, res))
elif res > 7:
    print("O aluno tirou {:.1f} e {:.1f}, esta APROVADO sua media foi de {:.1f}".format(n1, n2, res))
elif res < 4.9:
    print("O aluno tirou {:.1f} e {:.1f}, esta REPROVADO sua media foi de {:.1f}".format(n1, n2, res))