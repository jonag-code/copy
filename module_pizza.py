#Files, such as this one, which only contain functions are called MODULES.
#The functions in MODULES are imported into other files to be used. Here the 
#calling file will be "using_module_pizza.py"

def create_pizza(size, *toppings):
	print("\nMaking a " +str(size)+ "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

#THIS FUNCTION ACCEPTS AN ARBITRARY NUMBER OF ARGUMENTS AFTER THE FIRST ONE,
#USING THE * OPERATOR. * CREATES AN EMPTY TUPLE WHICH OBTAINS AN ARBITRARILY
#LARGE LENGTH DEPENDING ON THE NUMBER OF INPUT DATA. LINE 7 IN THE FUNCTION
#THEN READS THE TUPLE "toppings" AN ENTRY AT A TIME.

