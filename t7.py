# 7.	Create a function that takes a string as input and returns a dictionary containing the count of each character in the string.

x = input("Enter a string : ")
y=x.lower()
s = set(y)
d={}
for i in s:
    if i not in ". ":
        d[i]=y.count(i)
print(d)