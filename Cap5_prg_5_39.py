import numpy as np

notas = np.array([5, 9, 5.5, 10, 8])
pesos = np.array([1, 2, 4, 1, 2])

notas_ponderadas = notas * pesos
media = np.sum(notas_ponderadas)/np.sum(pesos)
print('Média = ', media)