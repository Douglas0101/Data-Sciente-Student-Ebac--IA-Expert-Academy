tempo = 0
velocidade = 0
distancia = 0
litros = 0


def leitura():
    global tempo
    global velocidade
    tempo = float(input('Insira o tempo gasto na viagem (em horas): '))
    velocidade = float(input('Insira a velocidade média (km/h): '))


def calculo_distancia():
    global distancia
    distancia = velocidade * tempo


def calculo_litros():
    global litros
    litros = distancia / 12


def resultado():
    print(f'A distância percorrida foi de {distancia:.2f} km')
    print(f'Foram gastos {litros:.2f} litros de combustível')


leitura()
calculo_distancia()
calculo_litros()
resultado()
