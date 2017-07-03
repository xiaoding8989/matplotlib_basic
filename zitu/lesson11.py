import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,100)

plt.subplot(211)

plt.plot(x,np.log(x))


plt.subplot(212)
plt.plot(x,x**x)


plt.show()