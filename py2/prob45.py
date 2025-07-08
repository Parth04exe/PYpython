#write a python program to print the contents of a directory using the os module.
#search online for the function which does that

import os

# Specify the directory you want to list
directory_path = '/'  # current directory

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print each item
for item in contents:
    print(item)
    
print(contents)

