import numpy as np
import sympy as sp
from matrix_operations import operations

def inputmatrix(z,x=[]):
    for i in range(z):
        y=[]
        for j in range(z):
           val=int(input("Enter a number"))
           y.append(val)
        x.append(y)

def numpymatrix(x=[]):
    arr=np.array(x)
    for i in range(n):
        for j in range(n):
           print(arr[i][j], end=" ")
    print(type(arr))

def multiply(n,p,a = [],b = []):
    result=[[0] * n for f in range(p)]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] = result[i][j] + a[i][k] * b[k][j]

    print("The resultant matrix is:")
    for i in range(m):
        for j in range(n):
            print(result[i][j],end=" ")
        print()
    return result

a=[]
n=int(input("Enter number of rows and columns for the square matrix A"))
inputmatrix(n,a)
numpymatrix(a)
b=[]
p=int(input("Enter number of rows and columns for the square matrix B"))
inputmatrix(p,b)
numpymatrix(b)

operations.calc_inv(b)
multiply(n,p,a,b)

operations.calc_inv(a)
multiply(n,p,a,b)



