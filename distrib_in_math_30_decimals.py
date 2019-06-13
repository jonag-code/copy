import time

from jonmodule import Sub_in_main as sbm 
from jonmodule import strconvert

import pygal
from pygal.style import Style
#from pygal.style import LightSolarizedStyle, DefaultStyle, RedBlueStyle

#custom_0 = Style(colors=('indigo','tomato','turquoise','steelblue'))
custom_0 = Style(colors=('darkblue', 'teal', 'tomato' ,'black'))
custom_1 = Style(colors=('rgba(255, 0, 0, 0.8)','rgba(50, 0, 255, 0.8)'))
custom_2 = Style(colors=('rgba(100, 255, 0, 0.8)','rgba(100, 0, 255, 0.8)'))
custom_3 = Style(colors=('teal','gold'))

indigo = Style(colors=('rgba(175,0,130,1)'),)
blue = Style(colors=('blue'),)



s=time.time()

filenames = ['pi_30.txt']
#filenames = [ 'pi_30.txt','e_30.txt', 'phi_30.txt', 'sqrt2_30.txt' ]
#filenames = ['pi_30.txt','e_30.txt' ]

#filenames = [ 'phi_30.txt', 'sqrt2_30.txt']


len_filenames = len(filenames)



lines =  [''] * len_filenames
str_lines = [''] * len_filenames
snippet_str =  [''] * len_filenames

for n in range( len_filenames ):
	with open(filenames[n]) as f:
		lines[n] = f.readlines()
	str_lines[n] = strconvert(lines[n])[0:1] + strconvert(lines[n])[2:-1] 
	snippet_str[n] = strconvert(lines[n])[0:-1]

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
	norm_freq[n] = [  100*element/sum(freq[n])  for element in freq[n] ]



hist = pygal.Bar(style = custom_0, legend_at_bottom = True)
hist1 = pygal.Line()

#hist = pygal.Bar(Style = blue)


##for n in range(len_filenames):
##	hist.add('c='+ str( len( str_lines[n]) ), norm_freq[n])

##for n in range(len_filenames):
##	hist.add('c = '+ str(  snippet_str[n]) , freq[n])


#hist.add( math_symbols_pi , freq)

#math_symbols_0 = ['π ≈ 3.14159..',  'e ≈ 2.71828..', 'ϕ ≈ 1.61803..', '√2 ≈ 1.41421..']
#math_symbols_0 = ['π ≈ ' + str(snippet_str[0]) ,  'e ≈ ' + str(snippet_str[1]) ,
# 'ϕ ≈ ' + str(snippet_str[2]), '√2 ≈ ' + str(snippet_str[3])]
math_symbols_0 = ['π ≈ ' + str(snippet_str[0]) ]

math_symbols_1 = ['π ≈ 3.14159..',  'e ≈ 2.71828..']
math_symbols_2 = [ 'ϕ ≈ 1.61803..', '√2 ≈ 1.41421..']





for n in range(len_filenames):
	hist.add( str(math_symbols_0[n]) , freq[n])
	

#hist = pygal.Bar(style = LightSolarizedStyle)
#hist = pygal.Bar(style = DefaultStyle)
#hist = pygal.Bar(style = RedBlueStyle)





hist.x_labels  = list(domain)

#hist.x_title = "Numbers"
#hist.y_title = "Frequency of Numbers"

hist.y_title = "Decimal Number"
hist.x_title = "Frequency of Decimal Number"
#hist.title = "Number Distribution for the First 30 digits of π,  e,  ϕ, √2 "
hist.title = "Results for the First 30 digits of π"
#hist.title = "Results for the First 30 digits of π"

svg_file_name = hist.title.replace(' ','_')
hist.render_to_file( str(svg_file_name) +'PURP' +'.svg')



e=time.time()

print(100*(e-s))


# π,  e,  ϕ, √2




