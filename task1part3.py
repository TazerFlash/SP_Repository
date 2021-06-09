
def product(A, B, Ca, Rb):
    AB = [[0] * Ca for n in range(Rb)]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                AB[i][j] += A[i][k] * B[k][j]
    return AB


def transpose(C, Rc, Cc):
    Ctran = [[0] * Rc for n in range(Cc)]
    for i in range(len(C)):
        for j in range(len(C[0])):
            Ctran[j][i] = C[i][j]
    return Ctran


A, B, dim = [], [], []
dim = [int(x) for x in input("Enter the rows and columns:\n").split()]
print("Enter the values of matrix A:\n")
for i in range(dim[0]):
    a = []
    for j in range(dim[1]):
        a.append(int(input()))
    A.append(a)
print("Enter the values of matrix B:\n")
for i in range(dim[2]):
    b = []
    for j in range(dim[3]):
        b.append(int(input()))
    B.append(b)

# Printing the two matrices
print("Your two matrices are:\n")
for i in range(dim[0]):
    for j in range(dim[1]):
        print(A[i][j], end=" ")
    print()
print("\n")
for i in range(dim[2]):
    for j in range(dim[3]):
        print(B[i][j], end=" ")
    print()

print("Since {} = {}, we can say that (AB)T = (BT)(AT).")