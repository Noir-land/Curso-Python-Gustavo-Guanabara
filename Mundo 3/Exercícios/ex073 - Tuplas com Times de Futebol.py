"""
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro,
na ordem de colocação.
Depois mostre:
apenas os 5 primeiros colocados
os últimos 4 colocados da tabela
uma lista com os times em ordem alfabética
em que posição na tabela está o time da Chapecoense
"""

times = ('São Paulo', 'Internacional', 'Atlético-MG', 'Grêmio', 'Flamengo', 'Palmeiras',
         'Fluminense', 'Corinthians', 'Santos', 'Ceará', 'Athletico-PR', 'Atlético-GO',
         'Bragantino', 'Sport', 'Vasco', 'Fortaleza', 'Bahia', 'Goiás', 'Botafogo', 'Coritiba')
print(times)
print("_-"*50, "|")
print(f"Os 5 primeiros são {times[0:6]}")
print("_-"*50, "|")
print(f"Os quatro ultimos são {times[16:]}")
print("_-"*50, "|")
o = sorted(times)
print(f"A lista de forma ordenada é {o}")
print("_-"*50, "|")
print(f"O Coritiba esta na possição {times.index('Coritiba')+1}")
