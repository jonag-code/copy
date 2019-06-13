from jonmodule import Sub_in_main as sbm 
from jonmodule import strconvert
import pygal
import time


s=time.time()


filenames = [ 'pi_30.txt', 'pi_100.txt' ]
len_filenames = len(filenames)


lines =  [''] * len_filenames
str_lines = [''] * len_filenames
for n in range( len_filenames ):
	with open(filenames[n]) as f:
		lines[n] = f.readlines()
	str_lines[n] = strconvert(lines[n])[0:1] + strconvert(lines[n])[2:-1] 

# NOTE: below n = 0, 1 indexes the two lengths of Pi being considered, and  
# x = 0, 1, 2, ..., 9 are the input values to be plotted against. E.g. x vs. F_n(x).

domain = range(0,10)


# Defines an array of Class Instantiations, CL[n][x],
# as made clear in the body of the for loop
CL = [[]] * len_filenames # = [ [], [] ] since len_filenames == 2.

# This list has two elements, Cl[0] = CL[1] = [],
# each of which are empty LISTS, but will soon take form.

for n in range(len_filenames):
	CL[n] = [ sbm(x, str_lines[n] ) for x in domain ]


#Defines an array of Methodized classes: freq[n][x]
freq = [[]] * len_filenames
for n in range(len_filenames):
	freq[n] = [ element.jcount() for element in CL[n] ]


norm_freq = [[]] * len_filenames
for n in range(len_filenames):
	norm_freq[n] = [ 100*element/sum(freq[n]) for element in freq[n] ]



hist = pygal.Bar()
for n in range(len_filenames):
	hist.add('N='+ str( len( str_lines[n]) ), norm_freq[n])

hist.x_labels  = list(domain)
hist.x_title = " Decimals"
hist.y_title = "%"
hist.title = "distrib decimals pi BETTER"

svg_file_name = hist.title.replace(' ','_')
hist.render_to_file( str(svg_file_name) +'.svg')


e=time.time()

print(100*(e-s))


