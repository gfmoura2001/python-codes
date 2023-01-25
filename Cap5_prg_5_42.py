import numpy as np

notas = np.array([5, 9, 5.5, 10, 8.4])
print(notas > 6)
print('notas > 6: ', notas[notas > 6])
print('notas <=6: ', notas[notas <= 6])