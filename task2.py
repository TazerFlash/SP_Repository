def entertpl(a=[]):
 n = int(input("Enter number of elements"))

 for i in range(n):
     a.append(input("Enter element:"))

 print("The tuple is:")
 for element in a:
     print(element)

 return n

def sum(n,a=[]):
    for x in range(n):
     while a[x] =! 0:
         for i in range(size(a)):
            x=a[i]
            y=a[i+1]
            z=x+y
     print("The sum of the tuple elements is:",z)
     return z


a=[]
entertpl(a)

a=tuple(a)

result = tuple(set(a))
for r in result:
    print(r)

sum(n,a)




