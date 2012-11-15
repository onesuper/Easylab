#!/usr/bin/python
# Filename: test_plots.py

import sys
sys.path.append("./src/easylab")
import plot as plt


plot = plt.EasylabPlot()


a = [[1, 2, 3, 4, 5, 6],
     [7, 4, 6, 8, 10, 12],
     [33, 6, 9, 12, 15, 18],
     [123, 8, 12, 16, 20, 24],
     [23, 10, 15, 20, 25, 30]]
b = ["N", "a", "b", "c", "d", "e"]

plot.bars(a,"X", "Y",  b)
