# will overwrite


with open('test2.txt', 'w') as f:
    f.write('Test1')

    #Move write file pointer position
    f.seek(2)
    f.write('wassup')




# will append
"""
with open('test2.txt', 'a') as f:
    pass
print(f.closed)
"""