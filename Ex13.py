# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = str(input('Informe o seu sexo (F)Feminino (M)Masculino: ')).upper()
altura = float(input('Informe a sua altura: '))


if sexo == 'M':
    
    peso = (72.7*altura) - 58
    print(f'O peso ideal para homens de altura {altura} é: {peso:.2f} Kg')
        
elif sexo == 'F':
    peso = (62.1*altura) - 44.7
    print(f'O peso ideal para mulheres de altura {altura} é: {peso:.2f} Kg')
else:
    print('Sexo não informado corretamente')
  
