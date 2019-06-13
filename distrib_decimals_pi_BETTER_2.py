

from jonmodule import Sub_in_main as sbm 
from jonmodule import strconvert
import pygal
import time


s=time.time()

filenames = [ 'pi_30.txt', 'pi_100.txt' ]

domain = range(0,10)
 

lines =  []
for item in filenames:
	with open(item) as f:
		lines_item = f.readlines() 
		lines.append(lines_item )

str_lines = [] 
for item in lines:
	str_lines_item = strconvert(item)[0:1] + strconvert(item)[2:-1] 
	str_lines.append(str_lines_item)



CL = []
for item in str_lines:
	CL_item = [ sbm(x, item ) for x in domain ]
	CL.append(CL_item)


freq = []
for CL_n in CL:
	freq_n = [ element.jcount() for element in CL_n ]
	freq.append(freq_n)
	

norm_freq = [ ]
for freq_n in freq:
	norm_freq_n = [ 100*element/sum(freq_n) for element in freq_n ]
	norm_freq.append(norm_freq_n)



hist = pygal.Bar()
for item in str_lines:
	n = str_lines.index(item)
	hist.add('N='+ str( len(item) ), norm_freq[n])



hist.x_labels  = list(domain)
hist.x_title = " Decimals"
hist.y_title = "%"
hist.title = "distrib decimals pi BETTER 2"

svg_file_name = hist.title.replace(' ','_')
hist.render_to_file( str(svg_file_name) +'.svg')

e=time.time()

print(100*(e-s))
