incr=2

for value in range(1,7,incr):
	print(value)
print('\n')
#prints integers up to but not including last.
#increments by incr value


numbers = [x**2 for x in range(1,6)]
numbers2=list(range(1,6))  #same output as line 10

halves = [x/2 for x in range(1,6)] #form of line 10 better for manipulation 
print(numbers)
print(numbers2)
print(halves)
print('\n')



squares=[]
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

#OR with one less defined variable
squares2=[]
for y in range(1,11):
	squares2.append(y**2)
print(squares2)

#OR the much faster code, similar to line 10.
squares3 = [z**2 for z in range (1,11)]
print(squares3)








