








import numpy as np
import matplotlib.pyplot as plt



def escenario():
    plt.style.use("dark_background")


CUADRADO = np.array([[0, 0],
                     [1, 0],
                     [1, 1],
                     [0, 1],
                     [0, 0]])

SEGMENTO = CUADRADO[:2]

### en 3D

ORIGIN = np.zeros(3).reshape(1, -1)
e1, e2, e3 = np.eye(3)[0].reshape(1, -1), np.eye(3)[1].reshape(1, -1), np.eye(3)[2].reshape(1, -1)

CUBO = np.vstack([ORIGIN, e1, e1+e2, e2, ORIGIN, e3, e3+e1, e3+e1+e2, e3+e2, e3, ORIGIN]).reshape(-1, 3)
