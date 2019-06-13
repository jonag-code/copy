
sub_string = '1911'
main_stringg = '0999199299'

filename = 'pi_1000000.txt'

with open(filename) as f:
	lines = f.readlines()

main_string = ''
for line in lines:
	main_string = main_string + line.strip()



m = tuple(sub_string)
M = tuple(main_string)

#print(float(main_string))

A = [] 
# Will hold the index locations, A_i, in M such that:
# M[A_i] = m[0], for as many indices that i runs over
# i = 0 to len(A) - 1 (the length span of A).

last_index_m = len(m) - 1
last_index_M = len(M) - 1
#these are useful for clarity in reading back the code


for J in range(last_index_M + 1):
	if M[ J ] == m[0]:
		A.append(J)

if A == []:
	print("(1) The substring is not in the main string.")
	exit()


last_index_A = len(A) - 1 



for k in range(last_index_A + 1):
	if A[last_index_A] + last_index_m > last_index_M:
		A.remove( A[last_index_A] )
		last_index_A = len(A) - 1 



# Same output but way faster!
C = []
for j in range(last_index_A + 1):
	for i in range(last_index_m + 1):
		Z = A[ j  ] + i
		if  M[ Z ] == m[ i ] and Z in range(last_index_M +1):
			if i == last_index_m:
				C.append( A[j] )	
			continue
		break
print(C)
print(len(C))
'''


##Same ouput but slower!
A_copy = A.copy()
last_index_A_copy = len(A) -1

for j in range(last_index_A_copy + 1):
	for i in range(last_index_m + 1):
		Z = A_copy[ j  ] + i
		if  MM[ Z ] == mm[ i ] and Z in range(last_index_M +1):
			continue
		A.remove( A_copy[ j ] )
		break
	
print("\n%s" %A)
'''