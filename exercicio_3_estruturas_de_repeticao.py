#3 - Exercício - IA Expert Academy

contador = 1
var_a = 0
var_negativo = 0

while contador <= 5:

    var_a = float(input("Digite o valor de A: "))
    if var_a < 0:
        var_negativo = var_negativo + 1
    contador = contador + 1

print(f'Existem {var_negativo} valor(es) negativos!.')
