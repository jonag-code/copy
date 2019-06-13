from jonmodule import Sub_in_main as sbm 
from jonmodule import strconvert
import pygal



filenames = ['pi_100.txt', 'pi_1000.txt' ]
len_filenames = len(filenames)
lines =  [''] * len_filenames
pi_str = [''] * len_filenames

for n in range( len_filenames ):
	with open(filenames[n]) as f:
		lines[n] = f.readlines()

	pi_str[n] = strconvert(lines[n])[0:1] + strconvert(lines[n])[2:-1] 



R = range(0,10)  # D = [0,1,2,..,9]
	

V_0 = [ sbm(r, pi_str[0] ) for r in R ]
V_1 = [ sbm(r, pi_str[1] ) for r in R ]
#V_2 = [ sbm(r, pi_str[2] ) for r in R ]


freq_0 = [ element.jcount() for element in V_0 ]
freq_1 = [ element.jcount() for element in V_1 ]
#freq_2 = [ element.jcount() for element in V_2 ]


norm_freq_0 = [100*element/sum(freq_0) for element in freq_0]
norm_freq_1 = [100*element/sum(freq_1) for element in freq_1]
#norm_freq_2 = [100*element/sum(freq_2) for element in freq_2]



hist = pygal.Bar()
hist.add('N='+ str( len(pi_str[0]) ), freq_0)
hist.add('N='+ str( len(pi_str[1]) ), freq_1)
#hist.add('N='+ str( len(pi_str[2]) ), freq_2)


hist.x_labels  = list(R)

hist.x_title = " Decimals"
hist.y_title = "Count"
hist.title = "Un-Normalized Distribution of Decimals in N digits of Pi"



hist.render_to_file('distrib_decimals_pi.svg')
#xlabel_list = list(R)