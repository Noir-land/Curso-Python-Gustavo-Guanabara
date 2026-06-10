estudantes = [[], []]
temp = list()
while True:
    nome = str(input('Nome do aluno: ').strip().capitalize())
    temp.append(nome)
    estudantes[0].append(temp[:])
    temp.clear()
    nota = float(input('1º nota: '))
    temp.append(nota)
    nota = float(input('2º nota: '))
    temp.append(nota)
    estudantes[1].append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? ').strip().capitalize())
    if resp == 'N':
        break
print('-'*30)
print(F'Nº.    NOME    NOTA')
print('-'*30)
contador = 0
for linha in range(1):
    for coluna in range(len(estudantes)):
        for n, estudante in enumerate(estudantes):
            media = 0
            if n % 2 == 0:
                print(f'{contador}', end=' ')
                contador += 1
                for aluno in estudante[coluna]:
                    print(f'{aluno}', end=' ')
            if n % 2 == 1:
                for nota in estudante[coluna]:
                    media += nota
                print(media/2)
print('-'*30)
while True:
    resp = int(
        input('\nDeseja ver a nota de qual aluno? [999 para finalizar] '))
    if resp <= contador-1:
        print('As notas do estudante ', end='')
        for n, estudante in enumerate(estudantes):
            for aluno in estudante[resp]:
                if n % 2 == 0:
                    print(f'"{aluno}". ', end='')
            if n % 2 == 1:
                print(f'Foram: {estudante[resp]}')
    if resp == 999:
        break
