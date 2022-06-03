n=int(input("enter the range: "))
count=0
for i in range(1,n):
    for j in range(1,n):
        if(i%j==0):
            count+=1
    if(count==2):
        print(i)
    count=0