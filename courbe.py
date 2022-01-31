#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
def g():
    	x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
	y1 = np.array([3,3,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,8,7,4])
	y2 = np.array([103,203,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,-92,-93,-96])
	plt.plot(x, y1)
	plt.plot (x, y2)
	plt.show()
g()


