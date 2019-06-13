List =[x**2 for x in range(5)]   
Dictionary = {0:'zero',  1:'one',  2:'four',  3:'nine',  4:'sixteen'}
Tuple = tuple(List)  		
#The following doesn't work as with lists: Tuple2 =(x**2 for x in range(10)).
#Also the entries of tuples cannot be modified like in lists or dictionaries. 
#This is useful when storing important information.

print("The following is a list followed by tuple: \n%s\n%s \n" %(List,Tuple))
print("This was the old dictionary: \n %s \n" %Dictionary)


for i in range(len(List)):
	print("%s \t%s \t%s " % (List[i], Tuple[i], Dictionary[i]) )
print("\n")
#Note how all three types are referenced the same way, In a given 
#dictionary only the "value" is printed, for instance,
# where the reference is the "key": Dictionary[key_0] = value_0.


Copy_Dictionary = dict(Dictionary)
#NOTE: Copy_Dictionary = Dictionary will not only copy, but both
#will change dynamically. Here unwanted. In for loop fine?
print("This is a copied dictionary: \n%s " %Copy_Dictionary)


#--------------------------------------------------------------------------------

#THE CODE BELOW HAS TWO BETTER VERSIONS IN: dictionaries_from_lists.py 
#ACTUALLY REALLY BAD CODE HERE, AS THE FOR LOOP CRITICALLY DEPENDS ON 
#THE FIRST "key" OF dictionary TO BE EQUAL TO 0.

dictionary = {0:'zero',  1:'one',  2:'four'}
copy_dictionary = dict(dictionary)

VALUES = list(dictionary.values())


for n in range(len(dictionary)):
	#Copy_Dictionary[ VALUES[n] ] = Copy_Dictionary.pop(n)
	copy_dictionary[ VALUES[n] ] = copy_dictionary[n]
	del copy_dictionary[n]
print("\n \nThis is the old dictionary: \n %s" %dictionary)
print("This is the new dictionary: \n %s\n" %copy_dictionary)






