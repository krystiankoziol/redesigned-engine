import math

var_first = 10
var_secound = 12

print (var_first, var_secound)
print (var_secound)
print (type (var_first))

var_3 = "uczymy sie Pythona"
var_first = 10.0

#List of data
list_of_data = [1,2,'Tekst',(234.56, 233.78)]
print (10*'#')
print (list_of_data)
print (10*'#')
for element_of_list in list_of_data:
    print((element_of_list),type(element_of_list))
    print (10*'#')
print (10*'*')
for element_of_list in list_of_data:
    print('Velue=',element_of_list,'Type=' ,type(element_of_list),)
    print (10*'#')

print (math.sin(0.1567))

#Indeks in string
print(var_3[5])
print(var_3[-5])
print(var_3[2:10])

#Extra chars in string
print("""uczymy 'sie' Pythona""")
print("uczymy sie \n Pythona")
print("uczymy sie \t Pythona")


def Nazwa_Funkcji(var_first, var_secound):
    result = var_first/var_secound 
    return result

print (Nazwa_Funkcji(10,13.0))
if ....:
    stac
elif ...:
    stac
else:
    stac
