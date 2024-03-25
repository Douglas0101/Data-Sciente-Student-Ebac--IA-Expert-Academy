# 3 - Exercício - For Ia Expert Academy

negativos = 0

for contador in range(5):
    contador += 1
    a = float(input(f'Digite o {contador}° valor de A: '))

    negativos = negativos + 1 if a < 0 else negativos

print(f'Foram digitados {negativos} valores negativos.')
