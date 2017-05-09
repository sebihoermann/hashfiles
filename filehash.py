#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 14:17:22 2017

@author: maluko
"""
import time, os, hashlib
class Filehash(object):
    def __init__(self, filename, mode = "md5"):
        self.filename = filename
        self.md5 = ""
        self.sha1 = ""
        self.mode = mode
        self.hashfile(filename)
        
    
    def hashfile(self, filename):
        # BUF_SIZE is totally arbitrary, change for your app!
        BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

        md5 = hashlib.md5()
        sha1 = hashlib.sha1()

        with open(self.filename, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                if self.mode == "md5":
                    md5.update(data)
                else:
                    sha1.update(data)

                #print("MD5: {0}".format(md5.hexdigest()))
                #print("SHA1: {0}".format(sha1.hexdigest()))
                self.md5 = md5.hexdigest().upper()
                self.sha1 =sha1.hexdigest().upper()
def walk(path):
        #self.db.createTable()
        
        t = time.time()
        print("Walking the line...")
        l = [".pdf", "epub", "mobi"]
        quicksearch = {}
        counter = 0
        #path = self.lineEdit_3.text()
        for root, dirs, files in os.walk(path):
            for f in files:
                if f[-4:] in l:
                    counter+=1
                    theFile = os.path.join(root,f)
                    rt = time.time()-t
                    print(rt, counter, theFile)
                    try:
                        hashes = Filehash(theFile)
                    except:
                        print("Error: ", theFile)
                #print(hashes)
                
                    quicksearch[hashes.md5] = theFile
        
        print(quicksearch)
        
        print(time.time()-t)
        return quicksearch