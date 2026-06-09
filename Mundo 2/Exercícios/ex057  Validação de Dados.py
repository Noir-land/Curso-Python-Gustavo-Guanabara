sex = str(input("Digite seu sexo: ")).upper().strip()[0]
while sex not in "MnFf":  # QUANDO TEM " "MnFf" É FINALIZADO O LOOP ou QUANDO A AFIRMAÇÃO SE TORNA FALSA
    sex = str(input("Digite seu sexo corretamente: ")).upper().strip()[0]
if sex == 'M':
    sex = 'Masculino'
elif sex == 'F':
    sex = 'Feminino'
else:
    Exception
    'error'
print(f"Parabens, o sexo {sex} foi registrado com sucesso")
