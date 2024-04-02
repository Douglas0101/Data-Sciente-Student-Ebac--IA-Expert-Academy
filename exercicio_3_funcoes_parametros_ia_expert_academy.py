# Exercício 3 - IA Expert Academy

idade = 0


def leitura_idade():
    global idade
    idade = int(input('Insira sua idade: '))


def verificar_idade():
    if idade >= 0 and idade <= 12:
        print('Criança')
    elif idade > 12 and idade <= 17:
        print('Adolescente')
    else:
        print('Adulto')


if __name__ == '__main__':
    leitura_idade()
    verificar_idade()
