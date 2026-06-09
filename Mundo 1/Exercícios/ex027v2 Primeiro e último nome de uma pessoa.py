nome = str(input("Digite seu nome:")).strip().split()
print("Seu primeiro nome é {}".format(nome[0]))
print(f"Seu ultimo nome é {nome[len(nome)-1]}")
