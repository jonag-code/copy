from jonmodule import Sub_in_main as sbm
import time



filename = 'pi_1000000.txt'
with open(filename) as f:
	lines = f.readlines()

main_string =''.join(line.strip() for line in lines)
#main_string = main_string[2:]
sub_string = '121391'
#sub_string = '151087'
#sub_string = '052380'
#sub_string = '6666'


v = sbm(sub_string, main_string) 

start = time.time()

print(v.location() )
v.counter() 

end = time.time()
delta_t_1 = (end-start)



start = time.time()
v.locationn() 
v.counterr() 

end = time.time()
delta_t_2 = (end-start)


start = time.time()

print(v.jfind())
v.jcount() 

end = time.time()
delta_t_3 = (end-start)


start = time.time()

print(v.jfindd() )
v.jcountt() 

end = time.time()
delta_t_4 = (end-start)

start = time.time()
main_string.find(sub_string) 


end = time.time()
delta_t_5 = (end-start)




print("\n")
code_times = dict(location = delta_t_1, locationn= delta_t_2, jfind = delta_t_3, jfindd =delta_t_4, find = delta_t_5)
#Delta = [delta_t_1, delta_t_2, delta_t_3, delta_t_4, delta_t_5]
#print("\nThe secound output takes %f times more time to compile than the first" %(delta_t_2/delta_t_1))
for (key, value) in code_times.items():
	a=10**5
	print(key, '->', value*a)
	



##EXTRA CODE:
'''
main_string = ''
for line in lines:
	main_string = main_string + line.strip()
'''



#list_1 = v.location()
#print(list_1[-1])
