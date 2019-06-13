
#code needs to be fixed for this example:

sub_string = '999'
filename = 'pi_30.txt'

with open(filename) as f:
	lines = f.readlines()

main_string = ''
for line in lines:
	main_string = main_string + line.strip()




#main_string = '9019029039'

m = list(sub_string)
M = list(main_string)
last_index_value_m = len(m) - 1
last_index_value_M = len(M) - 1

#print(float(main_string))
print(M)

#print("%s \n---> m = %s\n%s  \n---> M = %s \n" %(sub_string, m, main_string, M) )


#These are the set of values B_1,.., B_n
# such that M[B_1] = .. = M[B_n] = m[0]. 
#In other words the set of index locations 
# within the M string that match the first
# value of the m (sub) string.
B = []
for M_INDEX in range( last_index_value_M + 1 ):
	if M[ M_INDEX ] == m[0]:
		B.append(M_INDEX)
	

if len(B) == 0:
	print("\nsubstring not in main string")
	exit()

#print(B)
last_index_value_B = len(B) - 1
#print(len(B))
#print(last_index_value_B)

last_value_B = B[last_index_value_B]



if last_value_B + len(m) - 1 > last_index_value_M:
	B.remove(last_value_B)

	last_index_value_B = len(B) -1
	last_value_B = B[last_index_value_B]
#print(B)

# C values are going to be a subset of B values,
# which give the starting positions for the 
# substring to be contained in the mainstring
C = []

for B_INDEX in range( last_index_value_B + 1 ):
	for m_INDEX in range( last_index_value_m + 1 ):
		#this 'X' definition is for clarity only
		X = B[ B_INDEX ]
		#print("B_INDEX: %s" %B_INDEX)
		#print("m_INDEX: %s" %m_INDEX)
		#print("last_index_value_m: %s" %last_index_value_m)
		if M[ X + m_INDEX ] == m[ m_INDEX ] and X + m_INDEX in range(last_index_value_M + 1):
			if m_INDEX == last_index_value_m:
			#continue
				C.append( X )
	#C.append( X )

last_index_value_C = len(C) - 1
#print("C = %s" %C)


if len(C) == 0:
	print("\nsubstring not in main string")
	exit()
else:
	print("\nThe substring begins at these indices in the main string: ")
	for k in range(last_index_value_C + 1 ):
		print("%i" %(C[ k ] -1) )

