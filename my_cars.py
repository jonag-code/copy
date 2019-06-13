from car_module import Car 
from electric_car_module import ElectricCar
#from electric_car_module import ElectricCar, Car

my_beetle = Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())

#Note: ElectricCar() is a child class that uses the
#	parent class Car() in it's definition. The module 
#	"electric_car_module" uses Car() by importing
#	car_module as well! 
#Use the commented out line 3 and remove lines 1 and 
#	2 to show this.