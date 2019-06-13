#continuing from "class_cars.py"
class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 25

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has %s miles on it." %self.odometer_reading)

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You attempted to set the odometer value to %s miles. \
You can't roll back an odometer!" %mileage)

	def increment_odometer(self,miles):
		self.odometer_reading += miles


my_new_car = Car('audi','a4',2016)

print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(15)

my_new_car.increment_odometer(100)
my_new_car.read_odometer()


#Line 30 uses the method in line 16 to update the value of the 
#	"odometer_reading" attribute. This can only happen if the 
#	new value is greater or equal to the old one. Line 33 
#	explicitly increments the old value.

#Go to "class_cars_3.py" for additive code.


