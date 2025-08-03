def convert(f):
    c=round((5*(f-32)/9),2)
    print(f"the temperature in celsius is {c}")

f=int(input("enter temperature in farhenite"))
convert(f)