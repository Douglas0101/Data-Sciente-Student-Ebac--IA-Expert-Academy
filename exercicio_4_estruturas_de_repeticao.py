# 4 - Exercício - IA Expert Academy

nota_1 = -1.0
nota_2 = 12.0

while nota_1 < 0 or nota_1 > 10:
    nota_1 = int(input("Insira a primeira nota: "))

while nota_2 < 0 or nota_2 > 10:
    nota_2 = int(input("Insira a segunda nota: "))

media = (nota_1 + nota_2) / 2
print(f'A média é {media:.2f}')
