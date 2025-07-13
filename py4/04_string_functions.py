name="partha"

print(len(name))
print(name.endswith("tha"))
print(name.startswith("Par"))
print(name.capitalize()) # only first character

s = "  hello world  "

print(s.upper())        # '  HELLO WORLD  '
print(s.lower())        # '  hello world  '
print(s.capitalize())   # '  hello world  ' (only first non-space letter changes if stripped)
print(s.strip().capitalize()) # 'Hello world'
print(s.title())        # '  Hello World  '
print(s.strip())        # 'hello world'
print(s.lstrip())       # 'hello world  '
print(s.rstrip())       # '  hello world'

s1 = "hello world, hello python"

print(s1.find("hello"))     # 0
print(s1.rfind("hello"))    # 13
print(s1.index("world"))    # 6
# print(s1.index("java"))   # ValueError
print(s1.replace("hello", "hi"))  # 'hi world, hi python'
print(s1.count("hello"))    # 2

s2 = "Hello"
s3 = "123"
s4 = "Hello123"
s5 = "   "
s6 = "python"

print(s2.isalpha())    # True
print(s3.isdigit())    # True
print(s4.isalnum())    # True
print(s5.isspace())    # True
print(s6.islower())    # True
print(s2.isupper())    # False
print(s2.startswith("He")) # True
print(s2.endswith("lo"))   # True

s7 = "apple,banana,cherry"

lst = s7.split(",")
print(lst)             # ['apple', 'banana', 'cherry']

lst2 = s7.rsplit(",", 1)
print(lst2)           # ['apple,banana', 'cherry']

multi_line = "line1\nline2\nline3"
print(multi_line.splitlines()) # ['line1', 'line2', 'line3']

words = ["Hello", "world"]
print(" ".join(words)) # 'Hello world'

name = "Alice"
age = 25

# Using format()
print("My name is {} and I am {} years old".format(name, age))

# Using f-string (recommended, easier to read)
print(f"My name is {name} and I am {age} years old")

# Explanation:
# In format(), curly braces {} act as placeholders, which get filled by arguments.
# In f-strings, you write an 'f' before the string and can directly put variables inside {}.

s8 = "42"

print(s8.zfill(7))          # '0000042'

print("hello".center(11, "-")) # '---hello---'

print("hello".ljust(10, "."))  # 'hello.....'

print("hello".rjust(10, "."))  # '.....hello'

print("python-3.11".partition("-")) # ('python', '-', '3.11')
