def duplicate(tpl):
   print("The list of tuple is : ")
   print(tpl)

   tpl1 = list(set([i for i in tpl]))
   print("The list of tuples after removing duplicates is :")
   print(tpl1)

   return tpl1

def sum(tpl):
    print(sum(tpl1))

a = input("Provide a sequence of numbers separated by commas: ")

list = a.split(",")
tpl = tuple(list)

print(f"\nThis is a printed list of the number values: ")
print(f"\t{list} ")
print("\nThis is a printed tuple of the number values: ")
print(f"\t{tpl} ")

duplicate(tpl)
sum(tpl)