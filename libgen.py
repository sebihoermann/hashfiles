#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 10:47:12 2017

@author: maluko
"""
#import urllib
from bs4 import BeautifulSoup
#import codecs
import os
import pickle
import socks
import socket
from urllib import request
from DbHash import *
import hashlib
from filehash import *
import time
class Libgen(object):
    def __init__(self, search = "python"):
        self.db = DbHash("/home/maluko/hashes/test.db")
        self.db.loadDB()
        self.loadDb()
        self.search = search
        self.start = time.time()
        #self.debug = debug
        self.text = {}
        self.md5 = []
        self.titles = []
        self.hrefs = []
        self.tds = []
        self.lookup = {}
        self.lastsearch = {}
        self.downloadlink = ""
        self.missing= {}
        self.page = """
        http://libgen.io/search.php?&req={}&phrase=1&view=simple&column=def&sort=year&sortmode=DESC
        """.format(self.search)
        

        socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
        socket.socket = socks.socksocket
        #r = request.urlopen('http://icanhazip.com')
        #print(r.read()) # check ips
#        import urllib2
        #print(urllib2.urlopen('http://icanhazip.com').read())
#        if self.debug ==True:
#        try:
#                with open("soup.txt","r") as f:
#                    self.soup = BeautifulSoup(f)
#                f.close()
#                self.getTD()
#                print("Soup Cached!")
#        except:
#                self.payload = request.urlopen(self.page)
#                r = self.payload.readlines()
#                self.soup = BeautifulSoup(r)
#                print(self.soup)
#                self.getTD()
#                with open("soup.txt", "w") as f:
#                    f.write(r)
#                f.close()
#        else:
        self.payload = request.urlopen(self.page)
        #r = self.payload.readlines()
        self.soup = BeautifulSoup(self.payload)
        print(self.soup)
        self.getTD()
#        with open("soup.txt", "w") as f:
#            f.write(r)
#        f.close()
    def tstart(self):
        self.start = time.time()
    def timit(self):
        t = time.time()-self.start
        print("Timespent: ", t)
    def loadDb(self):
        self.tstart()
        self.dbcontent = {}
        for row in self.db.content:
            self.dbcontent[row[0]] = row [1]
        self.timit()
        print(self.dbcontent)
    def LookUp(self, hashvalue):
        #self.tstart()
        #self.already={}
        if hashvalue not in self.dbcontent:
            #self.already[hashvalue] = row[1]
            self.DbMissing[hashvalue] = self.lookup[hashvalue]
        else:
            self.already[hashvalue] = self.lookup[hashvalue]
        #self.timit()
    def lookupHashDb(self, hashvalue):
        #self.tstart()
        #self.already = {}
        #self.already = {}
        for row in self.db.content:
            if hashvalue == row[0]:
                #print ("Already there: ", row[0], row[1])
                self.already[hashvalue]= row[1]
        #self.timit()
    def nextpage(self, page):
        self.tstart()
        self.lookup = {}
        self.page = """
        http://libgen.io/search.php?&req={}&phrase=1&view=simple&column=def&sort=def&sortmode=ASC&page={}
        """.format(self.search, page)
        self.payload = request.urlopen(self.page)
        #r = self.payload.readlines()
        self.soup = BeautifulSoup(self.payload)
        print(self.soup)
        self.getTD()
        self.timit()
    def openDownload(self, md5):
        self.getDownloadLink(md5)
        s = "google-chrome '{}'".format(self.downloadlink)
        os.system(s)
    def writeLastSearch(self):
        self.tstart()
        filename = "/home/maluko/hashes/Libgen_"+self.search+".txt"
        f = open(filename, "wb")
        pickle.dump(self.lookup,f)
        f.close()
        self.timit()
    def lastSearch(self):
        self.tstart()
        filename = "/home/maluko/hashes/Libgen_"+self.search+".txt"
        f=open(filename, "rb")
        self.lastsearch = pickle.load(f)
        self.timit()
    def compareSearch(self):
        self.tstart()
        #if self.lastSearch == {}:
        self.lastSearch()
        if self.lookup == {}:
            self.getTD()
        for m in self.lookup.keys():
            if m in self.lastsearch.keys():
                print(m, "  ..checked")
            else:
                print(m, "  not in LastSearch!")
                self.missing[m]= self.lookup[m]
                print(self.lookup[m])
        f = open("missingbooks.txt","w")
        for item in self.missing:
            f.write(item)
            f.write("\n")
            f.write(self.missing[item])
            f.write("\n")
        f.close()
        out = open("missingdump.pickle", "wb")
        pickle.dump(self.missing,out)
        out.close()
        self.timit()
    def DbLookup(self):
        self.tstart()
        self.already = {}
        self.DbMissing = {}
        for m in self.lookup:
            self.LookUp(m)
        for key in self.lookup:
            if key not in self.lookup:
                self.DbMissing[key] = self.lookup[key]
        self.timit()
        return self.DbMissing
        
        
#    def DbLookup(self):
#        #self.tstart()
#        self.already = {}
#        self.DbMissing = {}
#        for m in self.lookup:
#            self.lookupHashDb(m)
#        for key in self.lookup:
##            if key in self.already:
##                pass
#            if key not in self.already:
#                self.DbMissing[key] = self.lookup[key]
        #self.timit()
        return self.DbMissing
        
    def getHash(self, name):
        self.tstart()
        for key in self.lookup:
            if name in self.lookup[key]:
                return key
        self.timit()
    def getDownloadLink(self, md5):
        part = "book/index.php?md5={}".format(md5)
        self.downloadlink = "http://libgen.io/"+part
        return self.downloadlink
    def getTD(self):
        self.tstart()
        self.lookup = {}
        self.hrefs = []
        self.td = []
        self.text = {}
        self.aHref = []
        self.titles = []
        self.md5 = []
        self.hrefs = self.soup.find_all("a")
        self.tds = self.soup.find_all("td", {"width":"500"})
        for item in self.soup.find_all("td", {"width":"500"}):
            self.titleText=item.text
            self.aHref = item.find("a")
            self.text[self.titleText] = self.aHref
            print(self.titleText)
            print(self.aHref)
            
            print("\n")
        print(self.text)
        m = list(self.text.values())
        for item in m:
            if "md5" in str(item):
                s = str(item).split('"')
                fin = s[1].split("=")
                print(fin[1])
                self.md5.append(fin[1])
            if "title"in str(item):
                title = str(item).split("=")
                p =title[4].split(">")
                for p2 in p:
                    p3 =p2.split("<")
                    if '"' not in p3[0] and len(p3[0])>3:
                        print(p3[0])
                        self.titles.append(p3[0])
        for o in range(len(self.md5)):
            self.lookup[self.md5[o]]= self.titles[o]
        print(self.md5)
        print(self.titles)
        print (self.lookup)
        self.timit()
        
                