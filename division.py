try:
	print(5/1)
except ZeroDivisionError:
	print("You can't divide by zero!")

#The comment after "except" in line 3 is the usual error message
#	that oocurs when dividing by 0. Here we use it in a try block
#	which prevents the program from crashing.
#-------------------------------------------------------------------
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number:")
	if first_number == 'q':
		break
	second_number = input("\nSecond number:")
	try:
		answer = int(first_number)/ int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(answer)