from math import *
import numpy as np
import matplotlib.pyplot as plt

#prime whether or not
def check(num) :
	count = int(sqrt(num)) + 1;
	for x in xrange(2,count):
		if (num % x == 0):
			return True
	return False

tal = 3000
# plot all natural number in 500 - tal
M = np.linspace(500, tal, tal - 500,endpoint=True)
# plt.figure(figsize=(8,6), dpi=100)
X = np.sin(M) * M
Y = np.cos(M) * M
plt.scatter(Y,X,5, color = 'blue', marker = 'o')

# plot prime number in 500 - tal
M_ = []
for x in xrange(500, tal):
	if (not check(x)):
		M_.append(x)
Y_ = np.sin(M_) * M_
X_ = np.cos(M_) * M_
plt.scatter(Y_,X_,5, color = 'red', marker = 'o')

plt.show()