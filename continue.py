
#the continue function puts control back to the top of the 
#for loop with the next iteration

for number in range(10):
	if number % 2 == 0:
		continue
	print(number)

#-----------------------------------------
print("\n")
#Or closer to C++:
#-----------------------------------------

Number = 0
while Number <10:
	Number +=1
	if Number % 2 == 0:
		continue
	print(Number)

#NOTE: INFINITE LOOP IF LINE 14 REMOVED.
#CLEARLY THE FIRST CODE IS SUPERIOR.
