#D = {'a':1, 'b': 2, 'c':3 }
D = dict(a=1, b=2, c=3)


for k in D.keys():
	print(k, '->', D[k])
print("\n")


for ke in D:
	print(ke, '->', D[ke])
print("\n")
	

for key in D:
	print('{} -> {}' .format( key, D[key] ))
print("\n")


for (key, value) in D.items():
	print("%s -> %s " %( key, value ))









