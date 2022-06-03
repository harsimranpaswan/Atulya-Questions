import math

def calc_auto(z):
    print(eval(z))

def calc(x,o,y):
    if(o=='*'):
        print(x*y)
    elif(o=='/'):
        print(x/y)
    elif(o=='+'):
        print(x+y)
    elif(o=='-'):
        print(x-y)
    else:
        print("invalid")

mode=input("chhose mode(auto/manual): ")
if(mode=="auto"):
    z=input("enter the expression: ")
    calc_auto(z)
elif(mode=="manual"):
    x=float(input("first number: "))
    o=input("operator")
    y=float(input("second number"))
    calc(x,o,y)
else:
    print("invalid")
