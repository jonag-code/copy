#p. 167 of PCC
class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has %s miles on it." %self.odometer_reading)


my_new_car = Car('audi','a4',2016)

print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


#In line 7 we've added an explicit attribute, "odometer_reading", with 
#	a default value of 0. 
#Line 20 uses the method defined in line 13 to print this default value.


#See "class_cars_2.py" for added code.
