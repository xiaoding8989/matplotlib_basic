#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/3/14 12:46
@Author  : yading
Theme   :
"""
import matplotlib.dates as mdate
ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
plt.xticks(pd.date_range(demo0719.index[0],demo0719.index[-1],freq='1min'))