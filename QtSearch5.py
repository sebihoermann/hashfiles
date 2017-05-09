#! /home/maluko/anaconda3/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from py3hashes_new import Pdhash
import os
import time
from DbHash import *
from filehash import *
from libgen import *
from ligenui import *

class Ui_MainWindow(object):
    def __init__(self):
        self.quicksearch = {}
        self.app = App()
        self.ext = ""
        self.start = time.time()
        self.app.db = DbHash("/home/maluko/hashes/test.db")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1351, 625)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(290, 10, 251, 62))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.SearchButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SearchButton.setObjectName("SearchButton")
        self.gridLayout.addWidget(self.SearchButton, 2, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(550, 10, 241, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ExcludeButtom = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.ExcludeButtom.setObjectName("ExcludeButtom")
        self.gridLayout_2.addWidget(self.ExcludeButtom, 3, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 0, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(9, 77, 256, 192))
        self.textBrowser_2.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.0633484 rgba(50, 255, 246, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "font: 63 italic 10pt \"Ubuntu\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(290, 90, 501, 401))
        self.listWidget.setStyleSheet(
            "font: 63 14pt \"Ubuntu\";\n"
            "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.0633484 rgba(50, 255, 246, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.listWidget.setObjectName("listWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 280, 212, 228))
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(
            QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.StatsButton = QtWidgets.QPushButton(self.groupBox)
        self.StatsButton.setObjectName("StatsButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                  self.StatsButton)
        self.ExportButton = QtWidgets.QPushButton(self.groupBox)
        self.ExportButton.setObjectName("ExportButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole,
                                  self.ExportButton)
        self.LibreButton = QtWidgets.QPushButton(self.groupBox)
        self.LibreButton.setObjectName("LibreButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                  self.LibreButton)
        self.CalibreButton = QtWidgets.QPushButton(self.groupBox)
        self.CalibreButton.setObjectName("CalibreButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole,
                                  self.CalibreButton)
        self.CsvButton = QtWidgets.QPushButton(self.groupBox)
        self.CsvButton.setObjectName("CsvButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.CsvButton)
        self.PopButton = QtWidgets.QPushButton(self.groupBox)
        self.PopButton.setObjectName("PopButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                  self.PopButton)
        self.TopSizeButton = QtWidgets.QPushButton(self.groupBox)
        self.TopSizeButton.setObjectName("TopSizeButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                  self.TopSizeButton)
        self.ComDictButton = QtWidgets.QPushButton(self.groupBox)
        self.ComDictButton.setObjectName("ComDictButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole,
                                  self.ComDictButton)
        self.CreateLibraryButton = QtWidgets.QPushButton(self.groupBox)
        self.CreateLibraryButton.setObjectName("CreateLibraryButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole,
                                  self.CreateLibraryButton)
        self.SaveLibraryButton = QtWidgets.QPushButton(self.groupBox)
        self.SaveLibraryButton.setObjectName("Libgen")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole,
                                  self.SaveLibraryButton)
        self.FindHashButton = QtWidgets.QPushButton(self.groupBox)
        self.FindHashButton.setObjectName("FindHashButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole,
                                  self.FindHashButton)
        #        self.label = QtWidgets.QLabel(self.centralwidget)
        #        self.label.setGeometry(QtCore.QRect(20, 40, 56, 17))
        #        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 500, 414, 63))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OpenButton = QtWidgets.QPushButton(self.groupBox_2)
        self.OpenButton.setObjectName("OpenButton")
        self.horizontalLayout.addWidget(self.OpenButton)
        self.AddLibraryButton = QtWidgets.QPushButton(self.groupBox_2)
        self.AddLibraryButton.setObjectName("AddLibraryButton")
        self.horizontalLayout.addWidget(self.AddLibraryButton)
        self.ShowLibrarButton = QtWidgets.QPushButton(self.groupBox_2)
        self.ShowLibrarButton.setObjectName("ShowLibrarButton")
        self.horizontalLayout.addWidget(self.ShowLibrarButton)
        self.PopFromLibraryButton = QtWidgets.QPushButton(self.groupBox_2)
        self.PopFromLibraryButton.setObjectName("PopFromLibraryButton")
        self.horizontalLayout.addWidget(self.PopFromLibraryButton)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(800, 90, 501, 401))
        self.listWidget_2.setObjectName("listWidget_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(720, 520, 171, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 10, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(10, 40, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_2.setStyleSheet("font: 63 10pt \"FreeSans\";\n"
                                       "color: rgb(0, 0, 0);")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(850, 30, 64, 23))
        self.lcdNumber_4.setObjectName("lcdNumber_4")

        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setGeometry(QtCore.QRect(80, 20, 64, 23))
        self.lcdNumber_5.setObjectName("lcdNumber_5")

        #self.lcdDics()
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(140, 0, 101, 81))
        self.dial.setObjectName("dial")

        self.dial.setMaximum(4)
        self.dial.setMinimum(1)
        self.dial.setValue(1)
        self.dial.raise_()

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(300, 70, 102, 22))
        self.radioButton.setObjectName("AndSearch")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 30, 56, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")

        self.label.setObjectName("label")
        self.gridLayoutWidget.raise_()
        self.gridLayoutWidget_2.raise_()
        self.textBrowser_2.raise_()
        self.listWidget.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        self.groupBox_2.raise_()
        self.listWidget_2.raise_()
        self.lineEdit_3.raise_()
        self.lcdNumber.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1351, 27))
        self.menubar.setObjectName("menubar")
        self.menuSearchbox = QtWidgets.QMenu(self.menubar)
        self.menuSearchbox.setObjectName("menuSearchbox")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSearchbox.menuAction())

        self.retranslateUi(MainWindow)
        self.listWidget.itemActivated['QListWidgetItem*'].connect(
            self.listWidget_2.setFocus)
        self.lineEdit.returnPressed.connect(self.SearchButton.click)
        self.lineEdit_2.returnPressed.connect(self.ExcludeButtom.click)
        self.lineEdit_3.returnPressed.connect(self.AddLibraryButton.click)
        self.CalibreButton.clicked.connect(self.listWidget_2.clear)
        self.CalibreButton.clicked['bool'].connect(self.listWidget.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #connects:
        self.CsvButton.clicked.connect(self.openCsv)
        self.SearchButton.clicked.connect(self.search)
        self.OpenButton.clicked.connect(self.openFromList)
        self.PopButton.clicked.connect(self.popDic)
        self.StatsButton.clicked.connect(self.stats)
        self.ExportButton.clicked.connect(self.export)
        self.LibreButton.clicked.connect(self.libre)
        self.TopSizeButton.clicked.connect(self.topsize)
        self.CalibreButton.clicked.connect(self.clear)
        self.CreateLibraryButton.clicked.connect(self.app.flushDB)
        self.AddLibraryButton.clicked.connect(self.walk)
        self.ExcludeButtom.clicked.connect(self.exclude)
        self.dial.sliderMoved['int'].connect(self.dialEvent)
        self.FindHashButton.clicked.connect(self.hashSearch)
        self.ShowLibrarButton.clicked.connect(self.openDB)
        self.SaveLibraryButton.clicked.connect(self.libgen)
        #self.lcdNumber.digitCount()

        self.retranslateUi(MainWindow)
        self.listWidget.itemActivated['QListWidgetItem*'].connect(
            self.listWidget_2.setFocus)
        self.lineEdit.returnPressed.connect(self.SearchButton.click)
        self.lineEdit_2.returnPressed.connect(self.ExcludeButtom.click)
        self.lineEdit_3.returnPressed.connect(self.AddLibraryButton.click)
        self.CalibreButton.clicked.connect(self.listWidget_2.clear)
        self.CalibreButton.clicked['bool'].connect(self.listWidget.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.listWidget.itemActivated['QListWidgetItem*'].connect(
            self.listWidget_2.setFocus)
        self.lcdDics()
        self.app.readDB()
        self.lcdDics()

    def libgen(self):
        #app = QtWidgets.QApplication(sys.argv)
        self.Libgen = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Libgen)
        self.Libgen.show()

    def popDic(self):
        self.app.popDic()
        self.lcdNumber.display(len(self.app.dicList))
        self.lcdDics()

    def exclude(self):
        self.start = time.time()
        self.output("Hi from exclude!")
        self.ex = self.lineEdit_2.text()
        self.output(self.ex)
        self.clear()
        c = 0
        for k in self.app.searchList:
            for i in k.values():
                #self.output(i)
                if self.ex.upper() not in i.upper():
                    c += 1
                    self.listing2(i)
                    self.listing(os.path.split(i)[1])
        self.lcdTime()
        self.lcdNumber_5.display(str(c))

    def walk(self):
        self.start = time.time()
        self.output("Walking the line...")
        self.clear()
        self.quicksearch = {}
        path = self.openDir()
        self.output(path)
        self.quicksearch = walk(path)
        for key, value in self.quicksearch.items():
            try:
                self.app.db.insertRow(key, value)
            except:
                print("error")
        self.app.db.con.commit()
        self.app.dicList.append(self.quicksearch)
        self.lcdTime()
        self.output("Finished indexing...")

    def toggleHash(self):
        self.listWidget_2.clear()

    def topsize(self):
        for l in self.app.dicList:
            if type(l) is dict:
                self.output("Topsize not available (Dict)!")
            else:
                top = l.topsize()
                for i in top.values():
                    self.output(str(i))

    def clear(self):
        self.listWidget.clear()
        self.listWidget_2.clear()

    def stats(self):
        for i in self.app.dicList:
            if type(i) is dict:
                stats = str(len(i))
            else:
                stats = str(i.describe())
            self.output(stats)
            self.output("LEN: " + str(len(self.app.dicList)))
            self.lcdDics()

    def export(self):
        self.start = time.time()
        with open("searchedText.csv", "w") as f:
            for i in self.app.searchList:
                for value in i.values():
                    f.write(value + "\n")
        self.lcdTime()

    def libre(self):
        self.start = time.time()
        self.export()
        self.app.t.libre(path="searchedText.csv")
        self.lcdTime()

    def dialEvent(self):
        value = self.dial.value()
        #self.output(str(value))
        if value == 1:
            self.ext = ""
        if value == 2:
            self.ext = ".pdf"
        if value == 3:
            self.ext = ".mobi"
        if value == 4:
            self.ext = ".epub"
        self.label.setText(self.ext)
        self.search()

    def search(self):
        self.start = time.time()
        self.app.searchList = []
        text = self.lineEdit.text()
        textlist = text.split()
        if len(textlist) > 0:
            for textitem in textlist:
                self.output(str(textitem))
                self.app.search(str(textitem), self.ext)
        else:
            self.app.search("", self.ext)
        self.listWidget.clear()
        self.listWidget_2.clear()
        er = len(self.app.shortnames)
        self.lcdNumber_5.display(er)
        self.clear()
        for i in self.app.shortnames:
            self.listing(i)
        for i in self.app.longnames:
            self.listing2(i)
        self.lcdTime()

    def openFile(self):
        self.output("Hi from openFile!")
        l = QtWidgets.QFileDialog()
        r = l.getOpenFileName()
        filename = r[0]
        return filename

    def openDir(self):
        dirname = str(QtWidgets.QFileDialog.getExistingDirectory())
        return dirname

    def openFromList(self):
        self.output("Hi from openFromList!")
        text = self.listWidget.currentItem().text()
        self.output("Choosen:", str(text))
        self.app.OpenFromShortName(text)

    def listing(self, *words):
        for text in words:
            self.listWidget.addItem(text)

    def listing2(self, *words):
        for text in words:
            self.listWidget_2.addItem(text)

    def hashSearch(self):
        self.output("Hello from HashSearch!")
        if len(self.app.searchList) < 1:
            self.app.search(term=self.lineEdit.text())
        self.listWidget_2.clear()
        text = self.lineEdit_3.text()
        self.output("Searchterm: ", text)
        m = self.app.searchList[0]
        for key in m:
            if text in key:
                self.listing2(key, m[key])

    def findHash(self):
        self.output("Hello from findHash!")
        h = self.lineEdit_3.text()
        self.output("Searchterm: ", h)
        self.listWidget_2.clear()
        for l in self.app.dicList:
            try:
                if l.type == "Pdhash":
                    for i in l.findbyHash(h):
                        self.listing2(i)
            except:
                pass
            if type(l) == dict:
                for key in l:
                    self.listing2(key, l[key])

    def output(self, *words):
        self.lcdNumber.display(len(self.app.dicList))
        for text in words:
            self.textBrowser_2.append(text)

    def lcdDics(self):
        self.output("----------------------")
        l = int(len(self.app.dicList))
        self.lcdNumber.display(l)
        l2 = 0
        for i in self.app.dicList:
            if type(i) is dict:
                l2 = l2 + len(i)
            else:
                l2 = l2 + len(i.path)
        self.lcdNumber_2.display(l2)

    def lcdTime(self):
        self.stop = time.time()
        self.sec = self.stop - self.start
        self.lcdNumber_4.display(self.sec)

    def openDB(self):
        self.output("Hi from openDB!")
        self.start = time.time()
        filename = self.openFile()
        self.output("filenemae : ", filename)
        self.app.db = DbHash(filename)
        self.app.readDB()
        self.lcdDics()

    def openCsv(self):
        self.output("Hi from openCsv!\n")
        filename = self.openFile()
        self.start = time.time()
        self.output('filename:', filename)
        t = Pdhash(filename)
        self.app.addDic(t)
        self.lcdDics()
        for u in t.path.values():
            self.listing(u + "\n")
        self.lcdTime()
        self.lcdDics()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        self.ExcludeButtom.setText(_translate("MainWindow", "Exclude"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.StatsButton.setText(_translate("MainWindow", "Stats"))
        self.ExportButton.setText(_translate("MainWindow", "Export"))
        self.LibreButton.setText(_translate("MainWindow", "Libre"))
        self.CalibreButton.setText(_translate("MainWindow", "Clear"))
        self.CsvButton.setText(_translate("MainWindow", "CSV"))
        self.PopButton.setText(_translate("MainWindow", "POP"))
        self.TopSizeButton.setText(_translate("MainWindow", "TopSize"))
        self.ComDictButton.setText(_translate("MainWindow", "CompDicts"))
        self.CreateLibraryButton.setText(_translate("MainWindow", "flushDB"))
        self.SaveLibraryButton.setText(_translate("MainWindow", "Libgen"))
        self.FindHashButton.setText(_translate("MainWindow", "FindHash"))
        # self.label.setText(_translate("MainWindow", "Output:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.OpenButton.setText(_translate("MainWindow", "Open"))
        self.AddLibraryButton.setText(_translate("MainWindow", "Add2Library"))
        self.ShowLibrarButton.setText(_translate("MainWindow", "ShowLibrary"))
        self.PopFromLibraryButton.setText(
            _translate("MainWindow", "PopFromLibrary"))
        self.menuSearchbox.setTitle(_translate("MainWindow", "Searchbox"))


class App(object):
    def __init__(self):
        self.dicList = []
        self.searchList = []
        self.shortnames = []
        self.longnames = []
        self.totalDic = {}
        """
        Initialize default Dict Laptop.csv
        """
        self.t = Pdhash("/home/maluko/hashes/laptop.csv")
        #self.dicList.append(self.t)
    def readDB(self):
        self.db.lastTable()
        self.db.loadDB()
        self.totalDic.update(self.db.content)
        self.dicList.append(self.totalDic)

    def flushDB(self):

        self.totalDic = {}
        print("Collecting Dictionary..")
        for dic in self.dicList:
            if type(dic) == dict:
                self.totalDic.update(dic)

            else:
                self.totalDic.update(dic.path)

        print("Writing Data...")
        for key, value in self.totalDic.items():
            try:
                self.db.insertRow(key, value)
            except:
                print("Error:", key, value)

        self.db.con.commit()
        self.dicList = []
        self.dicList.append(self.totalDic)
        try:
            ui.lcdDics()
        except:
            pass

    def popDic(self):
        if len(self.dicList) > 0:
            self.dicList.pop()
            print("Dic poped!")

    def addDic(self, other):
        self.dicList.append(other)

    def search(self, term, ext=""):
        #self.searchList = []
        for t in self.dicList:
            self.searchreturn = {}
            if type(t) is dict:

                for key in t:
                    if term.upper() in t[key].upper():
                        if ext.upper() in t[key].upper():
                            self.searchreturn[key] = t[key]
                print("Search returned: ", len(self.searchreturn))
                self.searchList.append(self.searchreturn)
            else:
                res = t.search(t.path, term)
                for key in t.searchreturn:
                    #print("ext: ", ext.upper(), t.searchreturn[key].upper())
                    if ext.upper() in t.searchreturn[key].upper():
                        self.searchreturn[key] = t.searchreturn[key]
                self.searchList.append(self.searchreturn)
        self.ShortNames()

    def ShortNames(self):
        self.shortnames = []
        self.longnames = []
        for i in self.searchList:
            k = list(i.values())
            for z in k:
                self.longnames.append(z)
                s = os.path.split(z)[1]
                if s in self.shortnames:
                    pass
                else:
                    self.shortnames.append(s)

    def FilenameFromShortName(self, shortname):
        #if len(self.searchlist)>0:
        for i in self.searchList:
            k = list(i.values())
            for z in k:
                if shortname in z:
                    if z[0] == ".":
                        longname = "/home/maluko" + z[1:]
                    else:
                        longname = z
                    print(longname)
                    return str(longname)

    def OpenFromShortName(self, shortname):
        f = self.FilenameFromShortName(shortname)
        print(f)
        if f[-4:] == ".pdf":
            self.t.genericExec("evince", f)

        if f[-5:] == ".epub" or f[-5:] == ".mobi":
            self.t.genericExec("ebook-viewer", f)
        if f[-4:] == ".azw":
            self.t.genericExec("ebook-viewer", f)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
