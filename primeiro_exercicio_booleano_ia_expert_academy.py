# 1 - Exercício Booleano - IA Expert Academy

letra = input(str('Digite uma letra: '))

if (
        letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or letra == 'A' or letra == 'E' or
        letra == 'I' or letra == 'O' or letra == 'U'
):
    print('Essa letra é uma vogal.')

else:
    print('Essa letra é uma consoante.')
