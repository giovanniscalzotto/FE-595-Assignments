
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)
w = np.tan(x)

plt.plot(x, y, x, z, x, w)
#plt.xlim(0, 10)
#plt.ylim(-1.1, 1.1)
plt.xlabel('x from 0 to 2*pi', fontsize = 12)
plt.ylabel('Sin, Cos and Tan', fontsize = 12) #ff change label
plt.legend(['Sin', 'Cos', 'Tan'], loc = "upper right", frameon = False, fontsize = 10) #ff change legend
plt.title('Assignment 1', loc='eft', fontsize = 20)

plt.axhline(y=0, color = 'black') #ff add graphical axis
plt.axhline(y=0, color = 'black') #ff add graphical axis
axes = plt.gca() #ff get the current Axes instance
axes.set_ylim([-1.5 , 1.5 ]) #ff ste y axes limit

plt.show()
