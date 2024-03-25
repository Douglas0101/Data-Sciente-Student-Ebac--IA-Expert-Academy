# 5 - Exercício - IA Expert Academy

comprimento = 0
largura = 0
altura = 0
continuar = 'sim'

while True:
    comprimento = float(input('Digite o comprimento: '))
    largura = float(input('Digite a largura: '))
    altura = float(input('Digite a altura: '))

    volume = comprimento * largura * altura
    print(f'Volume: {volume:.2f}')

    continuar = input('Deseja continuar?, sim ou não: ')

    if continuar == 'sim':
        continue
    else:
        break
