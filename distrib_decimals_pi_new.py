from Jmodule import jstring, jfilename, Sub_in_main
sbm = Sub_in_main 
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
	str_lines[n] = jstring(lines[n])[0:1] + jstring(lines[n])[2:-1] 


domain = range(0,10)


CL = [[]] * len_filenames # = [ [], [] ] since len_filenames == 2.

for n in range(len_filenames):
	CL[n] = [ sbm(x, str_lines[n] ) for x in domain ]


freq = [[]] * len_filenames
for n in range(len_filenames):
	freq[n] = [ element.jcount() for element in CL[n] ]


norm_freq = [[]] * len_filenames
for n in range(len_filenames):
	norm_freq[n] = [ 100*element/sum(freq[n]) for element in freq[n] ]



hist = pygal.Bar()
for n in range(len_filenames):
	hist.add('N='+ str( len( str_lines[n]) ), norm_freq[n])

hist.title = "distrib decimals pi new"

hist.x_labels  = list(domain)
hist.x_title = " Decimals"
hist.y_title = "%"

#hist.render_to_file( hist.title + ".svg" )
file_name_svg = jfilename(hist.title, 'svg')
hist.render_to_file( file_name_svg )




e=time.time()

print(100*(e-s))


