# 1 - Exercício - IA Expert Academy

comprimento = 0.0
largura = 0.0
altura = 0.0
volume = 0.0


def leitura():
    global comprimento
    global largura
    global altura
    comprimento = float(input("Comprimento: "))
    largura = float(input("Largura: "))
    altura = float(input("Altura: "))


def calcula_volume(c, l, a):
    global volume
    volume = c * l * a


def resultado(v):
    print(f"O volume da sua caixa e de {v:.2f}m³ ou litros.")


if __name__ == "__main__":
    leitura()
    calcula_volume(comprimento, largura, altura)
    resultado(volume)
