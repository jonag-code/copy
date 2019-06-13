cars = ['bmw','audi','toyota','subaru']

print("Original list:")
print(cars)

print("Reversed:")
cars.reverse() #replaces the cars list by the reverse list
print(cars)

print("Alphabetic sorted:")
cars.sort() 
print(cars)


print("Reverse alphabetic sorted:")
cars.sort(reverse =True) 
print(cars)

print("This is the length of the list: " + str(len(cars))+ "." )
#len(cars) inputs an arbitrary variable and spits out a number
