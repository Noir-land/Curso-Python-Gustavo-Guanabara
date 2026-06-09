n = float(input("Coloque quantos metros: "))
dm = n * 10
cm = n * 100
mm = n * 1000
km = n / 1000
hm = n / 100
dam = n / 10
print("{} metros \nConvertido em centimentros é  {}cm \nConvertido em milimetros é {}mm\nConvertido em killometros {}km".format(n, cm, mm, km))
print("Decimentro:{}\nHectometro: {}\nDecametro {}".format(dm, hm, dam))
