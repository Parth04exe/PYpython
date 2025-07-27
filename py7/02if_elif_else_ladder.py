a=int(input("enter your age: "))

if(a>=18):
    print("you are above the age of consent")
    print("good for you")

elif(a<0):
    print("you are entering a invalid age")

elif(a==0):
    print("you are entering zero`which is not valid")

else:
    print("you are below the age of consent")

print("end of program")