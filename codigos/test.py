from Lab_6 import lu, soltrinf, soltrsup, soleg
import numpy as np

if __name__ == "__main__":
    A = np.array([[2, -2, 1], [1, 1, 3], [0, 4, 1]])
    # b = np.array([-1, 6, 9])
    # b = np.array([-2, 1, 3])
    b = np.array([-10, 4, 8])
    L, U = lu(A)
    y = soltrinf(L, b)
    x = soltrsup(U, y)
    print(y)
    print(x)
    xeg = soleg(A, b)
    print(xeg)
