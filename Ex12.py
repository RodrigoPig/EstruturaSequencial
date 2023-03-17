# Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

while altura == float:
    try:
        altura = float(input('Informe a sua altura Ex(1.80): '))
        peso = (72.2*altura)-58

        print(f'Seu pesso ideal é: {peso:.2f}')
        break
    except ValueError:
        print('O formato informado não é valido')
        print('Por Favor siga o exemplo (1.80)')