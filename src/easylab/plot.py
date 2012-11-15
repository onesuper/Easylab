# Easylab
# Author: onesuper
# Filename: easylab_plot.py
# Under MIT License

import numpy as np
import matplotlib.pyplot as plt


"""
Please see the website of matplotlib
"""
LINE_STYLE = ["-",
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

COLOR = ['#1d72aa',
         '#c44440',
         '#8cbb4e',
         '#795892',
         '#0099b2',
         '#f38533',
         '#8baad1',
         '#FF7AB0',
         '#783749']

class EasylabPlot():


    def __init__(self, color=COLOR, linestyle=LINE_STYLE):

        self.env = {
            "xlabel" : "",
            "ylabel" : "",
            "title": ""
            }
        self.color = color
        self.linestyle = linestyle


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
        offset = -0.5 / 2.73;

        fig = plt.figure()
        ax = fig.add_subplot(111)
    
        for i in range(M):
            ax.bar(ind+width*i+offset, data[i], width, color=self.color[i],
                   label=namelist[i])
    
        if self.env["title"] != "":
            ax.set_title(self.env["title"])
        if self.env["xlabel"] != "":
            ax.set_xlabel(self.env["xlabel"])
        if self.env["ylabel"] != "":
            ax.set_ylabel(self.env["ylabel"])

        ax.set_xticks(ind)
        ax.set_xticklabels(ind)
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
        ax.set_xticks(X)
        ax.set_xticklabels(X)
        ax.grid(True)

        ax.set_xlabel(namelist[0])
        ax.set_ylabel(namelist[1])
        ax.set_title(table)
        
        if self.env["title"] != "":
            ax.set_title(self.env["title"])
        if self.env["xlabel"] != "":
            ax.set_xlabel(self.env["xlabel"])
        if self.env["ylabel"] != "":
            ax.set_ylabel(self.env["ylabel"])

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
        
        # plot lines
        for i in range(1, M):
            ax.plot(XY[0], XY[i], self.linestyle[i-1], label=namelist[i-1])

        ax.set_xticks(XY[0])
        ax.set_xticklabels(XY[0])
        ax.set_xlabel(xlabel) 
        ax.set_ylabel(ylabel)
        ax.grid(True)

        if self.env["title"] != "":
            ax.set_title(self.env["title"])
        if self.env["xlabel"] != "":
            ax.set_xlabel(self.env["xlabel"])
        if self.env["ylabel"] != "":
            ax.set_ylabel(self.env["ylabel"])

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels, loc=0)
        plt.show()


    def bars(self, result, xlabel, ylabel, namelist):
        if not result:
            return

        M = len(result[0])
        N = len(result)

        XY = []
        for i in range(M):
            temp = []
            for r in result:
                temp.append(r[i])
            XY.append(temp)

        # plot bars
        ind = np.arange(N)
        width = 1 / ( (M-1) * 2.73)
        
        fig = plt.figure()
        ax = fig.add_subplot(111)

        for i in range(1, M):
            offset = - 0.5 / 2.73
            ax.bar(ind+width*(i-1)+offset, XY[i] , width,
                   color=self.color[i-1], label=namelist[i-1])

        ax.set_xticks(ind)
        ax.set_xticklabels(XY[0])
        ax.set_xlabel(xlabel) 
        ax.set_ylabel(ylabel)

        if self.env["title"] != "":
            ax.set_title(self.env["title"])
        if self.env["xlabel"] != "":
            ax.set_xlabel(self.env["xlabel"])
        if self.env["ylabel"] != "":
            ax.set_ylabel(self.env["ylabel"])

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels, loc=0)
        plt.show()     
        
        

    def setEnv(self, key, value):
        if not self.env.has_key(key):
            print "no env called %s" % key
        else:
            self.env[key] = value
        return 
    
    def unsetEnv(self, name):
        if not self.env.has_key(name):
            print "no env called %s" % name
        else:
            self.env[name] = ""
        return

    def list(self):
        print self.env
