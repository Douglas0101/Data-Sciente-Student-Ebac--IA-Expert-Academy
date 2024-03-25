import numpy

vetor_A = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for i in range(len(vetor_A)):
    valor = int(input("Digite um valor: "))
    vetor_A[i] = valor

pesquisa = int(input("Digite o valor que deseja pesquisar: "))

if pesquisa in vetor_A:
    for i in range(len(vetor_A)):
        if pesquisa == vetor_A[i]:
            print(f'O valor {pesquisa} foi encontrado na posição {i + 1}')
else:
    print("O valor não foi encontrado")