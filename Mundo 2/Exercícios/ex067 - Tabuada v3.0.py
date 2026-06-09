con = 1
while True:
    num = int(input("Digite o numero da Tabuada"))
    print("~" * 15)
    con = 0  # resetar ou atribuir novo valor para a contagem
    if num > 0:
        while con <= 9:
            con += 1
            print(f'{num} x {con} = {num * con}')
        print("~" * 15)
    else:
        break
print('VOLTE SEMPRE.')
