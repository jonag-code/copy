
import time
from jonmodule import Sub_in_main as jon_sbm

filename = ['pi_one_million_digits.txt','e_two_million_digits.txt', 'phi_one_million_digits.txt' , 'sqrt2_one_million_digits.txt']
constant = ['pi', 'e ', 'phi ', 'sqrt2' ]
index = 0


birthday = ['121391', '101587', '110255', '042786', '141592','55555','666666','7777777','888888', '999999','052379','1415926' ]
b = 0


## Store lines of .txt file into a list. This list is separated
## into elements by virtue of whitespaces and newlines within the 
## original .txt file:
with open(filename[index]) as f:
	lines = f.readlines()


## Strip each element of the list of its whitespaces and newlines,
## then convert into one concatenated string:
'''
file_string = ''
for line in lines:
	file_string += line.strip()
'''
file_string = ''.join(line.strip() for line in lines)

#decimal_places = len(file_string)-2
decimal_places = len(file_string[2:])
approx = float(file_string)



start = time.time()

i = file_string.find(birthday[b])
if i == -1:
## Checks if substring 'birthday[b]' is in string 'file_string'.
## Returns starting index location into i, if found,  or -1 otherwise:
	print("The birthday %s is not in the first %i digits of %s ~= %f." %(birthday[b], decimal_places, constant[index], approx ) )
else:
	print("The birthday %s is in the first %i digits of %s = %f!\nIt's"\
		" first instance is at the %i-th decimal place." %(birthday[b], decimal_places, constant[index], approx, (i -2) +1 ) )

end = time.time()
delta_t_1 = (end-start)


## Because this outputs ALL the indices, it takes up to four times longer to compute than  .find()
start = time.time()
list_indices = jon_sbm(birthday[b], file_string).location()
if list_indices  == []:
	print("no")
else: 
	print("\nThe birthday %s is in the first %i digits of %s = %f!\nThe decimal place locations"\
		" are: %s." %(birthday[b], decimal_places, constant[index], approx, ', '.join(str(x -1) for x in list_indices) ) )
end = time.time()
delta_t_2 =(end-start)
#print("\nThe birthday %s is in the first %i digits of %s = %f!\nThe decimal place locations"\
#		" are: %s." %(birthday[b], decimal_places, constant[index], approx, ', '.join(str(x -1) for x in list_indices) ) )

start = time.time()
list_indices = jon_sbm(birthday[b], file_string).jfind()
if list_indices  == []:
	print("no")
else: 
	print("\nThe birthday %s is in the first %i digits of %s = %f!\nThe decimal place locations"\
		" are: %s." %(birthday[b], decimal_places, constant[index], approx, ', '.join(str(x -1) for x in list_indices) ) )
end = time.time()
delta_t_3 =(end-start)


print("\nThe third output takes %f times more time to compile than the first."\
	" \n(The compile times being %f sec and %f sec.)" %(delta_t_3/delta_t_1, delta_t_1, delta_t_3))

print("\nThe third output takes %f times more time to compile than the second."\
	" \n(The compile times being %f sec and %f sec.)" %(delta_t_3/delta_t_2, delta_t_2, delta_t_3))

print("\nThe second output takes %f times more time to compile than the first."\
	" \n(The compile times being %f sec and %f sec.)" %(delta_t_2/delta_t_1, delta_t_1, delta_t_2))

print("\nNote the second code outputs ALL the indices, not just the first.\nEven if there is only one "\
	"output the code is built to keep trying after the first found.")
'''



Main = '245125661212'
sub = '12'



i = Main.find(sub)
j = Main[i+1:].find(sub) + i + 1
k = Main[j+1:].find(sub) + j + 1

print(i)
print(j)
print(k)

empty = []
for i in range(len(Main)):
	J = Main[i:].find(sub) + i 
	empty.append(J)


print(empty)


'''




'''
if birthday in file_string:
	print("Your birthday appears in the first %i digits of e!" %decimal_places)

else:
	print("Your birthday does not appear in the first %i digits of e." %decimal_places)
'''



