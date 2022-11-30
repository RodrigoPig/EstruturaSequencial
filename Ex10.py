# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = (C x 1,8) + 32

c = float(input('Informe a temperatura em Celsius: '))

f = (c * 1.8) + 32

print('São {:.2f} graus Fahrenheit'.format(f))
