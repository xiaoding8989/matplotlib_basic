import numpy as np
import matplotlib.pyplot as plt


mu = 10  # mean of distribution
sigma = 20  # standard deviation of distribution
#x = mu + sigma * np.random.randn(2000)
x = np.array([3,10,10,26,25,25,50,50,100])

#plt.hist(x, bins=20,color='red',normed=True)

y1, x1, dummy =plt.hist(x, bins=10,color='green',normed=True)
print x1
plt.show()


# x = np.random.randn(1000)+2
# y = np.random.randn(1000)+3
#
# plt.hist2d(x, y, bins=40)
# plt.show()