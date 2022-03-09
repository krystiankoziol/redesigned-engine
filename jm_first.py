import math

var_first = 10
var_secound = 12

print (var_first, var_secound)

print (type (var_first))

var_3 = "uczymy sie Pythona"
var_first = 10.0

list_of_data = [1, 2, "tekst", (234,56, 233,78)]
print(10*"@")
print (list_of_data)
print(10*"@")

for element_of_list in list_of_data:
    print (str(element_of_list) + " " + str(type(element_of_list)))
    print(10*"#")

print(math.sin(0.1567))

print (var_3[5])
print (var_3[-5])
print (var_3[2:10])

print("""raz dwa trzy 'cztery'""")
print("""raz\n dwa\n trzy 'cztery'""")
print("""raz dwa trzy\t 'cztery'""")

def Nazwa_funkcji (var_1,var2):
    var_1 = 1
    return var_1

print Nazwa_funkcji(var_first, var_secound)
