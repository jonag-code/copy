## This code doesn't do what I need it to do. Line 32 shows that
## the check variable doesn't continue to update.

sub_string = '14159'
#birthday_string = '121391'
#birthday_string = '66666'

filename = 'pi_one_million_digits.txt'
#filename = 'e_two_million_digits.txt'
#filename = 'sqrt2_one_million_digits.txt'


with open(filename) as f:
	lines = f.readlines()


main_string = ''
for line in lines:
	main_string = main_string + line.strip()







sub_string = '50'
main_string = '0150506'

A = list(sub_string)
B = list(main_string)


len_A = len(A)
len_B = len(B)


b_start = []

for b in range( len_B ):
	if B[b] == A[0]:
		b_start.append(b)

len_bstart = len(b_start)
print(b_start)
print("\n")



return_value= 0
index = 0

for index in range(len_bstart):
	for a in range(0,len_A) :
		x = b_start[index] + a 
		print(x)
		if ( B[x] == A[a] ) and (x < len_B):
		#print("B[%i]  =  A[%i] " %(x, a))
			if a  == len_A - 1:
				return_value = 1
	

		else:
			return_value =-1 
			
#print(a)

#return_value == -1

if return_value == -1:
	print("%s not in %s" %(sub_string, main_string))
	
elif return_value == 1  :
	print("%s is in %s!"\
				" Location is at character %i "\
				"of %s." %(sub_string,main_string, b_start[index] + 1, main_string ))
else: 
	print("Unexpected error.")



print("\n")
print("return value: %i" %return_value)
print("\n")



