#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/3/16 13:42
@Author  : yading
Theme   :
"""
import matplotlib.pyplot as plt

import numpy as np
from pylab import *

x=np.arange(-5.0,5.0,0.002)
y1=np.sin(x)

plt.figure(1)
plt.subplot(211)
plt.plot(x,y1)

plt.subplot(212)
xlim(-2.5,2.5)
ylim(-1,1)

plt.plot(x,y1)

plt.show()