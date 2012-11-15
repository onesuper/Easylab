#!/usr/bin/python
# Filename: test_plots.py

import sys
sys.path.append("./src/easylab")
import plot as plt


plot = plt.EasylabPlot()


a = [[1, 2, 3, 4, 5],
     [2, 4, 6, 8, 10],
     [3, 6, 9, 12, 15],
     [4, 8, 12, 16, 20],
     [5, 10, 15, 20, 25]]
b = ["N", "a", "b", "c", "d"]


plot.plots(a, "x", "y", b)
