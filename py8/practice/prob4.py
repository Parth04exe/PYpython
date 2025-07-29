num=int(input("enter the number: "))
count=0
for i in range (1,num):
    if(num%i==0):
        count+=1
if(count==1):
    print("prime")
else:
    print("not prime")