# 12.	Create a function that calculates the total length of strings in a list.
n=int(input("Enter the size of list : "))
l=[]

for i in range(n):
    l.append(input("Enter the string : "))
def func(m):
    for i in m:
        print("Length of {i} is : ",len(i))
func(l)