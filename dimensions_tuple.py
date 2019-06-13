dimensions_list = [200,50] 
dimensions_tuple = (199,50)  #this a tuple (round brackets)

print(dimensions_list[0])
print(dimensions_tuple[0])  
#Note: both tuples and lists have the same index referencing
# for example when printing an entry. Tuple entries cannot be 
#overwritten, however, as with lists. Example below:


dimensions_list[0]=201  
#dimensions_tuple[0]=199 
print("\n")
print(dimensions_list[0])
print(dimensions_tuple[0])  
