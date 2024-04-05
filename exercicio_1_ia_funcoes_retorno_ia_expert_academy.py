# 1 - Exercício - IA - Expert Academy

def leitura(mensagem):
    print(mensagem)
    valor = float(input())
    return valor


def calculo_media(v1, v2, v3):
    return (v1 + v2 + v3) / 3


def resultado(media):
    print(f'Média = {media:.2f}')
    return media


if __name__ == '__main__':
    valor1 = leitura('Digite um número: ')
    valor2 = leitura('Digite um número: ')
    valor3 = leitura('Digite um número: ')
    media = calculo_media(valor1, valor2, valor3)
    resultado(media)
