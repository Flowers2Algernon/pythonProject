import numpy as np
data = np.loadtxt(fname='data mining/data/inflammation-01.csv', delimiter=',')
print(data)
print(type(data))
#find out the type of the data contained in the Numpy array.
print(data.dtype)
#print data's shape
print(data.shape)
print('first value in data:', data[0,0])
print('middle value in data:', data[30,20])
print('last value in data:', data[-1,-1])
print(data[5:10,0:10])
print("---")
# we don't have to include the upper and lower bounds in the slice
small = data[:3,36:]
print(small)
print(small.shape)
print(np.mean(data))