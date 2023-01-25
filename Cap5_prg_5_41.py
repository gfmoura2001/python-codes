import numpy as np

notas_e_pesos = np.array([[5, 9, 5.5, 10, 8],[1, 2, 4, 1, 2]])

media = np.average(notas_e_pesos[0], weights=notas_e_pesos[1,:])
print('média = ', media)