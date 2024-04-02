C = 0
F = 0


def leitura():
    global C
    C = float(input('Insira a temperatura em graus Celsius: '))


def conversao():
    global F
    F = (9 * C + 160) / 5


def resultado():
    print(f'A temperatura em Celsius é {C}, convertido para Fahrenheit = {F}')


leitura()
conversao()
resultado()
