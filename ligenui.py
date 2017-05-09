#! /home/maluko/anaconda3/bin/python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './hashes/libgen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from libgen import *
#import fileinput
class Ui_Form(object):
    def __init__(self, debug =  True):
        self.debug= debug
        self.p = 1
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1169, 625)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 371, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 3)
        self.getLink = QtWidgets.QPushButton(self.frame)
        self.getLink.setObjectName("getLink")
        self.gridLayout_2.addWidget(self.getLink, 3, 0, 1, 1)
        self.Search = QtWidgets.QPushButton(self.frame)
        self.Search.setObjectName("Search")
        self.gridLayout_2.addWidget(self.Search, 1, 1, 1, 1)
        self.Clear = QtWidgets.QPushButton(self.frame)
        self.Clear.setObjectName("Clear")
        self.gridLayout_2.addWidget(self.Clear, 1, 2, 1, 1)
        self.Lookup = QtWidgets.QPushButton(self.frame)
        self.Lookup.setObjectName("Lookup")
        self.gridLayout_2.addWidget(self.Lookup, 3, 1, 1, 1)
        self.checkDB = QtWidgets.QPushButton(self.frame)
        self.checkDB.setObjectName("checkDB")
        self.gridLayout_2.addWidget(self.checkDB, 3, 2, 1, 1)
        self.writeSearch = QtWidgets.QPushButton(self.frame)
        self.writeSearch.setObjectName("writeSearch")
        self.gridLayout_2.addWidget(self.writeSearch, 2, 1, 1, 1)
        self.Compare = QtWidgets.QPushButton(self.frame)
        self.Compare.setObjectName("Compare")
        self.gridLayout_2.addWidget(self.Compare, 2, 2, 1, 1)
        self.Download = QtWidgets.QPushButton(self.frame)
        self.Download.setObjectName("Download")
        self.gridLayout_2.addWidget(self.Download, 2, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(400, 20, 761, 601))
        self.listWidget.setObjectName("listWidget")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 280, 371, 341))
        self.textBrowser.setObjectName("textBrowser")
        
        #connects:
        self.Search.clicked.connect(self.search)
        self.Clear.clicked.connect(self.clear)
        self.Lookup.clicked.connect(self.listLookup)
        self.writeSearch.clicked.connect(self.write)
        self.Compare.clicked.connect(self.compare)
        self.checkDB.clicked.connect(self.dbcheck)
        self.Download.clicked.connect(self.download)
        self.getLink.clicked.connect(self.nextpage)
        
        
        self.retranslateUi(Form)
        self.lineEdit.returnPressed.connect(self.Search.click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.getLink.setText(_translate("Form", "nextPage"))
        self.Search.setText(_translate("Form", "Search"))
        self.Clear.setText(_translate("Form", "Clear"))
        self.Lookup.setText(_translate("Form", "Lookup"))
        self.checkDB.setText(_translate("Form", "CheckDB"))
        self.writeSearch.setText(_translate("Form", "WriteSearch"))
        self.Compare.setText(_translate("Form", "Compare"))
        self.Download.setText(_translate("Form", "Download"))
    def nextpage(self):
        self.L.lookup = {}
        self.p +=1
        self.L.nextpage(self.p)
        print("page : ", self.p)
        self.output("Page: ", str(self.p))
    def download(self):
        text = self.listWidget.currentItem().text()
        self.output("Choosen:", str(text))
        md5 = self.L.getHash(text)
        self.output("Hash found: ", md5)
        self.L.openDownload(md5)
        
    def dbcheck(self):
        self.dbmissing = {}
        self.dbmissing = self.L.DbLookup()
        self.clear()
        self.listing("Not in DB:")
        self.listing("-----------")
        for key in self.dbmissing:
            self.listing(self.dbmissing[key])
    def compare(self):
        self.L.compareSearch()
        self.clear()
        self.listing("Last searchResult:")
        self.listDict(self.L.lastsearch)
        self.listing("------------------")
        self.listing("New Search missing:")
        self.listMissing()
        self.listing("-------------------")
        self.listing("Lookup:")
        self.listLookup()
    def write(self):
        self.L.writeLastSearch()
    def clear(self):
        self.listWidget.clear()
    def output(self, *words):
        for word in words:
            self.textBrowser.append(word)
    def listing(self, *words):
        for text in words:
            self.listWidget.addItem(text)
    def listDict(self, dic):
        for key in dic:
            self.listing(key)
            self.listing(dic[key])
    def listMissing(self):
        
        for key in self.L.missing:
            self.listing(key)
            self.listing(self.L.missing[key])
    def listLookup(self):
        #self.clear()
        for key in self.L.lookup:
            self.listing(key)
            self.listing(self.L.lookup[key])
    def search(self):
        self.output("Searching...")
        text = self.lineEdit.text()
        self.output("Searchtext: ", text)
        self.L = Libgen(text)
        self.listLookup()
        
        
        

if __name__ == "__main__":
    import sys
#    print ("sysarg", sys.argv)
#    if len(sys.argv)>1:
#        debug = True
#    else:
#        debug = False
#    for line in fileinput.input():
#            print(line)
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

