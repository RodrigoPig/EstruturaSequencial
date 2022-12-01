#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input('Informe a nota da primeira prova: '))
n2 = float(input('Informe a nota da segunda prova: '))
n3 = float(input('Informe a nota da terceira prova: '))
n4 = float(input('Informe a nota da quarta prova: '))

soma = (n1+n2+n3+n4)/4

print(f'A media do Bimestre é: {soma}')
