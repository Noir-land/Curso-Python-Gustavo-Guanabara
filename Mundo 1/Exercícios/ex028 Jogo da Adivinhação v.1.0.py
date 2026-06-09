import random
from time import sleep
p = int(input("Digite um numero de 1 a 5: "))
r = random.randint(1, 5)
print('PROCESSANDO....')
sleep(1)
print("O numero é {}".format(r))
if p == r:
    print("Parabens você acertou.")
else:
    print("Boa sorte na proxima.")
