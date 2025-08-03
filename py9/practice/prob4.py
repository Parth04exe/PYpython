def sum (n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return n+sum(n-1)
n=int(input("enter a number: "))
print(f"The factorial of this number is : {sum(n)}")
