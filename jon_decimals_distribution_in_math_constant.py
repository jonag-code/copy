import time
from jonmodule import Sub_in_main as sbm
from jonmodule import List_to_string
j = List_to_string()
#j = List_to_string



filename = 'pi_1000.txt'

with open(filename) as f:
	lines = f.readlines()


sub_string = '1'

main_string = ''
for line in lines:
	main_string += line.strip()
## OR using my function:
main_string_2 = j.strconvert(lines)

'''
print(lines)
print(main_string_2)
print(type(main_string_2))
print("\n")
'''

main_list = list(main_string)[2:]



int_main_list = [int(N) for N in main_list]
int_main_list_2 = [int(N) for N in main_string_2[2:]]
#print(intlist_main_string)
avg = sum(int_main_list) / ( len(int_main_list) -1)
print(avg)

avgg = sum(int_main_list_2) / ( len(int_main_list_2) -1)
print(avgg)


##CODE #1: the quickest/ Python-est:
values_0 = [N for N in range(10)]
distr_values_0 = [ sbm( str(N) , main_string_2[2:]).counter() for N in values_0 ]

num = 0
for L in range(len(values_0)):
	num += values_0[L] * distr_values_0[L]

avgg = float(num)/ float(sum(distr_values_0)) 
print(avgg)




#exit()

## CODE #2: The longest/ C++-est:
s = time.time()
values_1 = []
for N in range(10):
	values_1.append(str(N))
	#decimals_1 += str(N)
last_index_values_1 = len(values_1) -1


distr_values_1 = []
for M in range(last_index_values_1 + 1):
	v = sbm( values_1[ M ], main_string)
	distr_values_1.append( v.counter() )  
e = time.time()
dur_1 = e-s



s = time.time()
values_2 = []
for N in range(10):
	values_2.append(N)
	#decimals_1 += str(N)
last_index_values_2 = len(values_2) -1


distr_values_2 = []
for value in values_2:
	v = sbm( str(value), main_string)
	distr_values_2.append( v.counter() )  
e = time.time()
dur_2 = e-s


s = time.time()
values_3 = [N for N in range(10)]
distr_values_3 = [ sbm( str(value) , main_string).counter() for value in values_3]
e = time.time()
dur_3 = e-s




s = time.time()
distr_values_4 = [ sbm(str(N) , main_string).counter() for N in range(10)]

e = time.time()
dur_4 = e-s

##Going to use this last code to try which of three count methods is fastest
## in jonmodule. 


print( '{} \n{} \n{} \n{} ' 
''.format(distr_values_0, distr_values_1, distr_values_3, distr_values_4) )


print("\nDuration in 10^-4 seconds:")
print(10**4*dur_1, 10**4*dur_2, 10**4*dur_3, 10**4*dur_4)
print("\n")
 


#Using the simplest code above now test three similar output functions from 
## jonmodule


M = main_string
#M = '90087654321011131415'
some_range = range(0,10)


s = time.time()
distr_valuess_0 = [ sbm(str(N) , M).jcount() for N in some_range]

e = time.time()
del_0 = e-s


s = time.time()
distr_valuess_1 = [ sbm(str(N) , M).jcountt() for N in some_range]

e = time.time()
del_1 = e-s




s = time.time()
distr_valuess_2 = [ sbm(str(N) , M).counter() for N in some_range]
e = time.time()
del_2 = e-s



s = time.time()
distr_valuess_3 = [ sbm(str(N) , M).counterr() for N in some_range]
e = time.time()
del_3 = e-s


print( '{} \n{} \n{}  \n{} ' 
''.format(distr_valuess_0, distr_valuess_1, distr_valuess_2, distr_valuess_3) )


print("\nDuration in 10^-4 seconds:")
a = 10**4

print('	jcount: 	{}'.format(a*del_0) )
print('	jcountt:	{}'.format(a*del_1) )
print('	counter: 	{}'.format(a*del_2) )
print('	counterr: 	{}'.format(a*del_3) )









