import os,re
import matplotlib.pyplot as plt
import numpy as np
# str="2018-10-25 13:11:43,210-AI-INFO- : iter:[88000] loss:[61258.3932163] overall acc:[0.948962379958] -[score.py:58]"
# testname=re.findall(r"\[(.+?)\]",str)
# print(testname)
# print(testname[0])
# print(testname[1])
# print(testname[2])
# print(testname[3])
str=[]
str1=[]
str2=[]
iterNumPlt=[]
lossPlt=[]
meanaccPlt=[]
flog=open('imageAItest.log','r')
for line in flog.readlines():
	str.append(line.replace("\n",''))
print(len(str))

for i in range(0,len(str)):
	if i%2==0:
		str1.append(str[i])

for i in range(0,len(str)):
	if i%2==1:
		str2.append(str[i])
print(len(str1))
print(str1)
print("*********************************************************************")
print(len(str2))
print(str2)

for i in range(0,len(str1)):
	str1re=str1[i]
	teststr=re.findall(r"\[(.+?)\]",str1re)
	iterNum=teststr[0]
	loss=teststr[1]
	iterNumPlt.append(teststr[0])
	lossPlt.append(float(teststr[1]))
	print(iterNum)
	print(loss)

for i in range(0,len(str2)):
	str2re=str2[i]
	teststr=re.findall(r"\[(.+?)\]",str2re)
	meanacc=teststr[0]
	meanaccPlt.append(float(teststr[0]))
	print(meanacc)
	
x = np.array(iterNumPlt)
y = np.array(lossPlt)
z = np.array(meanaccPlt)
print("*********************************************************************")
print(x)
print("*********************************************************************")
print(y)
print("*********************************************************************")
print(z)

plt.plot(x,y,'r',lw=2)
plt.show()
plt.plot(x,z,'y',lw=2)
plt.show()
	

