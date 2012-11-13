# Filename: easylab_db.py


"""
NOTE:

"""


import sqlite3
import os


COLUMN_WIDTH = 12

class EasylabDB():

    def __init__(self):
        dbpath = os.environ["HOME"] + "/.esaylab"
        self.conn = sqlite3.connect(dbpath)


    def __del__(self):
        self.conn.close()

    def showTables(self):
        return self.query("SELECT NAME FROM sqlite_master WHERE type='table' ORDER BY name;")


    def insertOrCreateTable(self, table, data):
        self.createTable(table, data)
        self.insertDict(table, data)


    def insertDict(self, table, data):
        try:
            cursor = self.conn.cursor()
            fields = data.keys()
            values = data.values()
            placeholder = "?"
            fieldlist = ",".join(fields)
            placeholderlist = ",".join([placeholder]*len(fields))
            query = "INSERT INTO %s(%s) values (%s)" % (table, fieldlist,
                                                placeholderlist)
            cursor.execute(query, values)
            self.conn.commit()
        except sqlite3.OperationalError, e:
            print e
        

    def showTable(self, table):
        try:
            # show colum names
            cursor = self.conn.cursor()
            query = "PRAGMA table_info([%s])" % table
            cursor.execute(query)
            fieldlist =  cursor.fetchall()
            if len(fieldlist) > 0:
                for t in fieldlist:
                    print str(t[1]).rjust(COLUMN_WIDTH) + "|",
                print "\n", 

            # show the values
            query = "SELECT * FROM %s" % table
            cursor.execute(query)
            result = cursor.fetchall()
            printfResult(result)
        except sqlite3.OperationalError, e:
            print e


    def createTable(self, table, data):
        if not data:
            print "data is empty"
            return
        try:
            cursor = self.conn.cursor()
            fields = data.keys()
            fieldlist = ",".join(fields)
            query = "CREATE TABLE IF NOT EXISTS %s(%s)" % (table, fieldlist)
            cursor.execute(query)
            self.conn.commit()
        except sqlite3.OperationalError, e:
            print e
        

    def dropTable(self, table):
        try:
            cursor = self.conn.cursor()
            query = "DROP TABLE %s" % table
            cursor.execute(query)
            self.conn.commit()
        except sqlite3.OperationalError, e:
            print e


    def query(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except sqlite3.OperationalError, e:
            print e

    


def printfResult(result):
    if not result:
        return
    for row in result:
        for col in row:
            print str(col).rjust(COLUMN_WIDTH) + "|",
        print "\n",
