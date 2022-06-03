import random
n=[]
k=int(input("enter the length of array: "))
for i in range(0,k):
    n.append(random.randint(1,99))

print(n)
count=0
max=0
val=0
for i in range(0,k):
    for j in range(0,k):
        if(n[i]==n[j]):
            count+=1
    if(count>max):
        max=count
        val=n[i]
    count=0
print(val,"repeated",max,"times")