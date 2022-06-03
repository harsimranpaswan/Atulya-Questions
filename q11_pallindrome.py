s=input("input any string: ")
z=''
for i in s:
    z=i+z
if(s==z):
    print("pallindrome")
else:
    print("not a pallindrome")