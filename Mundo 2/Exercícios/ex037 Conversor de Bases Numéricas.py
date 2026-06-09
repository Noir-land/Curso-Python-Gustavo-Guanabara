''' 
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
2 para hexadecimal
'''

numero = int(input("Digite um numero inteiro: "))
con = input("Você deseja converter para:\n1 Binario\n2 Octal\n3 Hexadeimal\nQual das opções? ")

if con == '1':
    print("Para Binario é {}".format(bin(numero)[2:]))
elif con == '2':
    print("Para octal é {}".format(oct(numero)[2:]))
elif con == '2':
    print("Para Hexadecimal é {}".format(hex(numero)[2:]))
else:
    print("Opção invalida")
