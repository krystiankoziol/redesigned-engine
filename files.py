import os
# Path to file which you want to raed
# in file there is one line 'Ala ma kota'
path = r'path to file'  # c:\\....
path = r'D:\\Git\redesigned-engine\example.csv'

try:
    my_file = open(path, 'r')
    lines = my_file.readlines()
    print(lines)
    # file is in readable mode
    # do work with data from file
finally:
    my_file.close()

# with loop
with open(path, 'a') as my_file:
    # file is in append mode
    # work with my_file
    my_file.write('Ala nie ma papugi')
print('in this line the file is closed\n')



with open(path, 'r') as my_file:
    while True:
        line = my_file.readline()
        if not line:
            break
        print(line.split(' '))
print('end of work - in this line the file is closed\n')

with open(path, 'r') as my_file:
    lines = my_file.readlines()
    for line in lines:
        print(line)
print('end of work - in this line the file is closed\n')

with open(path, 'r') as my_file:
    content = my_file.read(4)
    print('read(4)')
    print('I read this from file {0}'.format(content))
    print('And Im in this position in flie {0}'.format(my_file.tell()))
    content = my_file.read(8)
    print('Read next - read(8)')
    print('Now I read this from file {0}'.format(content))
    print('And Im in this position in flie {0}'.format(my_file.tell()))
    content = my_file.read()
    print('next - read()')
    print('Now I read this from file {0}'.format(content))
    print('And Im in this position inflie {0}'.format(my_file.tell()))
    print('back to beginning of file - seek()')
    print('And Im in this position inflie {0}'.format(my_file.tell()))
print('end of work - in this line the file is closed \n')

# with loop
with open(path, 'w') as my_file:
    # file is in writable mode
    # work with my_file
    my_file.write('Ala ma psa')
print('end of work - in this line the file is closed')
print('Guess what is in the file')