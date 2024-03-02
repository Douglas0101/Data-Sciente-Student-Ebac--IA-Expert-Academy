# Exercício 4: Ia Expert Academy

distancia = float(input("Qual a distância percorrida: "))
tempo_gasto = int(input("Qual o tempo gasto(em minutos): "))
velocidade_media = float(input("Qual a velocidade média: "))

distancia = (tempo_gasto * velocidade_media)

litros_usados = distancia / 12
print(f"Foi consumido {litros_usados:.2f} litros")
