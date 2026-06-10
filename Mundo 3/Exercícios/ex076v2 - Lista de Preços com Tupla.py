"""
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos precos,
na sequência
No final, mostre uma listagem de precos,
organizando os dados em forma tabular
"""

ListaDePreco = []

while True:
    ListaDePreco.append((input("Digite o nome do produto: ").capitalize(),
                         float(input("Digite o preço do produto: "))))
    Resposta = input('Você quer continuar? [S/N]: ').upper()
    if Resposta == 'S' or Resposta == 'SIM':
        continue
    else:
        break

print(' ')

'''for produtos in ListaDePreco:
    for produto in produtos:
        if type(produto) is str:
            print(f'{produto:.<20}', end='R$')
        else:
            print(f'{produto:9.2f}')'''

nova_ListaDePreco = ('Pão', 0.5,
                     'Queijo', 3,
                     'Bolo', 7,
                     'Pizza', 15,
                     'Refrigerante', 5,
                     'Computador', 1500)  # teorizando a entrada de uma tupla.

for i in range(0, len(nova_ListaDePreco), 2):
    nome_produto = nova_ListaDePreco[i]
    preco_produto = nova_ListaDePreco[i+1]
    ListaDePreco.append((nome_produto, preco_produto))

print('\n')

with open('lista de preço.txt', 'w', encoding='utf-8') as arquivo:
    for produto, preco in ListaDePreco:
        linha_formatada = f'{(produto):.<20}R${(preco):9.2f}'
        print(linha_formatada)
        # Salva no arquivo de texto, uma embaixo da outra
        arquivo.write(linha_formatada + '\n')
