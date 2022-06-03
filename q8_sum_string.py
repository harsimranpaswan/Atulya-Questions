s=input("enter any string: ")
n=0
for i in s:
    if(i.isdigit()):
        n=n+int(i)
print(n)