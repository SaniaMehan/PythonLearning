# with open('read.txt', 'r') as file:
#     content = file.read()
#     print(content)


with open('read.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    # this will get content in the form of list
    # The readline() method reads a single line from the file each time it's called.
    # The readlines() method reads all the lines but in List Format
    for line in lines: # this will give content line by line
        print(line,end='')