import numpy as np

def logistic_map(x0, r, size):
    x = np.zeros(size)
    x[0] = x0

    for i in range(1, size):
        x[i] = r * x[i-1] * (1 - x[i-1])

    return x