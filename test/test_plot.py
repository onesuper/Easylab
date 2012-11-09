#!/usr/bin/python
# Filename: test_plot.py

import sys
sys.path.append("..")
sys.path.append(".")
import easylab_plot as plt


plot = plt.EasylabPlot()



a = [[1, 2],
     [2, 4],
     [3, 23],
     [4, 54],
     [5, 33]]
b = ["a", "b"]



plot.plot(a, b, "title")
