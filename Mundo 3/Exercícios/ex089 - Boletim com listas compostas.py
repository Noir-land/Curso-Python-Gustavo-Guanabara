

from time import sleep
estudantes = list()
temp = list()
while True:
    nome = str(input('Nome do aluno: ').strip().capitalize())
    temp.append(nome)
    if len(estudantes) == 0:
        estudantes.append([])
        estudantes.append([])
    estudantes[0].append(temp[:])
    temp.clear()
    for n in range(1, 3):
        nota = float(input(f'{n}º nota: '))
        temp.append(nota)
    estudantes[1].append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? ').strip().capitalize())
    if resp == 'N':
        break
print('-'*30)
print(F'Nº.{"NOME":^18}{"NOTA"}')
print('-'*30)
contador = 0
for linha in range(1):
    for coluna in range(len(estudantes)):
        for n, estudante in enumerate(estudantes):
            media = 0
            if n % 2 == 0:
                print(f'Nº {contador}.', end=' '*5)
                contador += 1
                for aluno in estudante[coluna]:
                    print(f'{aluno:<5}', end=' '*6)
            if n % 2 == 1:
                for nota in estudante[coluna]:
                    media += nota
                print(f'{media/2:<5}')
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
                break
    if resp != 999 and resp > contador:
        print('Invalido!')
        print(f'Digite de 0 a {contador-1}')
    if resp == 999:
        for loop in range(1, 4):
            print('Finalizando', end='')
            print('.'*loop)
            sleep(0.5)
        break
print('Tenha um bom dia.')
