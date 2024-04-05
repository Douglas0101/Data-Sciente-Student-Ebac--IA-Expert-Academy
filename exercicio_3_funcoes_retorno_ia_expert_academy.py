# 3 - Exercício - IA Expert Academy

def leitura(mensagem):
    print(mensagem)
    numero = float(input())
    return numero


def calculo_distancia(t, v):
    return t * v


def calculo_litros(d):
    return d / 12


def resultado(d, lt):
    print(f'Distância = {d:.2f}')
    print(f'Litros = {lt:.2f}')
    return d, lt


if __name__ == '__main__':
    tempo = leitura('Digite o tempo gasto na estrada (em horas): ')
    velocidade = leitura('Digite a velocidade média percorrida: ')
    distancia = calculo_distancia(tempo, velocidade)
    litros_usados = calculo_litros(distancia)
    calculo_resultado = resultado(distancia, litros_usados)
