import pygal
from pygal.style import Style 
red = Style(colors=('red',))
blue = Style(colors=('blue',))
gold = Style(colors=('gold',))
teal = Style(colors=('teal',))
turquoise = Style(colors=('turquoise',))
aquamarine = Style(colors=('aquamarine ',))

from die import Die 
from Jmodule import jfilename

number_of_sides_1 = 6
number_of_sides_2 = 6
num_rolls = [100,100]




die_1 = Die(number_of_sides_1)
die_2 = Die(number_of_sides_2)

max_result = die_1.num_sides + die_2.num_sides 


#results = [ ( die_1.roll() + die_2.roll() ) for n in range(num_rolls[0])]
#frequencies_1 = [ results.count(m) for m in range(1, max_result + 1 )]
#norm_frequencies_1 = [ 100*frequency/sum(frequencies_1) for frequency in frequencies_1]


results = [ ( die_1.roll() + die_2.roll() ) for n in range(num_rolls[1])]
frequencies_2 = [ results.count(m) for m in range(1, max_result + 1 )]
#norm_frequencies_2 = [ 100*frequency/sum(frequencies_2) for frequency in frequencies_2]


hist = pygal.Bar(style = blue)

#hist.add("D%i + D%i" %(number_of_sides_1, number_of_sides_2), norm_frequencies)
#hist.add("N = %i" %num_rolls[0], frequencies_1) 
#hist.add("N = %i" %num_rolls[1], frequencies_2) 
hist.add("D%i + D%i"%(number_of_sides_1, number_of_sides_2), frequencies_2) 



#hist.title = "Rolling two dice (D%i + D%i) %i times" %(number_of_sides_1, number_of_sides_2, num_rolls[1])
hist.title = "Rolling two regular dice 100 times" 
hist.x_labels = [str(n) for n in range(1, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Count"

#hist.render_to_file("rolling_D%i-D%i_%i_times_not.svg" %(number_of_sides_1, number_of_sides_2, num_rolls))

hist.render_to_file( jfilename(hist.title, "svg") ) 


