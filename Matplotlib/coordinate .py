import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([3,5,7,6,2,6,10,15])
#plt.plot(x,y,'r',lw=2)
#plt.plot(x,y,'r')
plt.bar(x,y,0.2,alpha=1,color='b')
plt.show()
