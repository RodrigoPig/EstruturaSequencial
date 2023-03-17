#Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre: 
# A- o produto do dobro do primeiro com metade do segundo .
# B- a soma do triplo do primeiro com o terceiro.
# C- o terceiro elevado ao cubo.


while True:
    try:
        n1 = int(input(' Informe um numero inteiro: '))
        n2 = int(input(' Informe um numero inteiro: '))
        n3 = float(input('Informe um numero real: '))
        a = (n1*2) + (n2/2)
        b = (n1*3) + n3
        c = n3**3
        print(f'O produto do dobro do primeiro com metade do segundo é: {a}')
        print(f'A soma do triplo do primeiro com o terceiro é: {b}')
        print(f'O terceiro elevado ao cub é: {c:.3f}')
        break
        
    except ValueError:
        print('Os numeros informados não atendem o requisito informado')
        
   




