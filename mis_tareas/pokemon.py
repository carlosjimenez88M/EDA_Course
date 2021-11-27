import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pokemon = pd.read_csv('C:/Users/gloza/Downloads/Pokemon.csv')
nombre_pokemon = pokemon['name']
poder = pokemon['hp']
print('en promedio un pokemo tiene un poder de', round(poder.mean(),0))
for i,j in zip(nombre_pokemon, poder):
    poder_avg = poder.mean()
    if j > poder_avg:
        print(' {} es el pokemon con fuerza superior al promedio, su fuerza es de   {}'.format(i,j))
    elif j < poder_avg:
        print(' {} es el pokemon con fuerza menor al promedio, su fuerza es de {}'.format(i,j))