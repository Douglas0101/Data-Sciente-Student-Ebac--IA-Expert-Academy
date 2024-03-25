import numpy as np

v_Nomes = np.array(["João", "Maria", "Pedro", "Ana", "Lucas", "Carla", "Lara", "Julia", "Vitoria", "Isabela"])

v_Notas = np.array([1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00])

v_Notas_rounded = np.round(v_Notas, 2)

for i in range(len(v_Notas)):
    nota = float(input(f'Insira nota de {v_Nomes[i]}: '))
    v_Notas[i] = float(nota)

print('-' * 100)

for i in range(len(v_Notas)):
    print(f'Nome: {v_Nomes[i]} | Nota: {v_Notas_rounded[i]}')
