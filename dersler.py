# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dersler.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from dersplani_islemleri import dersPlaniCek
import  sqlite3 as sql


class Ui_dersPlaniPencere(object):
    def setupUi(self, dersPlaniPencere):
        dersPlaniPencere.setObjectName("dersPlaniPencere")
        dersPlaniPencere.resize(1010, 709)
        dersPlaniPencere.setMinimumSize(QtCore.QSize(1010, 709))
        dersPlaniPencere.setMaximumSize(QtCore.QSize(1010, 709))
        self.centralwidget = QtWidgets.QWidget(dersPlaniPencere)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1010, 710))
        self.tabWidget.setMinimumSize(QtCore.QSize(1010, 710))
        self.tabWidget.setMaximumSize(QtCore.QSize(1010, 710))
        self.tabWidget.setObjectName("tabWidget")
        self.dersPlaniTab = QtWidgets.QWidget()
        self.dersPlaniTab.setObjectName("dersPlaniTab")
        self.dersPlaniTablo = QtWidgets.QTableWidget(self.dersPlaniTab)
        self.dersPlaniTablo.setGeometry(QtCore.QRect(0, 0, 1008, 681))
        self.dersPlaniTablo.setMinimumSize(QtCore.QSize(1008, 681))
        self.dersPlaniTablo.setMaximumSize(QtCore.QSize(1008, 681))
        self.dersPlaniTablo.setObjectName("dersPlaniTablo")
        self.dersPlaniTablo.setColumnCount(5)
        self.dersPlaniTablo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dersPlaniTablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dersPlaniTablo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dersPlaniTablo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dersPlaniTablo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dersPlaniTablo.setHorizontalHeaderItem(4, item)
        self.tabWidget.addTab(self.dersPlaniTab, "")
        self.manuelDersTab = QtWidgets.QWidget()
        self.manuelDersTab.setObjectName("manuelDersTab")
        self.manualTablo = QtWidgets.QTableWidget(self.manuelDersTab)
        self.manualTablo.setGeometry(QtCore.QRect(0, 0, 1008, 681))
        self.manualTablo.setMinimumSize(QtCore.QSize(1008, 681))
        self.manualTablo.setMaximumSize(QtCore.QSize(1008, 681))
        self.manualTablo.setObjectName("manualTablo")
        self.manualTablo.setColumnCount(5)
        self.manualTablo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.manualTablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.manualTablo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.manualTablo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.manualTablo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.manualTablo.setHorizontalHeaderItem(4, item)
        self.tabWidget.addTab(self.manuelDersTab, "")
        dersPlaniPencere.setCentralWidget(self.centralwidget)
        satirsirasi=0
        for index,ders in enumerate(dersPlaniCek("http://www.sis.itu.edu.tr/tr/dersplan/plan/GMI/201810.html")):
            self.dersPlaniTablo.insertRow(satirsirasi)
            for kolonindex, kolon in enumerate([ders.kod,ders.ad,ders.kredi,ders.yariyil]):
                self.dersPlaniTablo.setItem(satirsirasi,kolonindex,QtWidgets.QTableWidgetItem(str(kolon)))
            satirsirasi+=1

        self.retranslateUi(dersPlaniPencere)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(dersPlaniPencere)

    def retranslateUi(self, dersPlaniPencere):
        _translate = QtCore.QCoreApplication.translate
        dersPlaniPencere.setWindowTitle(_translate("dersPlaniPencere", "Ders Planı"))
        item = self.dersPlaniTablo.horizontalHeaderItem(0)
        item.setText(_translate("dersPlaniPencere", "Ders Kodu"))
        item = self.dersPlaniTablo.horizontalHeaderItem(1)
        item.setText(_translate("dersPlaniPencere", "Ders Adı"))
        item = self.dersPlaniTablo.horizontalHeaderItem(2)
        item.setText(_translate("dersPlaniPencere", "Kredi"))
        item = self.dersPlaniTablo.horizontalHeaderItem(3)
        item.setText(_translate("dersPlaniPencere", "Yarıyıl"))
        item = self.dersPlaniTablo.horizontalHeaderItem(4)
        item.setText(_translate("dersPlaniPencere", "Harf Notu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dersPlaniTab), _translate("dersPlaniPencere", "Ders Planındaki Dersler"))
        item = self.manualTablo.horizontalHeaderItem(0)
        item.setText(_translate("dersPlaniPencere", "Ders Kodu"))
        item = self.manualTablo.horizontalHeaderItem(1)
        item.setText(_translate("dersPlaniPencere", "Ders Adı"))
        item = self.manualTablo.horizontalHeaderItem(2)
        item.setText(_translate("dersPlaniPencere", "Kredi"))
        item = self.manualTablo.horizontalHeaderItem(3)
        item.setText(_translate("dersPlaniPencere", "Yarıyıl"))
        item = self.manualTablo.horizontalHeaderItem(4)
        item.setText(_translate("dersPlaniPencere", "Harf Notu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manuelDersTab), _translate("dersPlaniPencere", "Manuel Eklenen Dersler"))
