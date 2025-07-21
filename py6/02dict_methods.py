marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0:"parth"
}
print(marks)
print(len(marks))
print(marks.items())#gives a list of key value pair and they are in the form of tuples
print(marks.keys())#left hand side are called keys
print(marks.values())#right hand side are called vaklues
marks.update({"Harry":99})#original disk is updated because it is mutable
print(marks)
marks.update({"Renuka":100})
print(marks)
print(marks.get("shiv"))

print(marks.get("Harry"))
print(marks["Harry"])
#print(marks.get("Harry2"))#prints none
#print(marks["Harry2"])#return error

new_dict = dict.fromkeys(marks)# Create dictionary with default value None
print(new_dict)
new_dict2 = dict.fromkeys(marks, 1)# Create dictionary with a given value
print(new_dict2)

new_dict = dict.fromkeys("abc", 1)# Using a string as keys
print(new_dict)


marks2=marks.copy()
print(marks2)

print("\n\n\n")

mark = marks.pop("Renuka")
print(mark) 
print(marks)  
mark = marks.pop(0)
print(mark)  
print(marks)

item = marks.popitem()
print(item)  
print(marks)

print("\n\n\n")


marks.clear()
print(marks)  # Output: {}

new_dict = dict.fromkeys(marks)
print(new_dict)

#dict.setdefault(key, default)
d = {"fruit": "apple"}
d.setdefault("fruit", "banana")  # Key exists, so value stays "apple"
print(d)
d.setdefault("color", "red")     # Adds "color" since key doesn't exist
print(d)  # Output: {'fruit': 'apple', 'color': 'red'}