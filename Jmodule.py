
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





def jstring(some_list = [],  some_filler = ''):

		if some_list == []:
			print("Enter a list into the first argument of strconvert().")
			exit()


		a = str(some_filler)
		some_string = a.join( str(element).strip() for element in some_list)

		return some_string


def jfilename(some_string = '',  some_file_ext = ''):

		if some_string == '' or some_file_ext == '':
			print("Enter a string into the first argument of jfilenamet()."
			"\nEnter a file extension as a string into the second argument of jfilenamet().")

			exit()
		
		
		some_string = str(some_string) + "." + str(some_file_ext)
		some_string = some_string.replace('\n',' ')
		#some_string = some_string.replace('.',' ')
		some_string = some_string.replace('-',' ')
		some_string = some_string.replace(' ','_')

		return some_string


