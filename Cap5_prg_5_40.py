import numpy as np

notas = np.array([5, 9, 5.5, 10, 8])
pesos = np.array([1, 2, 4, 1, 2])

media = np.average(notas, weights=pesos)
print('média = ', media)