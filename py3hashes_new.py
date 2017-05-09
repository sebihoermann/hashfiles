#! /usr/bin/python

# -*- coding: utf-8 -*-
"""
This is a Python 3 Version of hashclasses which tries to make use of pandas...
25.Okt.2016
"""

import csv, pickle
import pandas as pd
from pandas import DataFrame
from time import time
#import re
import os
import threading


class Hashfile(object):
    def __init__(self, filename="/home/sebi/hashes/books.csv", delimiter=","):
        import csv, pickle
        import os
        
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
        self.library = {}
        self.type = "Hashfile"
        
        #csvfiles:

        if type(filename) == str:
            self.csvfile = filename
            self.loadcsv(self.csvfile)
        if type(filename) == list:
            for i in filename:
                self.loadcsv(i)
        #load content:

        self.ebooks = self.generalhash(l=[".pdf", ".mobi", ".epub"])
        self.pythonbooks = self.notsearch(self.ebooks)
        self.totalsize()
        self.topsize()

        self.pdffiles = self.generalhash(l=[".pdf"])
        self.music = self.generalhash(
            l=[".mp3", ".ogg", ".wav", ".flac", ".aiff", ".vox", ".wma"])
    def __type__(self):
        return self.type
    def loadcsv(self, fn):
        """
        Read a .csv file from pfish
        """
        csvfile = fn
        with open(csvfile) as f:
            reader = csv.reader(f, delimiter=",")
            #print reader.next(), " ommitted"
            for row in reader:
                row0 = row[0]
                row8 = row[8]
                row3 = row[3]
                row4 = row[4]
                row5 = row[5]
                row6 = row[6]
                row7 = row[7]
                self.name[row8] = row0

                self.path[row8] = row3
                if "Size" not in row4:
                    row4 = int(row4)
                    self.size[row8] = row4
                    #self.pctsize[row[8]] = float(row[4) / float(self.tsize)
                    # size in KB
                self.modified[row8] = row5
                self.accessed[row8] = row6
                self.created[row8] = row7

        return

    def printtopfiles(self):
        """
        Prints out self.topfiles (largest files) in a nice way.
        """
        l = []
        for item in self.topfiles:
            l.append(self.topfiles[item])
        l.sort(key=lambda x: x[1], reverse=True)
        for i in l:
            for n in i:
                space = abs(int(51 - (len(str(n)[:50]))))
                sb = " " * space
                print(str(n)[:50] + sb, )
            print("\n")

    def topsize(self, level=10):
        """
        Returns the (level) largest Files
        """
        l = [(key, value) for key, value in self.pctsize.items()]
        l = sorted(l, key=lambda x: x[1])
        top = [x[0] for x in l[-level:]]
        self.topfiles = {
            key: (self.name[key], self.size[key], self.pctsize[key])
            for key in top
        }
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
            self.pctsize[key] = round(100 * (float(self.size[key]) /
                                             float(self.tsize)), 5)
            #print self.size[key], self.tsize, pct
        return

    def compare(self, cmp1={}, cmp2={}):
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
                self.doubles[k1] = self.cmp2[k1]
            else:
                self.singles[k1] = self.cmp1[k1]
        self.lensingles = len(self.singles)
        self.lendoubles = len(self.doubles)

    def save(self, d, filename):
        """
        Pickles dict d into filename
        """
        f = open(filename + ".pickle", "wb")
        pickle.dump(f, d)
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
                f = open(ans + ".pickle", "r")
                a = True
            except:
                a = False
        ret = pickle.load(f)
        f.close()
        return ret

    def generalhash(self, l=[".txt"]):
        """
        Simple general search function:
            -keyword is list
        """
        self.ghash = {}
        for i in l:
            for key in self.path:

                if str(i).upper() in str(self.path[key]).upper():
                    self.ghash[key] = self.path[key]
            return self.ghash

    def exportsearch(self, filename="searchreport.csv"):
        """ 
        Export  self.searchreturn to filename.
        """
        self.scripting(self.searchreturn, filename)

    def notsearch(self, d, s=["PYTHON", "ANACONDA"]):
        """
     Returns a dict of a search in d that contains searchterm but not notterm
     """
        searchterm = s[0]
        notterm = s[1]
        pythonbooks = {}
        for i in d:
            if notterm.upper() in self.path[i].upper():
                pass
            else:
                if searchterm.upper() in self.path[i].upper():
                    pythonbooks[i] = self.path[i]
        return pythonbooks

    def scripting(self, d, filename="output.txt"):
        """
        write d.values() into file filename.
        """
        f = open(filename, "w")

        for i in d.values():
            f.write(i + "\n")

        f.close()

    def cpscripting(
            self,
            d,
            filename="/home/sebi/hashes/cppoker.sh",
            path="/media/sebi/9b087df1-6f01-497c-8e83-0aa1e0086721/pokerbooks"
    ):
        f = open(filename, "w")
        for i in d.values():

            f.write("cp \"" + i + "\" \"" + path + "\"\n")
        f.close()

    def evince(self, path=""):
        s = 'evince "{}"'.format(path)
        print(s)
        return os.system(s)
    def genericExec(self, command, path):
        s = command + ' "{}"'.format(path)
        self.thread = threading.Thread(target =os.system, args = (s,) )
        self.thread.start()
    def nano(self, path=""):
        s = 'nano "{}"'.format(path)
        print(s)
        return os.system(s)
    def libre(self, path = ""):
        s = 'libreoffice "{}"'.format(path)
        print(s)
        return os.system(s)

    def quickEbookSearch(self, text="python"):
        s = self.search(self.ebooks, [text])
        return s

    def quickNotSearch(self, text=("data", "coursera")):
        s = self.notsearch(self.ebooks, searchterm=text[0], notterm=text[1])
        return s

    def search(self, d, s="python"):

        self.searchreturn = {}
    
        for key in d:
            if s.upper() in d[key].upper():
               self.searchreturn[key] = d[key]
        print("Search returned: ", len(self.searchreturn))

    def andsearch(self, d, s=["python", "linux"]):
        self.searchreturn = {}
        for key in d:
            if (s[0].upper() in d[key].upper()) and (
                    s[1].upper() in d[key].upper()):
                self.searchreturn[key] = d[key]
        print("Search returned: ", len(self.searchreturn))

    def popeye(self, d={}):
        if d == {}:
            d = self.searchreturn
        resp = False
        for i in d.keys():
            value = d[i]
            resp = self.areYouSure(
                "Are you sure you want to add {} to the Library?".format(
                    value))
            if resp == True:
                self.library[i] = value
            else:
                pass
        return

    def areYouSure(self, q="Are you sure  you want to continue? (y/n)?"):
        print(q)
        ans = input(">")
        if ans.upper() == "Y" or ans == "YES":
            return True
        else:
            return False

    def addToLibrary(self, d):
        for keys in d:
            self.library[key] = d[key]

    def loadLibrary(self, filename="./library.pickle"):
        print("I will load: ", filename)
        resp = self.areYouSure(
            "Are you sure you want to load {} as the library?".format(
                filename))
        if resp == True:
            with open(filename, "rb") as f:
                self.library = pickle.load(f)
        else:
            resp2 = self.areYouSure("Do you want to change filename?")
            if resp2 == True:
                print("please enter a filename:")
                input(resp3)
                self.loadLibrary(resp2)
            else:
                return 0

    def saveLibrary(self, filename="./library.pickle"):
        print("I will save the library to: ", filename)
        resp = self.areYouSure(
            "Are you sure you want to load {} as the library?".format(
                filename))
        if resp == True:
            with open(filename, "wb") as f:
                pickle.dump(self.library, f)
        else:
            resp2 = self.areYouSure("Do you want to change filename?")
            if resp2 == True:
                print("please enter a filename:")
                input(resp3)
                self.saveLibrary(resp2)
            else:
                return 0


class Pdhash(Hashfile):
    """
    Subclass of Hashfiles. Uses Pandas. Added Variables starting with pd...
    
    panda Dataframe: self.pd
    
    Variables:
        pdffiles = self.pdpdf
        
        
    """

    def __init__(self, filename):
        pd.options.display.float_format = '{:,.2f}'.format
        if type(filename) == str:

            self.df = pd.read_csv(filename)
        if type(filename) == list:
            print("its a list!")
            dfs = []
            for i in filename:
                print("concatting {}".format(i))
                dfs.append(pd.read_csv(i))
            self.df = pd.concat(dfs, ignore_index=True)
        
        self.df = self.df[["File", "Size", "Path", "MD5"]]
        super(Pdhash, self).__init__(filename)
        self.type = "Pdhash"
        self.pdpdf = self.contains()
        self.pdebooks = self.containsmore(container=[".pdf", ".mobi", ".epub"])
        self.pdmusic = self.containsmore(container=[".mp3", ".wav"])
        self.countDoubles()
    def __type__(self):
        return self.type
    def describe(self):
        """
        Calls pandas describe function on the class internal dataframe
        """
        return self.df.describe()

    def containsmore(self, cname="Path", container=list()):
        """
        Calls the pandas contains function several times and appends it to a 
        Dataframe which is returned.
        """
        ret = pd.DataFrame()
        for i in container:
            ret = ret.append(self.contains(cname, i))
        return ret

    def contains(self, cname="Path", container=".pdf"):
        """
        Simple search, selecting columns by String.
        """
        return self.df[self.df[cname].str.contains(container)]

    def sort(self, df, by="freq", asc=False):
        """
        Sorts Dataframe by "...", with Asc = True/False
        Returns: Sorted Dataframe
        """
        return df.sort([by], ascending=asc)

    def countDoubles(self, flagsort=True):
        """
        Adds a column "freq" counting the frequency of the Hashes
        returns sorted df
        """
        self.df["freq"] = self.df.groupby("MD5")["MD5"].transform("count")

        return self.sort(self.df, by="freq", asc=False)

    def findByHash(self, hash=""):
        """
        Finds row of specified Hash.
        Returns a List
        """
        return list(self.df.Path[self.df.MD5 == hash].values)

    def scriptRm(self, l=list()):
        """
        Makes a DELETE bash-script called rmen.sh
        returns 0
        """
        with open("./rmen.sh", "w") as f:
            for i in l:
                f.write('rm "{}"\n'.format(i))

        return 0

    def moreDoublesThen(self, c=1):
        """
        Returns a df where freq >c
        """
        return self.sort(self.df[self.df["freq"] > c], by="freq", asc=False)
