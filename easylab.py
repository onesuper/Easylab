#!/usr/bin/python
# Filename: easylab.py


version = '0.1'


import time
import easylab_db as db
import sys


class Easylab():
    def __init__(self):
        self.timeFactor = 1000
        self.timeMeassurement = "ms"
        self.conn = db.createConn()
        self.tablename = sys.argv[0][0:sys.argv[0].find(".")]

    def start(self):
        self.start = time.time()

    def end(self):
        self.end = time.time()
        self.elapsedTime = (self.end - self.start) * self.timeFactor
        
    def getElapsedTime(self):
        return self.elapsedTime
    
    def timeStr(self):
        return "%.3f%s" % (self.elapsedTime , self.timeMeassurement)

    def save(self, **attr):
        db.insertOrCreateTable(self.conn, self.tablename, attr)
        
    def __del__(self):
        self.conn.close
        



