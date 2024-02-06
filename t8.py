#8.	Write a program that removes duplicates from a list.

x=int(input("Enter the number : "))
l=[]
for i in range(x):
    l.append(int(input("Enter the values : ")))
s=set(l)
print(list(s))