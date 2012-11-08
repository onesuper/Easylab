#!/usr/bin/python
# Filename: easylab.py


version = '0.1'


import time
import sys
import os

import easylab_db as db


class Easylab():

    def __init__(self, name):
        self.name = name
        self.timeFactor = 1000
        self.timeMeassure = "ms"
        self.database = db.EasylabDB()

    def start(self):
        self.start = time.time()

    def end(self):
        self.end = time.time()
        self.elapsedTime = (self.end - self.start) * self.timeFactor
        
    def getElapsedTime(self):
        return self.elapsedTime
    
    def timeStr(self):
        return "%.3f%s" % (self.elapsedTime , self.timeMeassure)

    def log(self, **attr):
        self.database.insertOrCreateTable(self.name, attr)
        

