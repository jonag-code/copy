#continuing from "class_cars_2.py". New code starts at line 28.
#This example on p.172 of PCC.
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

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			message = "You attempted to set the odometer value to "
			message += str(mileage) + " miles. You cannot roll back"
			message += " an odometer!"
			#print("You attempted to set the odometer value to %s miles. \
#You can't roll back an odometer!" %mileage)
			print(message)

	def increment_odometer(self,miles):
		self.odometer_reading += miles

#------------------------------------------------------------------------
class Battery():
	def __init__(self, battery_size):
		self.battery_size = battery_size

	def describe_battery(self):
		print("This car has a %s-kWh battery." %self.battery_size)

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)

#------------------------------------------------------------------------
class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery(70)
#------------------------------------------------------------------------

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery = Battery(85)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.increment_odometer(100)
my_tesla.read_odometer()


#We've added another "parent class", Battery, and a "child class"
#	ElectricCar which has the parent class, Car, as its argument. Sometimes 
#	these are called sub classes and super classes, which clarifies the 
#	code syntax of line 38.
#Note: In line 39 we could've set the default value as 70 instead of 
#	Battery(70), however using the latter allows us to use the methods
#	(functions) inside the class Battery to describe this output.




