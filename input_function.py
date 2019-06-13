#To get the following code to work:
#1. open a terminal sesion
#2. enter the following:
#	cd Desktop/python_work/
#	python input_function.py

number = input("Enter a number and I'll tell you if it's even or odd: ")


if number % 2 ==0:
	print("%s is an even number. " %number)
else:
	print("%s is an odd number. " %number)

