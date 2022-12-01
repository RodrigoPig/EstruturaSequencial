# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

valorPorHora = float(input('Informe o valor que voce recebe por hora tabalhada: '))
horasTrabaladas = float(input('Informe o numero de horas trabalhadas por mês: '))

salario = valorPorHora * horasTrabaladas

print(f'Seu salário é: {salario}')