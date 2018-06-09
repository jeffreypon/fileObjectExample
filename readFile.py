# File Objects

"""
f = open('test.txt', 'r')
print(f.mode)
f.close()
"""


"""
with open('test.txt', 'r') as f:
    # Do nothing
    pass
print(f.closed)
"""

# Open File
with open('test.txt', 'r') as f:

    # Sets size to read
    sizeToRead = 4

    # Store File Chunk in an object
    f_contents = f.read(sizeToRead)

    #Read() with no args passed reads entire file. You're fault if you don't have enough RAM
    #f_contents = f.read()

    # States current position of file
    #print(f.tell())

    # Loop Through File Object
    while len (f_contents)>0:
        print (f_contents, end='')
        f_contents = f.read(sizeToRead)

"""
with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents)
"""

"""
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')
"""