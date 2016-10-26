#! /usr/bin/python

# -*- coding: utf-8 -*-
"""
This is a Python 3 Version of hashclasses which tries to make use of pandas...
25.Okt.2016
"""


import csv, pickle
import pandas as pd
from pandas import DataFrame, Series
from time import time
import re


class Hashfile(object):

    def __init__(self, filename = "/home/sebi/hashes/books.csv", delimiter = ","):
        import csv, pickle
        from os import system 
        
        self.csvfile = filename
        
        self.name = {}
        self.path = {}
        self.delimiter = delimiter
        self.size = {}
        self.modified = {}
        self.accessed = {}
        self.created = {}
        self.singles = {}
        self.doubles = {}
        self.cmp1 = {}
        self.cmp2 = {}
        self.singles = {}
        self.doubles = {}
        self.pythonbooks = {}
        self.searchreturn = {}  
        self.ghash = {}
        self.pctsize = {}
        self.tsize = 0
        self.topfiles = {}  

        #load content:
        self.loadcsv()
        self.ebooks = self.generalhash(l = [".pdf", ".mobi", ".epub"])
        self.pythonbooks = self.notsearch(self.ebooks)
        self.totalsize()
        self.topsize()
        
        
        self.pdffiles = self.generalhash(l = [".pdf"])
        self.music = self.generalhash(l = [".mp3", ".ogg", ".wav", ".flac", ".aiff", ".vox", ".wma" ])

    def loadcsv(self):
        """
        Read a .csv file from pfish
        """
        with open(self.csvfile) as f:
                reader = csv.reader(f, delimiter = self.delimiter)
                #print reader.next(), " ommitted"
                for row in reader:
                         self.name[row[8]] = row[0]
                         
                         self.path[row[8]] = row[3]
                         if "Size" not in row[4]:
                             row[4] = int(row[4])
                             self.size[row[8]] = row[4]
                             #self.pctsize[row[8]] = float(row[4) / float(self.tsize)
                             # size in KB
                         self.modified[row[8]] = row[5]
                         self.accessed[row[8]] = row[6]
                         self.created[row[8]] = row[7]
        
        return 
    def printtopfiles(self):
        """
        Prints out self.topfiles (largest files) in a nice way.
        """
        l = []
        for item in self.topfiles:
            l.append(self.topfiles[item])
        l.sort(key = lambda x : x[1], reverse = True)
        for i in l:
            for n in i:
                space  = abs(int(51-(len(str(n)[:50]))))
                sb = " "*space
                print (str(n)[:50]+ sb,)
            print ("\n")
    def topsize(self, level = 10):
        """
        Returns the (level) largest Files
        """
        l = [(key, value) for key, value in self.pctsize.items()]
        l = sorted(l, key = lambda x : x[1])
        top = [x[0] for x in l[-level:]]
        self.topfiles = {key:(self.name[key], self.size[key], self.pctsize[key]) for key in top}
        return self.topfiles        

    def find_fuckinghuge(self):
        """
        Finds the max(self.size.values())
        Returns a tuple of (size, path, hash)
        """
        fuckinghuge = max(self.size.values())
        f = [x for x in self.size.keys() if self.size[x] == fuckinghuge]
        return self.size[f[0]], self.path[f[0]], f
    def totalsize(self):
        """
        Calculates total Size of all files, stores it in self.tsize
        """
        self.tsize = sum(self.size.values())
        for key in self.size:
            #pct = float()
            self.pctsize[key] = round(100*(float(self.size[key]) / float(self.tsize)), 5)
            #print self.size[key], self.tsize, pct
        return
    def compare(self, cmp1 = {}, cmp2 = {}):
         """
        Compares two dictionaries and stores:
            - Stores valuess in both dicts in self.doubles
            - Stores values only in dict1 in singles
            - Stores length of self.soubles in self.lendoubles
            - Stores length of self.singles in self.lensingles
         """
         self.singles = {}
         self.doubles = {}
         self.cmp1 = cmp1
         self.cmp2 = cmp2
         for k1 in self.cmp1:
            if k1 in self.cmp2:
                self.doubles[k1]=self.cmp2[k1]
            else:
                self.singles[k1]=self.cmp1[k1]
         self.lensingles = len(self.singles)
         self.lendoubles = len(self.doubles)

    def save(self, d, filename):
        """
        Pickles dict d into filename
        """
        f = open(filename+".pickle", "w")
        pickle.dump(d, f)
        f.close()
    def load(self):
        """
        Ask for input and loads and returns pickled-file 
        """
        system("ls")
        a = False
        while a == False:
           ans = input(">")
           try:
               f = open(ans+".pickle","r")
               a = True
           except:
               a = False
        ret= pickle.load(f)
        f.close()
        return ret
    def generalhash(self, l = [".txt"]):
        """
        Simple general search function:
            -keyword is list
        """
        self.ghash = {}
        for i in l:
            for key in self.path:
                
                if str(i).upper() in str(self.path[key]).upper():
                    self.ghash[key]=self.path[key]
            return self.ghash
    def exportsearch(self, filename = "searchreport"):
        """ 
        Export  self.searchreturn to filename.
        """
        self.scripting(self.searchreturn, filename)
    def notsearch(self, d, searchterm = "PYTHON", notterm = "ANACONDA"):
     """
     Returns a dict of a search in d that contains searchterm but not notterm
     """
     pythonbooks = {}
     for i in d:
        if notterm.upper() in self.path[i].upper():
            pass
        else:
            if searchterm.upper() in self.path[i].upper():
                pythonbooks[i] = self.path[i]
     return pythonbooks
    def scripting(self, d, filename = "output.txt"):
        """
        write d.values() into file filename.
        """
        f = open(filename, "w")
    
        for i in d.values():
            f.write(i+"\n")
       
        f.close()
    def cpscripting(self, d, filename = "/home/sebi/hashes/cppoker.sh", path = "/media/sebi/9b087df1-6f01-497c-8e83-0aa1e0086721/pokerbooks"):
        f = open(filename, "w")
        for i in d.values():
        
            f.write("cp \""+i+"\" \""+path+"\"\n")
        f.close()
    def search(self, d,s = ["python"]):
        
        self.searchreturn = {}
        for i in s:
            for key in d:
                if i.upper() in d[key].upper():
                    self.searchreturn[key] = d[key]
        print( "Search returned: ", len(self.searchreturn))
             
        
class Pdhash(Hashfile):
    """
    Subclass of Hashfiles. Uses Pandas. Added Variables starting with pd...
    
    panda Dataframe: self.pd
    
    Variables:
        pdffiles = self.pdpdf
        
        
    """
    def __init__(self, filename):
        self.csvfile = filename
        pd.options.display.float_format = '{:,.2f}'.format
        self.df = pd.read_csv(self.csvfile)
        self.df = self.df[["File","Size", "Path", "MD5"]]
        super(Pdhash,self).__init__(filename)
        
        self.pdpdf = self.contains()
        self.pdebooks = self.containsmore(container = [".pdf", ".mobi", ".epub"])
        self.pdmusic = self.containsmore(container=[".mp3", ".wav"] )
        
    def describe(self):
        """
        Calls pandas describe function on the class internal dataframe
        """
        return self.df.describe()
    def containsmore(self, cname = "Path", container = list()):
        """
        Calls the pandas contains function several times and appends it to a 
        Dataframe which is returned.
        """
        ret = pd.DataFrame()
        for i in container:
            ret= ret.append(self.contains(cname, i))
        return ret
    def contains(self, cname = "Path", container = ".pdf"):
        """
        Simple search, selecting columns by String.
        """
        return self.df[self.df[cname].str.contains(container)]
        


