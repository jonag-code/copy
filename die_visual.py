from die import Die
import pygal

num_sides = 2
num_rolls = 10000



die = Die(num_sides)


results = []
frequencies = []


for roll_num in range(num_rolls):
	result = die.roll()
	results.append(result)
#print(results)


for value in range(1, die.num_sides +1):
	frequency = results.count(value)
	frequencies.append(frequency)

#print(frequencies)

#list1 = ['car','boat', 'car', 'dog','car']
#print(list1.count('car'))
#print(list(range(3)))
#print(list(range(1,3)))

hist = pygal.Bar()


hist.title = "Results of rolling one D%i %i times" %(num_sides, num_rolls)
#hist.x_labels = ['1','2','3','4','5', '6']
hist.x_labels = [str(n+1) for n in range(num_sides )]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')


xlabel_list = list( range(1, die.num_sides +1) )
#print(xlabel_list[1])
#print(xlabel_list)


'''
somelist1  = [str(2) for n in range(3)]
somelist2  = ["2" for n in range(3)]

##Clearly both of these are superior in clarity than somelist3.
## str() runs into less probles than " "


somelist3 = []
for n in range(3):
	somelist3.append("2")

somelist4 = [str(n  + 1)  for n in range(num_sides )]



print(somelist1)
print(somelist2)
print(somelist3)
print(somelist4)
 '''














