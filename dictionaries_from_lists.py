#THE CODE AFTER THIS ONE IS THE SUPERIOR VERSION:

d = {1:'one',2:'two'} 
print("This is the old d: \n %s \n" %d) 

Keys = list(d.keys()) 		
Values = list(d.values()) 	

for i in range(len(d)):
	d[Values[i]] = d[Keys[i]]
	del d[Keys[i]]
print("This is the new (overwritten) d: \n %s \n" %d) 

#Here we create two lists and overwrite a dictionary,
#where the data of dictionary lives in these two lists.
#The new keys are equivalent to the values.


#--------------------------------------------------------------------------------
c = {1:'one',2:'two'} 

e = dict(zip( list(c.values()) , list(c.values()) ) )
f = dict(zip( list(c.keys()) , list(c.keys()) ) )
g = dict(zip( list(c.values()) , list(c.keys()) ) )
print("These are new dictionaries, generated \
in a more versatile and efficient manner: \n %s \n %s \n %s, \n\n\
from the unmodified original: \n %s \n " %(e,f,g,c)) 


#This is a general method for creating a
#dictionary out of two (temporary) lists of same size.
#Doesn't delete/ modify any pre-exiting list.
#The previous code has to be completely altered
#to achieve the same results as this one.


