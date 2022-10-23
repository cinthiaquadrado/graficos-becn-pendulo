import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([0.1, 0.15, 0.22, 0.3, 0.35, 0.4, 0.46]) #comprimento
y1 = np.array([6.39, 7.62, 9.24, 10.94, 11.62, 12, 13.51]) #período

plt.figure(figsize=(10, 6))
plt.xlabel('\nComprimento (m)', fontsize=14)
plt.ylabel('Período (s)\n', fontsize=14)
plt.grid(True)
plt.title('Período por comprimento\n', fontsize=20)
#plt.savefig('periodo-comprimento.png')

plt.plot(x1, y1, '-')
plt.show()

x2 = np.array([0.1, 0.15, 0.22, 0.3, 0.35, 0.4, 0.46]) #comprimento
y2 = np.array([9.6, 10.24, 10.25, 9.95, 10.25, 10.95, 10.73]) #gravidade

plt.figure(figsize=(10, 6))
plt.xlabel('\nComprimento (m)', fontsize=14)
plt.ylabel('Aceleração da gravidade (m/s²)\n', fontsize=14)
plt.grid(True)
plt.title('Aceleração da gravidade por comprimento\n', fontsize=20)
#plt.savefig('gravidade-comprimento.png')

plt.plot(x2, y2, '-')
plt.show()

x3 = np.array([5, 10, 15, 20, 25, 30, 35]) #ângulo
y3 = np.array([9.11, 9.7, 10.1, 9.5, 9.5, 9.3, 9.2]) #gravidade

plt.figure(figsize=(10, 6))
plt.xlabel('\nÂngulo (graus)', fontsize=14)
plt.ylabel('Gravidade (m/s²)\n', fontsize=14)
plt.grid(True)
plt.title('Aceleração da gravidade por ângulo θ\n', fontsize=20)
#plt.savefig('gravidade-angulo.png')

plt.plot(x3, y3, '-')
plt.show()
