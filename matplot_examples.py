import matplotlib.pyplot as plt

X= [x**2 for x in range(10)]
Y= [y**3 for y in range(10)]

plt.plot(X,Y, 'ro')
plt.plot(X,Y, linestyle = 'solid')

#plt.plot(Y, 'b')
plt.axis([0,100,0,1000])
plt.show()



