frase = str(input("Digite uma frase: ")).strip().upper()
dividir = frase.split()
junto = ''.join(dividir)
inverso = ''
for letras in range(len(junto)-1, -1, -1):
    inverso += junto[letras]
if inverso == junto:
    print("TEMOS UM POLINDRAMO")
else:
    print("NÃO É UM POLINDRAMO")
