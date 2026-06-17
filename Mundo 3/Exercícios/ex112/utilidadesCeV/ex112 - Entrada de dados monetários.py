"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), 
mas com uma validação de dados para aceitar apenas valores que sejam monetários.
"""


from utilitariosCV.dados import leia_dinheiro
from utilitariosCV.Moeda import resumo

valor = leia_dinheiro('Digite um valor: ')
resumo(valor, 80, 35)
