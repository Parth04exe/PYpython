with open ("log.txt") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if("python" in line):
        print(f"Present in {lineno}")
        break
    lineno+=1

else:
    print("not present")