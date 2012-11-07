#!/usr/bin/python
# Filename: easylab_db.py

db_name = "easylab.db"

import sqlite3


def insertOrCreateTable(conn, tablename, data):
    createTable(conn, tablename, data)
    insertDict(conn, tablename, data)
    

def insertDict(conn, tablename, data):
    try:
        cursor = conn.cursor()
    	fields = data.keys()
    	values = data.values()
    	placeholder = "?"
    	fieldlist = ",".join(fields)
    	placeholderlist = ",".join([placeholder]*len(fields))
    	query = "INSERT INTO %s(%s) values (%s)" % (tablename, fieldlist,
                                                placeholderlist)
        cursor.execute(query, values)
        conn.commit()
    except sqlite3.OperationalError, e:
        print e
        

def showTable(conn, tablename):
    try:
        # show colum names
        cursor = conn.cursor()
        query = "PRAGMA table_info([%s])" % tablename
        cursor.execute(query)
        fieldlist =  cursor.fetchall()
        if len(fieldlist) > 0:
            for t in fieldlist:
                 print str(t[1]) + "\t|",
            print "\n", 

        # show the values
        query = "SELECT * FROM %s" % tablename
        cursor.execute(query)
        result = cursor.fetchall()
        printfResult(result)

    except sqlite3.OperationalError, e:
        print e

def createTable(conn, tablename, data):
    try:
    	cursor = conn.cursor()
    	fields = data.keys()
    	fieldlist = ",".join(fields)
    	query = "CREATE TABLE IF NOT EXISTS %s(%s)" % (tablename, fieldlist)
    	cursor.execute(query)
    	conn.commit()
    except sqlite3.OperationalError, e:
        print e
        
def createConn():
    return sqlite3.connect(db_name)


def dropTable(conn, tablename):
    try:
        cursor = conn.cursor()
        query = "DROP TABLE %s" % tablename
        cursor.execute(query)
        conn.commit()
    except sqlite3.OperationalError, e:
        print e


def query(conn, query):
     try:
         cursor = conn.cursor()
         cursor.execute(query)
         result = cursor.fetchall()
         printfResult(result)
     except sqlite3.OperationalError, e:
         print e


def printfResult(result):
    for row in result:
        for col in row:
            print str(col) + "\t|",
        print "\n",
