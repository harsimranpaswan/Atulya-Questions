def sorter(list_n,y):
    if(y=="asc"):
        list_n.sort()
    elif(y=="desc"):
        list_n.sort(reverse=True)
    else:
        pass
    print(list_n)


list_n=[]
n=int(input("input length of list: "))
for i in range(0,n):
    list_n.append(int(input()))
y=input("enter the sorting parameter(asc/desc/none): ")
sorter(list_n,y)





