
##Starting with a list of characters representing numbers, convert to 
## a list of numbers:

list0 = ['4','3', '2', '1', '5']
#list0.sort()


## Note:  "list1" and "list2" for loop is closer to how you would do it in C++

list1 = [] 
m=0
print(m)
print(len(list0))
#while m < len(list0):
	#list1.append( int(list0[m]) )

list2 = [] 
for n in range( len(list0) ):
	list2.append( int(list0[n]) )


list3 = [int(list0[n]) for n in range( len(list0) ) ]

list4 = [int(x) for x in list0 ]


print(list0)
#print(list1)
print(list2)
print(list3)
print(list4)

