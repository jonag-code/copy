import csv

from matplotlib import pyplot as plt
from datetime import datetime 


#filename = 'sitka_weather_07-2014.csv'
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	#print(header_row)

	#for index, column_header in enumerate(header_row):
	#	print(index, column_header)

	dates, highs, lows = [], [], []
	for row in reader:

		highs.append( row[1] )
		lows.append( row[3] )
		
		current_date = datetime.strptime(row[0],"%Y-%m-%d")
		#x = current_date.strftime('%b %Y')
		#print( x )
		dates.append(current_date)

		

highs_float_C = [ (5/9)*(float(value) - 32)  for value in highs]
lows_float_C 	= [ (5/9)*(float(value) - 32)  for value in lows]





fig = plt.figure(dpi = 128, figsize = (10,6))

plt.plot(dates, highs_float_C, c = 'red',  alpha = 1)
plt.plot(dates,lows_float_C, c = 'blue',  alpha = 1 )
plt.fill_between(dates, highs_float_C, lows_float_C, facecolor = 'blue', alpha = 0.1)


plt.title("Daily high temperatures - 2014", fontsize = 24)

fig.autofmt_xdate()

plt.xlabel('', fontsize = 16)


plt.ylabel("Temperature(C)", fontsize = 16)
plt.tick_params(axis= 'both', which = 'major', labelsize = 16)

#fig.xaxis_date()

#plt.xticks(rotation = 30)
plt.show()




'''
date_string = '31-Dec-07'
some_date = datetime.strptime(date_string,"%d-%b-%y")
some_date_2 = datetime.strftime(some_date, "%B %d %Y")
some_date_3 = some_date.strftime("%B %d %Y")


print(some_date)
print(some_date_2)
print(some_date_3)
'''


	
	