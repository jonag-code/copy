from jonmodule import Sub_in_main as sbm 
from jonmodule import strconvert
import pygal



#filenames = ['e_2000000.txt', 'e_1000.txt', 'e_100.txt', 'e_30.txt' ]
filenames = ['e_1000.txt', 'e_100.txt', 'e_30.txt' ]
filenames = list(reversed(filenames))
len_filenames = len(filenames)
lines =  [''] * len_filenames
pi_str = [''] * len_filenames
 


for n in range( len_filenames ):
	with open(filenames[n]) as f:
		lines[n] = f.readlines()
	pi_str[n] = strconvert(lines[n])[0:1] + strconvert(lines[n])[2:-1] 

# NOTE: below n = 0, 1, 2 indexes the three lengths of Pi being considered, and  
# x = 0, 1, 2, ..., 9 are the input values to be plotted against. E.g. x vs. F_n(x).

domain = range(0,10)

#Defines an array of Class Instantiations: CL[n][x]
CL = [ [] ] * len_filenames
for n in range(len_filenames):
	CL[n] = [ sbm(x, pi_str[n] ) for x in domain ]


#Defines an array of Methodized classes: freq[n][x]
freq = [ [] ] * len_filenames
for n in range(len_filenames):
	freq[n] = [ element.jcount() for element in CL[n] ]
	#freq[n] = [ CL[n][x].jcount() for x in domain ]


norm_freq = [ [] ] * len_filenames
for n in range(len_filenames):
	norm_freq[n] = [ 100*element/sum(freq[n]) for element in freq[n] ]


# From their uses inside the for loops AT a given n: CL[n], freq[n] and norm_freq[n] 
# are actually a 'list' of numbers, F_n <-> [ F_n(0), F_n(1), ..., F_n(9)) ] :

'''
print( len( V[0] ) )
print( len( V[1] ) )
print( len( V[2] ) )

print( len(freq[0]) )
print( len(freq[1]) )
print( len(freq[2]) )

print( len(norm_freq[0]) )
print( len(norm_freq[1]) )
print( len(norm_freq[2]) )
'''

# MATH ASIDE:
# A function over a continuous-valued domain can be thought of as an infinite discrete list,
# as the discrete values 'get closer' or as you 'zoom out'.

hist = pygal.Bar()
for n in range(len_filenames):
	hist.add('N='+ str( len(pi_str[n]) ), freq[n])

hist.x_labels  = list(domain)
hist.x_title = " Decimals"
hist.y_title = "Count"
hist.title = "Un-Normalized Distribution of Decimals in N digits of e part 2"

svg_file_name = hist.title.replace(' ','_')


hist.render_to_file( str(svg_file_name) +'.svg')
#xlabel_list = list(R)