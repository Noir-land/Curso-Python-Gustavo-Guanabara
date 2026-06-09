import random
from time import sleep
print('''Eu, Ultron lhe chamo para jogar um jogo....
Pensarei em um numero de 0 a 10 e veremos em quantas chances podera acerta.
Que os jogos comecem.MUHAHAHAHA''')
num = int(input("Qual o seu palpite? "))
ultron = random.randint(0, 5)
chances = 1
print("PROCESSANDO...")
sleep(0.5)
while num != ultron:
    print("Voce errou, patetico.")
    sleep(0.5)
    print("CARRENDO NOVA TENTATIVA....")
    sleep(0.5)
    num = int(input("Tente outro numero: "))
    chances += 1
sleep(0.5)
print("PARABENS!!!")
print(f"Voce acertou e so precisou de {chances} tentativas")
