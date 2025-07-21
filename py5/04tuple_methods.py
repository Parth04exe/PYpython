a=(1, 45, 342, 3424, False, "Rohan", "Shivam")
print(a)

no= a.count(45)
print(no)

print(a.index(45))

print(len(a))

#membership checking
t = ('a', 'e', 'i', 'o', 'u', 1, 2)
print('e' in t)
print(2 in t)

e = (1, 2, 3)
b = (4, 5)
c = e + b
print("Concatenated Tuple:", c)

#repeatation
u = ('Hi',) * 3
print("Repeated Tuple:", t)  # Output: ('Hi', 'Hi', 'Hi')

#repeatation
v=(1, 2, 3)
w=v*3
print(w)

#unpacking
person = ('Alice', 25, 'Engineer')
name, age, job = person
print(name, age, job)

o=(4,3,6,877,3)
print(min(o))
print(max(o))

f=(1,2,3,4,5,6)
sliceing=f[1:4]
print(sliceing)

# colors = ('red', 'green', 'blue')
# for color in colors:
#     print(color)

# nested = ((1, 2), (3, 4), (5, 6))
# print(nested[1])      # Output: (3, 4)
# print(nested[1][0])   # Output: 3

