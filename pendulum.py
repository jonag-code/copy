from Jmodule import jfilename 

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


sin = np.sin
pi = np.pi 

#Parameter values:
b = 0.0
c = 5.0

#Initial conditions:
offset = 0.1
theta0 = pi - offset
omega0=0.0


timestop = 50
numpoints = 2001
timestep = timestop/ (numpoints - 1)
#timestop is the length of time interval in
#  arbitrary units. 
#numpoints is the number of points in the t array, 
#with numpoints - 1 the number of subintervals.
#timestep is the size of a sub interval. print(timestep)


def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*sin(theta)]
    return dydt


t = np.linspace(0, timestop, numpoints)
y0 = [theta0, omega0]

ysol = odeint(pend, y0, t, args=(b, c))
#print(ysol)


title = 'Angular Position and Angular Velocity'
filename_svg = jfilename(title,'svg')

plt.title(title)
plt.plot(t, ysol[:, 0], 'b', label='$\Theta$(t)')
plt.plot(t, ysol[:, 1], 'g', label='$\omega$(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
#plt.show()
plt.savefig(filename_svg)
plt.close()


title = 'Phase Space of Angular Coordinates'
filename_svg = jfilename(title,'svg')


plt.title(title)
plt.plot(ysol[:, 0], ysol[:, 1], 'orange', label='$\Gamma(t) = \omega(\Theta) $')
plt.legend(loc='best')
plt.xlabel('$\Theta$(t)')
plt.ylabel('$\omega$(t)')
plt.grid()
#plt.show()
plt.savefig(filename_svg)
plt.close()






