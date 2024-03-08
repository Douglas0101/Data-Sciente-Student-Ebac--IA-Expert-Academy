# 4 - Exercício: Estruturas Condicionais - IA Expert Academy

num_1 = float(input("Insira um número: "))
num_2 = float(input("Insira outro número: "))

adicao = num_1 + num_2
subtracao = num_1 - num_2
multiplicacao = num_1 * num_2
divisao = num_1 / num_2
potencia = num_1 ** num_2

opcao = int(input("Escolha uma das seguintes opções:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - "
                  "Potência\n"))

if opcao == 1:
    print(f"Adição = {adicao:.2f}")
elif opcao == 2:
    print(f"Subtração = {subtracao:.2f}")
elif opcao == 3:
    print(f"Multiplicação = {multiplicacao:.2f}")
elif opcao == 4:
    print(f"Divisão = {divisao:.2f}")
elif opcao == 5:
    print(f"Potência = {potencia:.2f}")
else:
    print(f'Com os números {num_1:.2f} e {num_2:.2f}, a operação aritmética não foi executada!')
