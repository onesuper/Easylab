#!/usr/bin/python
# Filename: easylab_plot.py


import numpy as np
import matplotlib.pyplot as plt


class EasylabPlot():

    def __init__(self):
        self.color = ['#3480C2',
                 '#CC3D3D',
                 '#4CC234',
                 '#dcad1f',
                 '#6f2293',
                 '#C8F291',
                 '#B6E2FA',
                 '#FF7AB0',
                 '#783749']
        self.title = ""
        self.xlabel = ""
        self.ylabel = ""


    def comparePlot(self, result, namelist):
        
        if not result:
            return

        # [(a,b),(a,b),(a,b)]
        # m = 3,n = 2
        M = len(result[0])
        N = len(result)

        # [(a,b),(a,b),(a,b)] => [[a,a,a],[b,b,b]]
        data = [[] for i in range(M)] 
        for r in result:
            for i in range(M):
                data[i].append(r[i])
    
        #  [[a,a,a],[b,b,b]] => [(a,a,a),(b,b,b)]
        data = [tuple(l) for l in data]

        ind = np.arange(N)
        width = 1 / (M * 2.73)
        fig = plt.figure()
        ax = fig.add_subplot(111)
    
        for i in range(M):
            ax.bar(ind+width*i, data[i], width, color=self.color[i],
                   label=namelist[i])
    
        ax.set_ylabel(self.ylabel)
        ax.set_xlabel(self.xlabel)
        ax.set_title(self.title)
        ax.set_xticklabels([])
        ax.grid(True)
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels, loc=0)
        plt.show()
    
