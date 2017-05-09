#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 13:00:55 2017

@author: maluko
"""
import sqlite3
class DbHash(object):
    def __init__(self, database = "/home/maluko/hashes/books.db"):
        self.counter = 0
        self.database = database
        self.tablename = ""
        self.content = {}
        self.type = "DbHash"
        self.tableprefix = "books_"
        
        try:
            self.con = sqlite3.connect(self.database)
            self.cur = self.con.cursor()
            #self.cur.execute('SELECT SQLITE_VERSION()')
            #data = cur.fetchone()
            #print "SQLite version: %s" % data
        except:
            print ("Error")
#            sys.exit(1)
#        finally:
#            if con:
#                con.close()
        #self.createDB()
        self.lastTable()
        
    def outputTable(self):
        self.loadDB()
        for row in self.content:
            print(row[0], row[1])
        
    def loadTable(self, tablename):
        self.tablename = tablename
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.cur.execute("SELECT * FROM {}".format(self.tablename))
        self.content = self.cur.fetchall()
#        for row in self.content:
#            print ("{} , {}".format (row["hashes"], row["names"]))
    def loadDB(self):
        
        self.loadTable(self.tablename)
    def __type__(self):
        return self.type
    def lastTable(self):
        self.getTables()
        if len(self.tables) >0:
            self.tablename = self.tables[-1][0]
        else:
            self.createDB()
        print(self.tablename)
    def dropLastTable(self):
        self.lastTable()
        self.dropTable(self.tablename)
    def selectHash(self, query):
        self.con.row_factory = sqlite3.Row
        q = 'SELECT hashes FROM {} WHERE hashes = ?'.format(self.tablename)
        print(q)
        self.cur.execute(q, (query,))
        res = self.cur.fetchall()
        return res
        
    def dropTable(self, name):
        self.cur.execute('DROP TABLE IF EXISTS {}'.format(name))
        self.getTables()
        self.con.commit()
    def insertRow(self, h, n):
        self.cur.execute("INSERT INTO {} (hashes, names ) VALUES (?,?)".format(self.tablename), (h,n))
        self.con.commit()
    def createTable(self, name):
        #name = str(name)
        self.cur.execute('CREATE TABLE {} (hashes TEXT PRIMARY KEY, names TEXT)'.format(name))
        self.con.commit()
    def getTables(self):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        self.tables = self.rows = self.cur.fetchall()
#        if self.tables == []:
#            self.createDB()
    def currentTableNumber(self):
        self.getTables()
        number = self.rows[-1][0].split("_")
        print(number)
        self.currentTable = number[1]
    def newTableName(self):
        self.currentTableNumber()
        self.counter = int (self.currentTable)+1
        self.tablename = self.tableprefix + str(self.counter)
    def createDB(self):
        self.counter +=1
        
        #try:
        self.getTables()
        
        if self.rows == []:
            self.createTable("books_0")
            self.getTables()
        print(self.rows)
        print(self.rows[-1][0])
        if self.rows[-1][0] == "books_0":
            #self.counter  = 0
            
            self.newTableName()
            self.createTable(self.tablename)
        else:
            self.newTableName()

        self.con.commit()