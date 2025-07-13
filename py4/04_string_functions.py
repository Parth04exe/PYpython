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
