# 2 - Exercício Booleano - IA Expert Academy

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
potencia = num1 ** num2

a = print('Adição')
s = print('Subtração')
m = print('Multiplicação')
d = print('Divisão')
p = print('Potência')

escolha = input('Escolha a operação aritmética: ')

if escolha == 'a':
    print(f'Soma = {num1:.2f} + {num2:.2f} = {soma:.2f}')
elif escolha == 's':
    print(f'Subtracao = {num1:.2f} - {num2:.2f} = {subtracao:.2f}')
elif escolha == 'm':
    print(f'Multiplicação = {num1:.2f} * {num2:.2f} = {multiplicacao:.2f}')
elif escolha == 'd':
    print(f'Divisão = {num1:.2f} / {num2:.2f} = {divisao:.2f}')
elif escolha == 'p':
    print(f'Potência = {num1:.2f} ** {num2:.2f} = {potencia:.2f}')
