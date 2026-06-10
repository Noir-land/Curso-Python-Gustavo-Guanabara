

estudantes = list()
while True:
    nome = str(input('Nome: ').strip().capitalize())
    nota1 = float(input('1º nota: '))
    nota2 = float(input('2º nota: '))
    media = (nota1 + nota2) / 2
    estudantes.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar?[S/N] ').strip().capitalize())
    if resp in 'Nn':
        break
print('/\/'*10)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
print('==='*10)
for n, aluno in enumerate(estudantes):
    print(f'{n:<4}{aluno[0]:<10}{aluno[2]:>8}')
    print('___'*10)
while True:
    resp = int(input('Digite o Nº correspondente ao aluno. 999 para finalizar. '))
    if resp == 999:
        break
    if resp < len(estudantes) - 1:
        print(f'As notas do aluno {estudantes[resp][0]} '
              f'foram: {estudantes[resp][1]}')
