# 2 - Exercício - IA Expert Academy

def leitura(mensagem):
    print(mensagem)
    valor = int(input())
    return valor


def comparativo(num_inteiro):
    if num_inteiro < 0:
        return False
    else:
        return True


if __name__ == '__main__':
    num_inteiro = leitura('Digite um número inteiro: ')
    resultado = comparativo(num_inteiro)
    print(resultado)
