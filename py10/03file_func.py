f = open("file.txt")
# lines = f.readlines()##readlineS
# print(lines, type(lines))

# lines1 = f.readline()
# print(lines1, type(lines1))
# lines2 = f.readline()
# print(lines2, type(lines2))
# lines3 = f.readline()
# print(lines3, type(lines3))
# lines4 = f.readline()
# print(lines4, type(lines4))
# lines5 = f.readline()
# print(lines5=="")
# print(lines5, type(lines5))

line = f.readline()
while(line!=""):
    print(line)
    line=f.readline()

f.close()