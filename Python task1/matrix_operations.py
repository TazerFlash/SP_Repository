import numpy as np
import sympy as sp

class operations:
    def calc_inv(x=[]):
        np.linalg.inv(x)

    def calc_det(x=[]):
        np.linalg.det(x)

    def calc_adj(x=[]):
        arr1=sp.Matrix(x)
        print("The adjoint of thee matrix is:")
        for i in range(n):
            for j in range(n):
                print(arr1[i][j],end=" ")
            print(type(arr1))
