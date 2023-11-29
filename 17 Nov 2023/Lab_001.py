# File Handling
# How to Read a Text, and Write into it using python Code

# Open a File
# file_object = open("sania.text", mode)

# Modes:
# 'r' for reading (default).
# 'w' for writing (creates a new file or truncates an existing one).
# 'a' for appending.
# 'b' for binary mode.
# '+' for updating (reading and writing).

# Read a File
# Reading Entire Content: content = file_object.read()
# line = file_object.readline() for a single line.
# lines = file_object.readlines() for all lines in a list.

# Write to a File

# Writing String: file_object.write(string) for a single line
# Writing Multiple Lines: file_object.writelines(list_of_strings)

# Closing a File
# Syntax: file_object.close()

# if file doesn't exist and overcome from error use try & except
try:
    with open("TestData2.txt", 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as error:
    print(error)

#how to read the file
with open("sania.txt" , 'r') as file:
    content = file.read()
    print(content)

with open("Testdata.txt" , 'r') as file:
    content = file.read()
    print(content)