#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
import math

ladoDoQuadrado = float(input('Informe o valor (em metros) do lado de um quadrado: '))

area_quadrado = math.pow(ladoDoQuadrado,2)
area_dobrada =area_quadrado * 2

print(f'A area do quadrado é {area_quadrado} e o seu dobro é {area_dobrada}')