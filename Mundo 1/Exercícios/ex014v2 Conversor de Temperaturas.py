"""
Conversor de temperaturas: escreva um programa 
que converta uma temperatura digitada em ºC para ºF
"""

t = float(input("Converter Fahrenheit para Celsius: "))
r = (t-32) * 5 / 9
print("\033[1;31m{}ºF\033[m é convertido para \033[1;31m{:.2f}ºC".format(t, r))
