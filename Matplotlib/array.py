import matplotlib.pyplot as plt
import numpy as np
for i in range(0,20):
	dateone=np.zeros([2])
	dateone[0]=i;
	dateone[1]=i;
	y=np.zeros([2])
	y[0]=20;
	y[1]=i;
	plt.plot(dateone,y,'r',lw=3)
plt.show()

