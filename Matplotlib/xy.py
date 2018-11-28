import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
x = np.array([8000,16000,24000,32000,40000,48000,56000,64000,72000,80000,88000])
y = np.array([61641,61456,61379,61245,61090,61250,61160,61152,61116,60962,61258])
plt.plot(x,y,'r',lw=2)
#plt.plot(x,y,'r')
plt.show()
