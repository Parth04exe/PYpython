def greatest(a,b,c):
    if(a>b and a>c):
        print("a is greater")
    elif(b>a and b>c):
        print("b is greater")
    else :
        print("c is greater")

a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))

greatest(a,b,c)