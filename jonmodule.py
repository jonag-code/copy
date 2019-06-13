
class Sub_in_main():
	def __init__(self, sub_string = '', main_string = '' ):
		
		
		if sub_string == '' or main_string == '':
			print("Sub_in_main() requires a (sub) string as its first argument"
				" and a (main) string as its second argument.")
			exit()
		
		self.sub_string = str(sub_string)
		self.main_string = str(main_string)


	def jfind(self, num_elements =""):
		
		m = self.sub_string
		M = self.main_string

		Index = [M.find(m)]

		for element in Index:
			if element == -1:
				Index.remove(element)
				break
			else:
				next_element = M.find(m, element + 1 )
				Index.append(next_element)

		#self.Index = Index

		if num_elements  == "" :
			return( Index )
		if num_elements in range( len(Index) ):
			return( Index[0: num_elements ])
		else:
			print("Out of range! Leaving this empty will produce the full list.")
			exit()
	

	def jcount(self):

		F = self.jfind()
		#F = self.Index
		return len(F)





	def jfindd(self, num_elements =""):
		
		m = self.sub_string
		M = self.main_string

 
		Index = [M.find(m)]
		
		for n in range ( len(M) ):
			if Index[n] == -1:
				Index.remove(Index[n])
				break
			else:
				Index_n_plus_1 = M.find(m, Index[n] + 1 )
				Index.append(Index_n_plus_1)
		
		# self.Index = Index

		if num_elements  == "" :
			return( Index )
		if num_elements in range( len(Index) ):
			return( Index[0: num_elements ])
		else:
			print("Out of range! Leaving this empty will produce the full list.")
			exit()

	def jcountt(self):

		G = self.jfindd()
		#G = self.Index
		return len(G)



	def location(self, num_elements =""):
		
		m = tuple(self.sub_string)
		M = tuple(self.main_string)
		

		last_index_m = len(m) - 1
		last_index_M = len(M) - 1

		
		J_start = [] 
		for j in range(last_index_M + 1):
			if M[ j ] == m[0]:
				J_start.append(j)
		last_index_J_start = len(J_start) - 1


		if J_start == []:
			return J_start 
			exit()



		for k in range(last_index_J_start + 1):
			if J_start[-1] + last_index_m > last_index_M:
				J_start.remove( J_start[-1] )
				last_index_J_start = len(J_start) - 1 				
		'''			
		for k in range(last_index_J + 1):
			if J[last_index_J] + last_index_m > last_index_M:
				J.remove( J[last_index_J] )
				last_index_J = len(J) - 1 
		'''
		J = []
		for k in range(last_index_J_start + 1):
			for i in range( last_index_m + 1):
				J_k = J_start[ k ]
				if  M[ J_k + i ] == m[ i ] and J_k + i <= last_index_M :
					if i == last_index_m:
						J.append( J_k )	
					continue
				break
		#self.J = J	

		if num_elements  == "" :
			return(J)
		elif num_elements <= len(J):
			return( J[0: num_elements + 1 ])
		else:
			print("Out of range! Leaving this empty will produce the full list.")
			exit()
		'''
		## Alternative code to lines 32 to 35:
		
		for f in reversed( range(len(L)) ) :
			if L[f] + last_index_m > last_index_M:
				L.remove( L[f] )
		
		last_index_L = len(L) - 1 	
		'''
	def counter(self):
		
		D = self.location()
		#D = self.J
		return len(D)


	## NOTE1: This code reproduces the same output as the 'location()' method above
	## whose guts are contained between lines 20 to 49, compared to this code
	## whose guts are contained between lines 86 to 94 ...yet this one STILL
	## computes around 3 times slower...HOW?!

	# NOTE 2: adding the local variable definitions m and M inside locationn() gives 
	## a speed boost, however location() still compiles 2 times faster than locationn() ...
	def locationn(self, num_elements =""):
		
		m = self.sub_string
		M = self.main_string
		#Read somewhere that using tuples is more efficient... it's not tho..

		last_index_m = len(m) -1
		last_index_M = len(M) -1


		index_list = []
		for J in range( last_index_M + 1 ):
			for k in range( last_index_m + 1 ):
				if (J+k) <= last_index_M  and M[ J + k ] == m[ k ]:
					if k == last_index_m:
						index_list.append(J)
					continue
				break
		len_index_list = len(index_list) 
		#self.index_list = index_list


		if num_elements  == "" :
			return( index_list )
		elif num_elements in range( len_index_list +1):
			return( index_list[0: num_elements ])
		else:
			print("Out of range! Leaving this empty will produce the full list.")
			exit()

	def counterr(self):

		F = self.locationn()
		#F = self.index_list
		return len(F)



def strconvert(some_list = [],  some_filler = ''):

		if some_list == []:
			print("Enter a list into the first argument of strconvert().")
			exit()


		a = str(some_filler)
		some_string = a.join( str(element).strip() for element in some_list)

		return some_string

'''
def filestrconvert(some_string = '',  some_filler = ''):

		if some_string == '':
			print("Enter a string into the first argument of filestrconvert().")
			exit()

		


		a = str(some_filler)
		some_string = a.join( str(element).strip() for element in some_list)

		return some_string




'''


'''
class List_to_string():
	def __init__(self):
		pass
		
	def strconvert(self, some_list = [],  some_filler = ''):

		if some_list == []:
			print("Enter a list into the first argument of strconvert().")
			exit()


		a = str(some_filler)
		some_string = a.join( str(element).strip() for element in some_list)

		return some_string



	def strconvertt(self, some_list,  some_filler = ''):

		if some_list == '':
			print("Enter a list into the first argument of strconvert().")
			exit()

		b = str(some_filler)
		#interstingly without this in between local variable definition
		# the code runs slower....i.e. using: 
		# some_string = some_string + b + str(element).strip(), is faster than
		# some_string = some_string + str(some_filler) + str(element).strip(),
		# inside the for loop
		Some_string = ''
		for element in some_list:
			Some_string = Some_string + b + str(element).strip() 
			#some_string = some_string + str(some_filler) + str(element).strip() 

		return Some_string[1:]
'''




'''
##EXAMPLE 1:
import time
sbm = Sub_in_main 
j = List_to_string()
## both above are Classes within this module (also...don't need to import as already inside)


filename = 'pi_1000.txt'
with open(filename) as f:
	raw_pi_list = f.readlines()


sub_string = '66'
pi_string = j.strconvert(raw_pi_list)


print(raw_pi_list[0:3])
print(pi_string[0:32])


v = sbm(sub_string, pi_string)


start = time.time()

print("Location: %s" %v.location() )
print("Counter: 	%i" %v.counter() )

end = time.time()
delta_t_1 = (end-start)



start = time.time()

print("\nLocationn: %s" %v.locationn() )
print("Counterr: 	%i" %v.counterr() )

end = time.time()
delta_t_2 = (end-start)

print("\nThe second output takes %f times longer to compile than the first." %(delta_t_2/delta_t_1) )

'''




'''
##EXAMPLE 2:
## Note: the original list 'List' is one of integer elements, so the 
## in between code in example2 is necessary to reproduce List.

j = List_to_string()

List = [1,2,3,4]

string1 = j.strconvert( List ) 
string2 = j.strconvert( List, ' |' ) 

example1 = list( j.strconvert( List ) )
example2 = list( int(x) for x in j.strconvert( List ) )

print(string1)
print(string2)

print(example1)
print(example2)
'''

'''
##EXAMPLE 3: 
import time
sbm = Sub_in_main 
j = List_to_string()


raw_list_integers = list(range(10))
print(raw_list_integers)


start = time.time()

string = j.strconvert(raw_list_integers,'.')



end = time.time()
delta_t_1 = (end-start)


start = time.time()

String = j.strconvertt(raw_list_integers,'.')

end = time.time()
delta_t_2 = (end-start)

print(string)
print(String)

print("Second code takes %f the time as the first code" %(delta_t_2/delta_t_1) )
'''


'''

##EXAMPLE 4: COMPARES four substring in mainstring counters
import time
sbm = Sub_in_main 

M = '90087654321011131415'
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

'''



