import math

var_first = 8
var_second = 19
print(var_first, var_second)

print(type(var_first))

var_third = "Hello world :p"

print(20*'*')

list_of_data = [1,2,'Word', (125.21, 241.81)]
print(list_of_data)

print(20*'*')
print(list_of_data[0],list_of_data[1],list_of_data[2],list_of_data[3])
print(20*'*')

for i in list_of_data: ##i - emelment of list
    type_of_el = type(i)
    print (str(i) +' '+ str(type_of_el))

print(20*'*')

print(math.sin(var_second*2.0))

#indesk in string
print(var_third[0:5])
print(var_third[-5:-1])
print(var_third[0:8:2])
print(20*'*')


#extra cahrs in string
print("""Hello 'world' :p""")
print("Hello 'world' :p")
print("Hello\n'world'\t :p")

print(20*'*' + '\n')


def Name_func(var_first):
    answer = var_first**2
    print(str(var_first) + '^2 = ' + str(answer))
    return 

Name_func(5)

