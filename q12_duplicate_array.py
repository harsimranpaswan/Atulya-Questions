import random
n=[]

for i in range(0,100):
    n.append(random.randint(1,99))

print(n)
count=0
for i in range(0,100):
    for j in range(i+1,100):
        if(n[i]==n[j]):
            print(n[i])
            count+=1
            break
    if(count!=0):
        break 