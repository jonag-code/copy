
#filename = 'pi_1000.txt'
filename = 'pi_100.txt'
#filename = 'pi_30.txt'

##Store  lines of .txt file into a list,
with open(filename) as f:
	lines = f.readlines()
print("%s \n" %lines)


##print an element at a time, stripping
## off the insisible newline characters
## from the original .txt file.
for line in lines:
	#print(line)
	#print(line.strip())
	print(line.rstrip())


##Store lines of .txt file into a list,
## stripping newline and blank spaces.
lines_stripped = [line.strip() for line in lines]
print("\n %s" %lines_stripped)

##Store the contents of txt file as one string (y)
pi_string = ''
for line in lines:
	pi_string = pi_string + line.strip()
	#pi_string += line.strip()



print("\n %s " %pi_string)
print("\n This is Pi to %i decimal places\n" %(len(pi_string) -2 ))
print(type(pi_string))







