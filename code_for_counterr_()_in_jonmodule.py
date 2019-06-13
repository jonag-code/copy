## For some reason this code, mainly contained in lines 27 to 35,
## compiles ~3 times slower than in 'jonmodule_example.py'. The 
## relevant code imported from 'jonmodule.py' is also longer...


sub_string = '1911'


filename = 'pi_1000000.txt'

with open(filename) as f:
	lines = f.readlines()

main_string = ''
#main_string = '10121013101'
for line in lines:
	main_string = main_string + line.strip()



#for clarity
last_index_sub = len(sub_string) -1
last_index_main = len(main_string) -1



index_list = []
for j in range( last_index_main + 1 ):
	for k in range( last_index_sub + 1 ):
		if (j+k) <= last_index_main  and main_string[ j+k ] == sub_string[ k ]:
			if k == last_index_sub:
				index_list.append(j)
			continue
		break
print(index_list)
## Using ' (j+k) <= last_index_main ' is almost twice as fast as
## using ' (j+k) in range( last_index_main +1) ' 













