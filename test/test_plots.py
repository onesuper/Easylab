#!/usr/bin/python
# Filename: test_plots.py

import sys
sys.path.append("..")
sys.path.append(".")
import easylab_plot as plt


plot = plt.EasylabPlot()


a = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
     [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
     [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
     [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
     [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
b = ["N", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]


plot.plots(a, "x", "y", b)
