def inputoutput(x=[]):
    m = int(input("Number of rows:"))
    n = int(input("Number of columns:"))
    matrix = []
    print("Enter the entries row-wise:")

    for i in range(m):
        a = []
        for j in range(n):
            a.append(int(input()))
        matrix.append(a)
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()
    return n

def product(p=[],q=[]):                            #product of matrix function
    result=[[0,0,0,],[0,0,0],[0,0,0]]
    for i in range(len(p)):
        for j in range(len(q[0])):
           for k in range(len(q)):
              result[i][j] += p[i][k] * q[k][j]
    print("The Resultant Matrix Is ::>")
    for r in result:
       print(r)

def transpose(p=[],q=[]):                           #transpose of matrix
    transpose=[[0,0,0],[0,0,0],[0,0,0]]
    print("The transpose of matrix is:")
    for i in range(len(p)):
        for j in range(len(q[0])):
            transpose[j][i]=p[i][j]
    for r in transpose:
        print(r)

a=[]
inputoutput(a)
b=[]
inputoutput(b)

product(a,b)

print("the transpose of first matrix is")
transpose(a)
print("The transpose of second matrix is")
transpose(b)