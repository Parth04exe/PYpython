n=int(input("enter a number: "))

i=10
while(i>0):
    print(f"{n} X {i}={n*i}")
    i-=1

for i in range (1,11):
    print(f"{n} X {11-i}={n*(11-i)}")