def inputmatrix(x,y,z = []):
    for i in range(x):
        c = []
        for j in range(y):
            j = int(input("Ënter number in index"+str(i)+" "+str(j)+" "))
            c.append(j)
        print()
        z.append(c)

    print("The entered matrix is:")
    for i in range(x):
       for j in range(y):
            print(z[i][j],end=" ")
       print()

    return(n)

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

def transpose(h, l, g=[]):
    trans = [[0] * h for f in range(l)]
    for i in range(h):
        for j in range(l):
            trans[j][i] = g[i][j]

    for i in range(h):
        for j in range(l):
            print(trans[i][j], end=" ")
        print()
    return trans


a=[]
print("For first matrix")
m = int(input("Enter number of rows"))
n = int(input("Enter number of columns"))
inputmatrix(m,n,a)

b=[]
print("For second matrix")
p = int(input("Enter number of rows"))
q = int(input("Enter number of columns"))
inputmatrix(p,q,b)

multiply(n,p,a,b)

print("The transpose of first matrix is")
transpose(m,n,a)

print("The transpose of second matrix is")
transpose(p,q,b)

transpose(m,n,result)

print(transpose(m,n,result)," = ", transpose(m,n,a)," * ", transpose(p,q,b))

print("Hence, (AB)T = BT * AT")








