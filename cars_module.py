#The classes here are copied from "class_cars_3.py".
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

