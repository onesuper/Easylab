# Filename: easylab_plot.py


import numpy as np
import matplotlib.pyplot as plt


class EasylabPlot():

    def __init__(self):

        self.env = {
            "xlabel" : "",
            "ylabel" : "",
            "title": ""
            }
        self.color = ['#3480C2',
                 '#CC3D3D',
                 '#4CC234',
                 '#dcad1f',
                 '#6f2293',
                 '#C8F291',
                 '#B6E2FA',
                 '#FF7AB0',
                 '#783749']
     
        self.linestyle = ["-",
                          "o-",
                          "x-",
                          ".-",
                          "s-",
                          "+-",
                          "D-",
                          "d-",
                          "*-",
                          "v-",
                          "^-",
                          "<-",
                          ">-",
                          "1-",
                          "2-",
                          "3-",
                          "4-",]

    def bar(self, result, namelist):
        
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
        #ax.grid(True)
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels, loc=0)
        plt.show()
    

    """
    plot a line against a series of (X, Y)
    """
    def plot(self, result, namelist, table):
        if not result:
            return

        X = []
        Y = []
        for r in result:
            X.append(r[0])
            Y.append(r[1])
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlabel(namelist[0])
        ax.set_xticks(X)
        ax.set_xticklabels(X)
        ax.set_ylabel(namelist[1])
        ax.set_title(table)
        ax.grid(True)
        ax.plot(X, Y, "o-")
        plt.show()


    """
    plot several lines in a figure
    """
    def plots(self, result, xlabel, ylabel, namelist):
        if not result:
            return

        M = len(result[0])
        XY = []

        for i in range(M):
            temp = []
            for r in result:
                temp.append(r[i])
            XY.append(temp)

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.grid(True)
        
        # plot lines
        for i in range(1, M):
            ax.plot(XY[0], XY[i], self.linestyle[i], label=namelist[i-1])

        ax.set_xticks(XY[0])
        ax.set_xticklabels(XY[0])
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels, loc=0)
        plt.show()


    def setEnv(self, key, value):
        if not self.env.has_key(key):
            print "there is no environment called", key
        return 
        

    def list(self):
        print self.env
