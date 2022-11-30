# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. (A = π*r²)
import math

pi = 3.14

r = float(input('Informe o raio (em metros) da circunferência: '))

raio = math.pow(r,2)

area_circulo = pi * raio
print('A area da circunferencia de raio {}m é: {}m²'.format(r,area_circulo))