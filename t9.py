# 9. Create a function that takes a list of strings as input and returns a set containing unique words across all the strings.
n=int(input("Enter size of list : "))
l=[]
for i in range(n):
    l.append(input("Enter the string : "))
def func(m):
    s=set()
    for i in m:
        for x in i:
            s.add(x)
    print(s)
func(l)