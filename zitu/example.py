#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/3/14 9:10
@Author  : yading
Theme   :
"""
import numpy as np
import matplotlib.pyplot as plt

plt.subplot(221) #分成2x2，占用第一个，即第一行第一列的子图
plt.subplot(222) #分成2x2，占用第二个，即第一行第二列的子图
plt.subplot(212) # 分成2x1，占用第二个，即第二行

plt.show()
