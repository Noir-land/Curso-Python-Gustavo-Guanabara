t = float(input("Conversão de Celsius para Fahrenheit:"))
r = t*1.8+32
print("\033[1;31m{}ºC\033[m é igual a \033[1;31m{:.2f}F\033[m".format(t, r))
