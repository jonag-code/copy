
motorcycles = [] #empty list ti be ƒilled 


motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0,'ducati') #places at front of old list
print(motorcycles)

motorcycles[-1] = 'bmw' #overwrites last entry
del motorcycles[1] #deletes 2nd entry
print(motorcycles)


first_owned = motorcycles.pop(0) #deletes 1st item, AND stores info 
last_owned = motorcycles.pop() #deletes last item if not specified

print("The first motorcycle I owned was a "+first_owned.title() + \
	" and the last was a " +last_owned.title()+ ".")

print(motorcycles)


motorcycles.remove('suzuki')
print(motorcycles)

too_pricey = 'yamaha'
motorcycles.remove(too_pricey)
print("A " +too_pricey.title()+ " is too pricey for me.")
print(motorcycles)






