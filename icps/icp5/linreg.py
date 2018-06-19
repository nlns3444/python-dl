import numpy as np
import matplotlib.pyplot as plt#for plotting the given points
x=np.array([0,1,2,3,4,5,6,7,8,9])#converts the given list into array
y=np.array([1,3,2,5,7,8,8,9,10,12])
meanx=np.mean(x)#the meanvalue of x will be stored in meanx
meany=np.mean(y)#the meanvalue of y will be stored in meany
num=np.sum((x-meanx)*(y-meany))#calculate the difference between the mean and given value
den=np.sum(pow((x-meanx),2))#squares the difference between given x and meanx
m=num/den#slope calculation
intercept=meany-(m*meanx)
val=(m*x)+intercept#gives us the line equation
plt.plot(x,y)#plots the given x,y values
plt.plot(x,val)
plt.show()#plots the points on the graph