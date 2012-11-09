#!/usr/bin/python
# Filename: test_bar.py

import sys
sys.path.append("..")
import easylab_plot as plt


plot = plt.EasylabPlot()


# test bar
a = [(1, 2, 3, 3, 23, 12, 23, 12, 30),
     (2, 3, 4, 2, 21, 12, 30, 9, 11),
     (4, 4, 10, 20, 12, 23, 33, 12, 12)]
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plot.bar(a, b)

