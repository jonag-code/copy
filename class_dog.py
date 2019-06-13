#p. 162-166 of PCC.
#FUNCTIONS DEFINED INSIDE A CLASS ARE CALLED "METHODS".
class Dog():
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
her_dog = Dog('akira', 8)

print("My dog is %s years old." %my_dog.age )
print("Her dog is %s years old.\n" %my_dog.age )

my_dog.roll_over()
her_dog.sit()

#The class Dog() is çalled in line 15 as if it were a function. 
#	The variable "my_dog" in line 15 is called an "INSTANCE" and
#	the value of input variables are called "ATTRIBUTES" of the
#	correponding instance, my_dog. 

#The "." notation, e.g. in line 18, calls on the ATTRIBUTES
#	in a similar manner to key-value pairs in a dictionary, 
#	with the exact calling form defined in lines 5 and 6.



