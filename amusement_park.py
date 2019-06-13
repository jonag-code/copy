age =5

if age <4:
	print("Your admission cost is $0.")	
elif age< 18:
	print("Your admission cost is $5.")	
elif age< 65:
	print("Your admission cost is $10.")	
else:
	print("Your admission cost is $5.")
print("\n")	

#Exampling of CHAINING if-elif-else statements in ascending
#order of age to avoid double inequalties.

if age <0:
	print("Age cannot be negative")
	exit()
elif age <4:
	price = 0
elif age< 18:
	price = 5	
elif age< 65:
	price = 10	
elif age >= 65:
	price =5	
print("Your admission is $" +str(price)+ ".")

#same output as before, but tidier. Unlike C++, Python
#doesn't need to end in an else statement. Lines 16 eliminates
#the unwanted possibility of negative age.