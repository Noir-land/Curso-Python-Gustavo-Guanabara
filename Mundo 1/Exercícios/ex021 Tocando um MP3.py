import pygame

n = (input("Pressione qualquer [SIM] par executar a musica: ")).upper()
if n == "SIM":
    print("Tocando musica")
    pygame.mixer.init()
    pygame.mixer.music.load(
        'D:\VsCode\PycharmProjects\Curso em video\Exercicios\ex021.mp3')
    pygame.mixer.music.play()
    input()
else:
    print("Tenha um bom dia.")
print("Musica finalizada")
