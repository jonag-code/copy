from jonmodule import List_to_string 
j = List_to_string()


some_string = 'steebeeweebee'

#Easy to convert string to list:
some_list = list(some_string)


## 3 ways to convert list to string:

	#C++-y way
some_string_1 = ''
for k in range( 0 , len(some_list) ):
	some_string_1 += some_list[ k ]

	#C++/Python way
some_string_2 = ''
for element in some_list:
	some_string_2 += element

	#Python-y way
some_string_3 = ''.join( str(element) for element in some_list)


## This is a function I created in the module 'jonmodule',
## doing the reverse of what list() does to a string. In the
## relevant class 'List_to_string()' I use the code from line 24
## but could've used line 14 code to be safest.
some_string_4 = j.strconvert(some_list, '/')
some_string_5 = j.strconvert(some_list)






print(type(some_string))
print("some_string (original): %s" %some_string)
print("\n")

print(type(some_list))
print(some_list)
print("\n")

print(type(some_string_1))
print("some_string_1: %s" %some_string_1)
print("\n")

print(type(some_string_2))
print("some_string_2: %s" %some_string_2)
print("\n")

print(type(some_string_3))
print("some_string_3: %s" %some_string_3)
print("\n")

print(type(some_string_5))
print("some_string_4: %s" %some_string_4)
print("\n")

print(type(some_string_5))
print("some_string_4: %s" %some_string_5)
print("\n")

