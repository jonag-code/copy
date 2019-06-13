#This single class is copied from "cars_module.py". We choose to seperate
# the Car() class from the Battery() class and the ElectricCar() child class.
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