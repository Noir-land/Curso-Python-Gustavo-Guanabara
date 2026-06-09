"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos
"""


maior_de_18 = homens = mulheres = 0
opção = sexo = " "
while True:
    print("||"*20)
    print("CADASTRE UM NOME.".center(40))
    print("||" * 20)
    idade = int(input("IDADE: "))
    nome = str(input("NOME: "))
    sexo = str(input("SEXO:(F/M) ")).strip().upper()
    opção = str(input("DESEJA CONTINUAR ? (S/N)")).strip().upper()[0]
    if idade >= 18:
        maior_de_18 += 1
    if sexo in "M":
        homens += 1
    if sexo in "F" and idade < 20:
        mulheres += 1
    if opção == "N":
        break
print("||"*20)
print(f"Existem {maior_de_18} pessoas com mais de 18 anos.\nExistem {homens} homens no grupo no grupo.\nExistem {mulheres} mulheres com menos de 20 anos ")
print("||"*20)
