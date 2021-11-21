import numpy as np
import matplotlib.pyplot as plt

# Buscando el x:
for x in range(-10, 10):
    print("Evaluando cuando x es " + str(x))
    a = (5 * ((-3 * x) - 2))-(-x - 3)
    b = -4 * ((4 * x) + 5 ) + 13

    if a == b: 
        print ("**** El valor de x es:" + str(x) + "****")

# Vista gráfica para identificar el x:
x = np.linspace(0, 9, 100)
plt.plot(
    x, (5 * ((-3 * x) - 2))-(-x - 3), 
    x, -4 * ((4 * x) + 5 ) + 13
)
plt.show()

