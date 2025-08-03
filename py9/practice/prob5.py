def stars(n):
    if(n==0):
        return
    print("*" * n)
    stars(n-1)
n=int(input("enter a number: "))
stars(n)