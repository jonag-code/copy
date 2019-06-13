#THE VALUE OF FUNCTIONS IS TO DO SIMPLE TASKS TO BE REPEATEDLY USED 
#IN THE BODY OF THE CODE, IN EFFECT MAKING IT MORE READABLE. IF A FUNCTION 
#IS DEFINED TO DO TOO MANY TASKS IT IS NOT AS POWERFUL. REMEMBER YOU CAN CALL 
#FUNCTIONS WITHIN A FUNCTION.
def f(x,y):
	return x + y
x_0=1
y_0=2	
print("The function evaluated at (%s,%s) is %s" %( x_0, y_0, f(x_0,y_0)) )

#--------------------------------------------------------------------------
from math import sin, exp
#Or: import math ... and use math.sin(), math.exp(), etc

def g(x, a = '', b=''):
	if a and b:
		return exp(a*sin(b*x))
	elif a:
		return exp(a*sin(x))
	elif b:
		return exp(sin(b*x))
	else:
		return exp(sin(x))
value = g(3.14)
vvalue = g(3.14, 1)
vvvalue = g(a =1, b =1, x= 3.14)

print(value)
print(vvalue)
print(vvvalue)

#NOTE HOW g(x,a,b) HAS THE FLEXIBILITY TO TAKE 1,2, OR 3
#INPUT DATA AS EVIDENCED IN LINES 24-26.
#--------------------------------------------------------------------------
##PASSING AN ARBITRARY NUMBER OF ARGUMENTS INTO A FUNCTION USING '*'': 
def make_pizza(size, *toppings):
	print("\nMaking a " +str(size)+ "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
make_pizza(16,'pepperoni')
make_pizza(12, 'mushrooms','green peppers', 'extra cheese')

