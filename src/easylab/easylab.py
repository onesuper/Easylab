# Easylab
# Author: onesuper
# Filename: easylab.py
# Under MIT License

version = '0.1'


import time
import sys
import os


class Easylab():

    def __init__(self, name):
        self.name = name
        self.timeFactor = 1000
        self.timeMeassure = "ms"
        

    def start(self):
        self.start = time.time()

    def end(self):
        self.end = time.time()
        self.elapsedTime = (self.end - self.start) * self.timeFactor
        
    def getElapsedTime(self):
        return self.elapsedTime
    
    def timeStr(self):
        return "%f%s" % (self.elapsedTime , self.timeMeassure)

    def log(self, attrstr):
        sys.stderr.write(self.name)
        sys.stderr.write("\n")
        sys.stderr.write(attrstr)
        
