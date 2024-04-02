# Exercício - 2 - IA Expert Academy - Funções e Parâmetros

num_inteiro = 0


def leitura():
    global num_inteiro
    num_inteiro = int(input("Digite um número inteiro: "))


def parametros():
    if num_inteiro == 0:
        print('Zero = Nada')
    elif num_inteiro > 0:
        print('Positivo')
    else:
        print('Negativo')


if __name__ == '__main__':
    leitura()
    parametros()
