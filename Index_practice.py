import numpy as np

temps = np.array([32,13,8,34,23,3,30,1,21,29])
hot_temps = temps[temps > 30]
hot_temps_indices = np.where(temps > 30)[0] 
temps = np.where(temps < 10, 10, temps)
print(temps)
print(f'Temps above 30: {hot_temps}')
print(hot_temps_indices)
