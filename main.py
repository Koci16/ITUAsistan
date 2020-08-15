# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from course_grabber import getCourseClasses,getCourseCodes
import random
from itertools import product
from profilim import Ui_Profilim
from dersler import Ui_dersPlaniPencere
from vt_islemleri import *


bolumkodlari=[""]

__vt_veri=[]
with sql.connect("ogrencidb.asistan") as __vt:
    __im = __vt.cursor()
    __im.execute("""SELECT bolumkodu FROM 'bolumkodlari'""")
    for __veri in __im.fetchall():
        __vt_veri.append(__veri[0])
    __vt.commit()

if(len(__vt_veri)>1):
    bolumkodlari += __vt_veri
else:
    bolumkodlari += getCourseCodes()
    bolumkodlari_vt_kaydet([__bkvt for __bkvt in bolumkodlari if __bkvt != ""])

cekilenbolumler={}
alternatiflistesi=[""]
secilidersler=[]
gunler={"Pazartesi":0,
        "Salı":1,
        "Çarşamba":2,
        "Perşembe":3,
        "Cuma":4}

saatler={"0830":0,
         "0900":1,
         "0930":2,
         "1000":3,
         "1030":4,
         "1100":5,
         "1130":6,
         "1200":7,
         "1230":8,
         "1300":9,
         "1330":10,
         "1400":11,
         "1430":12,
         "1500":13,
         "1530":14,
         "1600":15,
         "1630":16,
         "1700":17,
         "1730":18,
         "1800":19
         }


acilanders1_text=""
acilanders2_text=""
acilanders3_text=""
acilanders4_text=""
acilanders5_text=""
acilanders6_text=""
acilanders7_text=""
acilanders8_text=""
acilanders9_text=""
acilanders10_text=""
acilanders11_text=""
acilanders12_text=""
acilanders13_text=""
acilanders14_text=""
acilanders15_text=""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 988)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1150, 988))
        MainWindow.setMaximumSize(QtCore.QSize(1150, 988))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(730, 360, 411, 572))
        self.groupBox.setMinimumSize(QtCore.QSize(401, 572))
        self.groupBox.setMaximumSize(QtCore.QSize(1000, 572))
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.otomatik = QtWidgets.QPushButton(self.groupBox)
        self.otomatik.setObjectName("otomatik")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.otomatik)
        self.alternatifler = QtWidgets.QComboBox(self.groupBox)
        self.alternatifler.setObjectName("alternatifler")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.alternatifler)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 360, 725, 572))
        self.tableWidget.setMinimumSize(QtCore.QSize(725, 572))
        self.tableWidget.setMaximumSize(QtCore.QSize(725, 572))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        for __row in range(0,20):
            for __col in range(0,5):
                self.tableWidget.setItem(__row,__col,QtWidgets.QTableWidgetItem())

        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(27)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(1, 1, 1148, 359))
        self.scrollArea.setMinimumSize(QtCore.QSize(1148, 359))
        self.scrollArea.setMaximumSize(QtCore.QSize(1148, 359))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1145, 580))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, 5, 10, 10)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labeller = QtWidgets.QHBoxLayout()
        self.labeller.setObjectName("labeller")
        self.renkLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.renkLabel.setMaximumSize(QtCore.QSize(68, 16777215))
        self.renkLabel.setObjectName("renkLabel")
        self.labeller.addWidget(self.renkLabel)
        self.bolumLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.bolumLabel.setObjectName("bolumLabel")
        self.bolumLabel.setMaximumSize(QtCore.QSize(148, 16777215))
        self.labeller.addWidget(self.bolumLabel)
        self.dersKoduLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.dersKoduLabel.setObjectName("dersKoduLabel")
        self.dersKoduLabel.setMaximumSize(QtCore.QSize(148, 16777215))
        self.labeller.addWidget(self.dersKoduLabel)
        self.acilanlarLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.acilanlarLabel.setObjectName("acilanlarLabel")

        self.labeller.addWidget(self.acilanlarLabel)
        self.verticalLayout_2.addLayout(self.labeller)
        self.ders1 = QtWidgets.QHBoxLayout()
        self.ders1.setObjectName("ders1")
        self.renk1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk1.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk1.setText("")
        self.renk1.setAutoDefault(False)
        self.renk1.setDefault(False)
        self.renk1.setFlat(False)
        self.renk1.setObjectName("renk1")
        self.ders1.addWidget(self.renk1)
        self.bolumkodu1 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu1.setObjectName("bolumkodu1")
        self.ders1.addWidget(self.bolumkodu1)
        self.derskodu1 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu1.setObjectName("derskodu1")
        self.ders1.addWidget(self.derskodu1)
        self.acilanders1 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders1.setObjectName("acilanders1")
        self.ders1.addWidget(self.acilanders1)
        self.verticalLayout_2.addLayout(self.ders1)
        self.ders2 = QtWidgets.QHBoxLayout()
        self.ders2.setObjectName("ders2")
        self.renk2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk2.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk2.setText("")
        self.renk2.setAutoDefault(False)
        self.renk2.setDefault(False)
        self.renk2.setFlat(False)
        self.renk2.setObjectName("renk2")
        self.ders2.addWidget(self.renk2)
        self.bolumkodu2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu2.setObjectName("bolumkodu2")
        self.ders2.addWidget(self.bolumkodu2)
        self.derskodu2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu2.setObjectName("derskodu2")
        self.ders2.addWidget(self.derskodu2)
        self.acilanders2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders2.setObjectName("acilanders2")
        self.ders2.addWidget(self.acilanders2)
        self.verticalLayout_2.addLayout(self.ders2)
        self.ders3 = QtWidgets.QHBoxLayout()
        self.ders3.setObjectName("ders3")
        self.renk3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk3.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk3.setText("")
        self.renk3.setAutoDefault(False)
        self.renk3.setDefault(False)
        self.renk3.setFlat(False)
        self.renk3.setObjectName("renk3")
        self.ders3.addWidget(self.renk3)
        self.bolumkodu3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu3.setObjectName("bolumkodu3")
        self.ders3.addWidget(self.bolumkodu3)
        self.derskodu3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu3.setObjectName("derskodu3")
        self.ders3.addWidget(self.derskodu3)
        self.acilanders3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders3.setObjectName("acilanders3")
        self.ders3.addWidget(self.acilanders3)
        self.verticalLayout_2.addLayout(self.ders3)
        self.ders4 = QtWidgets.QHBoxLayout()
        self.ders4.setObjectName("ders4")
        self.renk4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk4.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk4.setText("")
        self.renk4.setAutoDefault(False)
        self.renk4.setDefault(False)
        self.renk4.setFlat(False)
        self.renk4.setObjectName("renk4")
        self.ders4.addWidget(self.renk4)
        self.bolumkodu4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu4.setObjectName("bolumkodu4")
        self.ders4.addWidget(self.bolumkodu4)
        self.derskodu4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu4.setObjectName("derskodu4")
        self.ders4.addWidget(self.derskodu4)
        self.acilanders4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders4.setObjectName("acilanders4")
        self.ders4.addWidget(self.acilanders4)
        self.verticalLayout_2.addLayout(self.ders4)
        self.ders5 = QtWidgets.QHBoxLayout()
        self.ders5.setObjectName("ders5")
        self.renk5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk5.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk5.setText("")
        self.renk5.setAutoDefault(False)
        self.renk5.setDefault(False)
        self.renk5.setFlat(False)
        self.renk5.setObjectName("renk5")
        self.ders5.addWidget(self.renk5)
        self.bolumkodu5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu5.setObjectName("bolumkodu5")
        self.ders5.addWidget(self.bolumkodu5)
        self.derskodu5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu5.setObjectName("derskodu5")
        self.ders5.addWidget(self.derskodu5)
        self.acilanders5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders5.setObjectName("acilanders5")
        self.ders5.addWidget(self.acilanders5)
        self.verticalLayout_2.addLayout(self.ders5)
        self.ders6 = QtWidgets.QHBoxLayout()
        self.ders6.setObjectName("ders6")
        self.renk6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk6.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk6.setText("")
        self.renk6.setAutoDefault(False)
        self.renk6.setDefault(False)
        self.renk6.setFlat(False)
        self.renk6.setObjectName("renk6")
        self.ders6.addWidget(self.renk6)
        self.bolumkodu6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu6.setObjectName("bolumkodu6")
        self.ders6.addWidget(self.bolumkodu6)
        self.derskodu6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu6.setObjectName("derskodu6")
        self.ders6.addWidget(self.derskodu6)
        self.acilanders6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders6.setObjectName("acilanders6")
        self.ders6.addWidget(self.acilanders6)
        self.verticalLayout_2.addLayout(self.ders6)
        self.ders7 = QtWidgets.QHBoxLayout()
        self.ders7.setObjectName("ders7")
        self.renk7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk7.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk7.setText("")
        self.renk7.setAutoDefault(False)
        self.renk7.setDefault(False)
        self.renk7.setFlat(False)
        self.renk7.setObjectName("renk7")
        self.ders7.addWidget(self.renk7)
        self.bolumkodu7 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu7.setObjectName("bolumkodu7")
        self.ders7.addWidget(self.bolumkodu7)
        self.derskodu7 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu7.setObjectName("derskodu7")
        self.ders7.addWidget(self.derskodu7)
        self.acilanders7 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders7.setObjectName("acilanders7")
        self.ders7.addWidget(self.acilanders7)
        self.verticalLayout_2.addLayout(self.ders7)
        self.ders8 = QtWidgets.QHBoxLayout()
        self.ders8.setObjectName("ders8")
        self.renk8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk8.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk8.setText("")
        self.renk8.setAutoDefault(False)
        self.renk8.setDefault(False)
        self.renk8.setFlat(False)
        self.renk8.setObjectName("renk8")
        self.ders8.addWidget(self.renk8)
        self.bolumkodu8 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu8.setObjectName("bolumkodu8")
        self.ders8.addWidget(self.bolumkodu8)
        self.derskodu8 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu8.setObjectName("derskodu8")
        self.ders8.addWidget(self.derskodu8)
        self.acilanders8 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders8.setObjectName("acilanders8")
        self.ders8.addWidget(self.acilanders8)
        self.verticalLayout_2.addLayout(self.ders8)
        self.ders9 = QtWidgets.QHBoxLayout()
        self.ders9.setObjectName("ders9")
        self.renk9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk9.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk9.setText("")
        self.renk9.setAutoDefault(False)
        self.renk9.setDefault(False)
        self.renk9.setFlat(False)
        self.renk9.setObjectName("renk9")
        self.ders9.addWidget(self.renk9)
        self.bolumkodu9 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu9.setObjectName("bolumkodu9")
        self.ders9.addWidget(self.bolumkodu9)
        self.derskodu9 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu9.setObjectName("derskodu9")
        self.ders9.addWidget(self.derskodu9)
        self.acilanders9 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders9.setObjectName("acilanders9")
        self.ders9.addWidget(self.acilanders9)
        self.verticalLayout_2.addLayout(self.ders9)
        self.ders10 = QtWidgets.QHBoxLayout()
        self.ders10.setObjectName("ders10")
        self.renk10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk10.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk10.setText("")
        self.renk10.setAutoDefault(False)
        self.renk10.setDefault(False)
        self.renk10.setFlat(False)
        self.renk10.setObjectName("renk10")
        self.ders10.addWidget(self.renk10)
        self.bolumkodu10 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu10.setObjectName("bolumkodu10")
        self.ders10.addWidget(self.bolumkodu10)
        self.derskodu10 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu10.setObjectName("derskodu10")
        self.ders10.addWidget(self.derskodu10)
        self.acilanders10 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders10.setObjectName("acilanders10")
        self.ders10.addWidget(self.acilanders10)
        self.verticalLayout_2.addLayout(self.ders10)
        self.ders11 = QtWidgets.QHBoxLayout()
        self.ders11.setObjectName("ders11")
        self.renk11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk11.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk11.setText("")
        self.renk11.setAutoDefault(False)
        self.renk11.setDefault(False)
        self.renk11.setFlat(False)
        self.renk11.setObjectName("renk11")
        self.ders11.addWidget(self.renk11)
        self.bolumkodu11 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu11.setObjectName("bolumkodu11")
        self.ders11.addWidget(self.bolumkodu11)
        self.derskodu11 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu11.setObjectName("derskodu11")
        self.ders11.addWidget(self.derskodu11)
        self.acilanders11 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders11.setObjectName("acilanders11")
        self.ders11.addWidget(self.acilanders11)
        self.verticalLayout_2.addLayout(self.ders11)
        self.ders12 = QtWidgets.QHBoxLayout()
        self.ders12.setObjectName("ders12")
        self.renk12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk12.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk12.setText("")
        self.renk12.setAutoDefault(False)
        self.renk12.setDefault(False)
        self.renk12.setFlat(False)
        self.renk12.setObjectName("renk12")
        self.ders12.addWidget(self.renk12)
        self.bolumkodu12 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu12.setObjectName("bolumkodu12")
        self.ders12.addWidget(self.bolumkodu12)
        self.derskodu12 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu12.setObjectName("derskodu12")
        self.ders12.addWidget(self.derskodu12)
        self.acilanders12 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders12.setObjectName("acilanders12")
        self.ders12.addWidget(self.acilanders12)
        self.verticalLayout_2.addLayout(self.ders12)
        self.ders13 = QtWidgets.QHBoxLayout()
        self.ders13.setObjectName("ders13")
        self.renk13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk13.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk13.setText("")
        self.renk13.setAutoDefault(False)
        self.renk13.setDefault(False)
        self.renk13.setFlat(False)
        self.renk13.setObjectName("renk13")
        self.ders13.addWidget(self.renk13)
        self.bolumkodu13 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu13.setObjectName("bolumkodu13")
        self.ders13.addWidget(self.bolumkodu13)
        self.derskodu13 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu13.setObjectName("derskodu13")
        self.ders13.addWidget(self.derskodu13)
        self.acilanders13 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders13.setObjectName("acilanders13")
        self.ders13.addWidget(self.acilanders13)
        self.verticalLayout_2.addLayout(self.ders13)
        self.ders14 = QtWidgets.QHBoxLayout()
        self.ders14.setObjectName("ders14")
        self.renk14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk14.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk14.setText("")
        self.renk14.setAutoDefault(False)
        self.renk14.setDefault(False)
        self.renk14.setFlat(False)
        self.renk14.setObjectName("renk14")
        self.ders14.addWidget(self.renk14)
        self.bolumkodu14 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu14.setObjectName("bolumkodu14")
        self.ders14.addWidget(self.bolumkodu14)
        self.derskodu14 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu14.setObjectName("derskodu14")
        self.ders14.addWidget(self.derskodu14)
        self.acilanders14 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders14.setObjectName("acilanders14")
        self.ders14.addWidget(self.acilanders14)
        self.verticalLayout_2.addLayout(self.ders14)
        self.ders15 = QtWidgets.QHBoxLayout()
        self.ders15.setObjectName("ders15")
        self.renk15 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.renk15.setMaximumSize(QtCore.QSize(64, 16777215))
        self.renk15.setText("")
        self.renk15.setAutoDefault(False)
        self.renk15.setDefault(False)
        self.renk15.setFlat(False)
        self.renk15.setObjectName("renk15")
        self.ders15.addWidget(self.renk15)
        self.bolumkodu15 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bolumkodu15.setObjectName("bolumkodu15")
        self.ders15.addWidget(self.bolumkodu15)
        self.derskodu15 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.derskodu15.setObjectName("derskodu15")
        self.ders15.addWidget(self.derskodu15)
        self.acilanders15 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.acilanders15.setObjectName("acilanders15")
        self.ders15.addWidget(self.acilanders15)
        self.verticalLayout_2.addLayout(self.ders15)
        self.verticalLayout_8.addLayout(self.verticalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 26))
        self.menubar.setObjectName("menubar")
        self.menuProfil = QtWidgets.QMenu(self.menubar)
        self.menuProfil.setObjectName("menuProfil")
        self.menuDersler = QtWidgets.QMenu(self.menubar)
        self.menuDersler.setObjectName("menuDersler")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBilgilerim = QtWidgets.QAction(MainWindow)
        self.actionBilgilerim.setObjectName("actionBilgilerim")
        self.actionDers_Plan = QtWidgets.QAction(MainWindow)
        self.actionDers_Plan.setObjectName("actionDers_Plan")
        self.actionNot_Hesapla = QtWidgets.QAction(MainWindow)
        self.actionNot_Hesapla.setObjectName("actionNot_Hesapla")
        self.menuProfil.addAction(self.actionBilgilerim)
        self.menuDersler.addAction(self.actionDers_Plan)
        self.menuDersler.addAction(self.actionNot_Hesapla)
        self.menubar.addAction(self.menuProfil.menuAction())
        self.menubar.addAction(self.menuDersler.menuAction())
        self.bolumkodu1.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu1.setMaximumSize(QtCore.QSize(148, 16777215))
        self.bolumkodu2.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu2.setMaximumSize(QtCore.QSize(148, 16777215))
        self.bolumkodu3.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu3.setMaximumSize(QtCore.QSize(148, 16777215))
        self.bolumkodu4.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu4.setMaximumSize(QtCore.QSize(148, 16777215))
        self.bolumkodu5.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu5.setMaximumSize(QtCore.QSize(148, 16777215))
        self.bolumkodu6.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu6.setMaximumSize(QtCore.QSize(148, 16777215))
        self.bolumkodu7.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu7.setMaximumSize(QtCore.QSize(148, 16777215))
        self.bolumkodu8.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu8.setMaximumSize(QtCore.QSize(148, 16777215))
        self.bolumkodu9.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu9.setMaximumSize(QtCore.QSize(148, 16777215))
        self.bolumkodu10.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu10.setMaximumSize(QtCore.QSize(148, 16777215))
        self.bolumkodu11.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu11.setMaximumSize(QtCore.QSize(148, 16777215))
        self.bolumkodu14.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu14.setMaximumSize(QtCore.QSize(148, 16777215))
        self.bolumkodu13.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu13.setMaximumSize(QtCore.QSize(148, 16777215))
        self.bolumkodu14.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu14.setMaximumSize(QtCore.QSize(148, 16777215))
        self.bolumkodu15.setMaximumSize(QtCore.QSize(148, 16777215))
        self.derskodu15.setMaximumSize(QtCore.QSize(148, 16777215))

        #----------------
        #BÖLÜM KODU DEĞİŞTİ FONKSİYONU
        self.bolumkodu1.currentTextChanged.connect(self.bolumKodu1Degisti)
        self.bolumkodu2.currentTextChanged.connect(self.bolumKodu2Degisti)
        self.bolumkodu3.currentTextChanged.connect(self.bolumKodu3Degisti)
        self.bolumkodu4.currentTextChanged.connect(self.bolumKodu4Degisti)
        self.bolumkodu5.currentTextChanged.connect(self.bolumKodu5Degisti)
        self.bolumkodu6.currentTextChanged.connect(self.bolumKodu6Degisti)
        self.bolumkodu7.currentTextChanged.connect(self.bolumKodu7Degisti)
        self.bolumkodu8.currentTextChanged.connect(self.bolumKodu8Degisti)
        self.bolumkodu9.currentTextChanged.connect(self.bolumKodu9Degisti)
        self.bolumkodu10.currentTextChanged.connect(self.bolumKodu10Degisti)
        self.bolumkodu11.currentTextChanged.connect(self.bolumKodu11Degisti)
        self.bolumkodu12.currentTextChanged.connect(self.bolumKodu12Degisti)
        self.bolumkodu13.currentTextChanged.connect(self.bolumKodu13Degisti)
        self.bolumkodu14.currentTextChanged.connect(self.bolumKodu14Degisti)
        self.bolumkodu15.currentTextChanged.connect(self.bolumKodu15Degisti)
        #----------------
        self.derskodu1.currentTextChanged.connect(self.derskodu1Degisti)
        self.derskodu2.currentTextChanged.connect(self.derskodu2Degisti)
        self.derskodu3.currentTextChanged.connect(self.derskodu3Degisti)
        self.derskodu4.currentTextChanged.connect(self.derskodu4Degisti)
        self.derskodu5.currentTextChanged.connect(self.derskodu5Degisti)
        self.derskodu6.currentTextChanged.connect(self.derskodu6Degisti)
        self.derskodu7.currentTextChanged.connect(self.derskodu7Degisti)
        self.derskodu8.currentTextChanged.connect(self.derskodu8Degisti)
        self.derskodu9.currentTextChanged.connect(self.derskodu9Degisti)
        self.derskodu10.currentTextChanged.connect(self.derskodu10Degisti)
        self.derskodu11.currentTextChanged.connect(self.derskodu11Degisti)
        self.derskodu12.currentTextChanged.connect(self.derskodu12Degisti)
        self.derskodu13.currentTextChanged.connect(self.derskodu13Degisti)
        self.derskodu14.currentTextChanged.connect(self.derskodu14Degisti)
        self.derskodu15.currentTextChanged.connect(self.derskodu15Degisti)
        #----------------
        self.acilanders1.currentTextChanged.connect(self.acilanders1Degisti)
        self.acilanders2.currentTextChanged.connect(self.acilanders2Degisti)
        self.acilanders3.currentTextChanged.connect(self.acilanders3Degisti)
        self.acilanders4.currentTextChanged.connect(self.acilanders4Degisti)
        self.acilanders5.currentTextChanged.connect(self.acilanders5Degisti)
        self.acilanders6.currentTextChanged.connect(self.acilanders6Degisti)
        self.acilanders7.currentTextChanged.connect(self.acilanders7Degisti)
        self.acilanders8.currentTextChanged.connect(self.acilanders8Degisti)
        self.acilanders9.currentTextChanged.connect(self.acilanders9Degisti)
        self.acilanders10.currentTextChanged.connect(self.acilanders10Degisti)
        self.acilanders11.currentTextChanged.connect(self.acilanders11Degisti)
        self.acilanders12.currentTextChanged.connect(self.acilanders12Degisti)
        self.acilanders13.currentTextChanged.connect(self.acilanders13Degisti)
        self.acilanders14.currentTextChanged.connect(self.acilanders14Degisti)
        self.acilanders15.currentTextChanged.connect(self.acilanders15Degisti)

        self.otomatik.clicked.connect(self.otomatikOlustur)
        self.alternatifler.currentIndexChanged.connect(self.alternatifDegisti)

        self.Profilim = QtWidgets.QMainWindow()
        self.profui = Ui_Profilim()
        self.profui.setupUi(self.Profilim)
        self.actionBilgilerim.triggered.connect(self.Profilim.show)

        self.dersPlaniPencere = QtWidgets.QMainWindow()
        self.planui = Ui_dersPlaniPencere()
        self.planui.setupUi(self.dersPlaniPencere)
        self.actionDers_Plan.triggered.connect(self.dersPlaniPencere.show)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def profilPenceresiniGoster(self,text):
    #     profilim.Profilim.show()
    #     pass

    def otomatikOlustur(self):
        global alternatiflistesi
        global secilidersler

        alternatiflistesi=[""]
        self.alternatifler.clear()
        kombinasyonualinacakdersler=[]
        secilikodunacilancb=[]
        for __row in range(0, 20):
            for __col in range(0, 5):
                self.tableWidget.item(__row, __col).setText("")
                self.tableWidget.item(__row, __col).setBackground(QtGui.QColor(255, 255, 255))
        secilidersler=[]
        __silinecekalternatifler=[]
        if(self.cakismaVarmi()):
            self.statusbar.showMessage("Seçtiğin dersler çakışıyor birini bırak.")
        else:
            for index,__acilanderscb in enumerate([self.acilanders1,self.acilanders2,self.acilanders3,self.acilanders4,self.acilanders5,self.acilanders6,self.acilanders7,self.acilanders8,self.acilanders9,self.acilanders10,self.acilanders11,self.acilanders12,self.acilanders13,self.acilanders14,self.acilanders15]):
                __dersler = []
                if(__acilanderscb.currentText()!=""):
                    __crn=__acilanderscb.currentText().split(" | ")[0]
                    for kod in bolumkodlari:
                        if kod in cekilenbolumler:
                            for k in cekilenbolumler[kod]:
                                if k.crn == __crn:
                                    kombinasyonualinacakdersler.append([k])
                else:

                    if (index == 0):
                        if(self.derskodu1.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders1,self.acilanders1.currentText()])
                            __tumcrnler = [self.acilanders1.itemText(i).split(" | ")[0] for i in range(self.acilanders1.count())]

                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)

                    if (index == 1):
                        if(self.derskodu2.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders2,self.acilanders2.currentText()])
                            __tumcrnler = [self.acilanders2.itemText(i).split(" | ")[0] for i in
                                           range(self.acilanders2.count())]
                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)
                    if (index == 2):
                        if(self.derskodu3.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders3,self.acilanders3.currentText()])
                            __tumcrnler = [self.acilanders3.itemText(i).split(" | ")[0] for i in
                                           range(self.acilanders3.count())]
                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)
                    if (index == 3):
                        if(self.derskodu4.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders4,self.acilanders4.currentText()])
                            __tumcrnler = [self.acilanders4.itemText(i).split(" | ")[0] for i in
                                           range(self.acilanders4.count())]
                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)
                    if (index == 4):
                        if(self.derskodu5.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders5,self.acilanders5.currentText()])
                            __tumcrnler = [self.acilanders5.itemText(i).split(" | ")[0] for i in
                                           range(self.acilanders5.count())]
                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)
                    if (index == 5):
                        if(self.derskodu6.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders6,self.acilanders6.currentText()])
                            __tumcrnler = [self.acilanders6.itemText(i).split(" | ")[0] for i in
                                           range(self.acilanders6.count())]
                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)
                    if (index == 6):
                        if(self.derskodu7.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders7,self.acilanders7.currentText()])
                            __tumcrnler = [self.acilanders7.itemText(i).split(" | ")[0] for i in
                                           range(self.acilanders7.count())]
                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)
                    if (index == 7):
                        if(self.derskodu8.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders8,self.acilanders8.currentText()])
                            __tumcrnler = [self.acilanders8.itemText(i).split(" | ")[0] for i in
                                           range(self.acilanders8.count())]
                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)
                    if (index == 8):
                        if(self.derskodu9.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders9,self.acilanders9.currentText()])
                            __tumcrnler = [self.acilanders9.itemText(i).split(" | ")[0] for i in
                                           range(self.acilanders9.count())]
                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)
                    if (index == 9):
                        if(self.derskodu10.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders10,self.acilanders10.currentText()])
                            __tumcrnler = [self.acilanders10.itemText(i).split(" | ")[0] for i in
                                           range(self.acilanders10.count())]
                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)
                    if (index == 10):
                        if(self.derskodu11.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders11,self.acilanders11.currentText()])
                            __tumcrnler = [self.acilanders11.itemText(i).split(" | ")[0] for i in
                                           range(self.acilanders11.count())]
                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)
                    if (index == 11):
                        if(self.derskodu12.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders12,self.acilanders12.currentText()])
                            __tumcrnler = [self.acilanders12.itemText(i).split(" | ")[0] for i in
                                           range(self.acilanders12.count())]
                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)
                    if (index == 12):
                        if(self.derskodu13.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders13,self.acilanders13.currentText()])
                            __tumcrnler = [self.acilanders13.itemText(i).split(" | ")[0] for i in
                                           range(self.acilanders13.count())]
                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)
                    if (index == 13):
                        if(self.derskodu14.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders14,self.acilanders14.currentText()])
                            __tumcrnler = [self.acilanders14.itemText(i).split(" | ")[0] for i in range(self.acilanders14.count())]
                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)
                    if (index == 14):
                        if(self.derskodu15.currentText()!=""):
                            secilikodunacilancb.append([self.acilanders15,self.acilanders15.currentText()])
                            __tumcrnler = [self.acilanders15.itemText(i).split(" | ")[0] for i in range(self.acilanders15.count())]
                            for __crn in __tumcrnler:
                                for kod in bolumkodlari:
                                    if kod in cekilenbolumler:
                                        for k in cekilenbolumler[kod]:
                                            if k.crn == __crn:
                                                __dersler.append(k)
                    if(len(__dersler)>0):
                        kombinasyonualinacakdersler.append(__dersler)
            alternatiflistesi=list(product(*kombinasyonualinacakdersler))
            for __altindex,__alternatif in enumerate(alternatiflistesi):
                for __alternatifders in __alternatif:
                    for __ikincialternatif in __alternatif:
                        if(__alternatifders!=__ikincialternatif):
                            for __birincindex,__birinciningun in enumerate(__alternatifders.day):
                                for __ikincindex,__ikinciningun in enumerate(__ikincialternatif.day):
                                    if(__birinciningun==__ikinciningun):
                                        __saat = __alternatifders.time[__birincindex].split("/")
                                        __ikincisaat = __ikincialternatif.time[__ikincindex].split("/")
                                        __baslangic = [__saat[0][:2], __saat[0][2:4]]
                                        __bitis = [__saat[1][:2], str(int(__saat[1][2:4]) + 1)]
                                        __cakisma=False
                                        if (__bitis[1] == "60"):
                                            __bitis[1] = "00"
                                            __bitis[0] = str(int(__bitis[0]) + 1)
                                            if (int(__bitis[0]) < 10):
                                                __bitis[0] = "0" + __bitis[0]
                                        __imlec = __baslangic
                                        while (__cakisma==False and (int(__bitis[0]) > int(__imlec[0]) or int(__bitis[1]) > int(__imlec[1]))):
                                            __cakismakontrolimleci=__imlec[0]+__imlec[1]
                                            if(int(__cakismakontrolimleci)>=int(__ikincisaat[0]) and int(__cakismakontrolimleci)<=int(__ikincisaat[1])):
                                                __cakisma=True

                                            if (__imlec[1] == "00"):
                                                __imlec[1] = "30"
                                            else:
                                                __imlec[1] = "00"
                                                __imlec[0] = str(int(__imlec[0]) + 1)
                                            if (int(__imlec[0]) < 10):
                                                __imlec[0] = "0" + str(int(__imlec[0]))
                                        if(__cakisma):
                                            try:
                                                # alternatiflistesi.pop(__altindex)
                                                __silinecekalternatifler.append(__alternatif)
                                            except Exception as e:
                                                print("-"*15)
                                                print(e.message,e.args)
                                                print("-"*15)
            for __silinecek in __silinecekalternatifler:
                try:
                    alternatiflistesi.remove(__silinecek)
                    __silinecekalternatifler.remove(__silinecek)
                except Exception as e:
                    print("-" * 15)
                    print(e)
                    print("-" * 15)
            if(len(alternatiflistesi)>0):
                self.alternatifler.addItems([""]+["{}. alternatif".format(i) for i in range(1,len(alternatiflistesi)+1)])


    def alternatifDegisti(self,index):
        if(index!=0 and self.alternatifler.currentText()!=""):
            # while(len(secilidersler)>0):
            #     for __secili in secilidersler:
            #         self.derskaldir(__secili)
            for __acilanderscb in [self.acilanders1, self.acilanders2, self.acilanders3, self.acilanders4, self.acilanders5,
                     self.acilanders6, self.acilanders7, self.acilanders8, self.acilanders9, self.acilanders10,
                     self.acilanders11, self.acilanders12, self.acilanders13, self.acilanders14,
                     self.acilanders15]:
                    __acilanderscb.setCurrentIndex(0)

            for __altders in alternatiflistesi[index-1]:
                #self.dersyerlestir(__altders)
                gun_saat = ""
                for i in range(len(__altders.day)):
                    if i != range(len(__altders.day))[-1]:
                        gun_saat += "{}-{},".format(__altders.day[i], __altders.time[i])
                    else:
                        gun_saat += "{}-{}".format(__altders.day[i], __altders.time[i])
                for index, __acilanderscb in enumerate(
                        [self.acilanders1, self.acilanders2, self.acilanders3, self.acilanders4, self.acilanders5,
                         self.acilanders6, self.acilanders7, self.acilanders8, self.acilanders9, self.acilanders10,
                         self.acilanders11, self.acilanders12, self.acilanders13, self.acilanders14,
                         self.acilanders15]):
                    if(__acilanderscb.count()>0):
                        __acilanderscbtext = [__acilanderscb.itemText(i) for i in range(__acilanderscb.count())]
                        for __textindex,__text in enumerate(__acilanderscbtext):
                            if(__text=="{} | {} | {} | {}".format(__altders.crn,__altders.title,__altders.instructor,gun_saat)):
                                __acilanderscb.setCurrentIndex(__textindex)
                                break





    def dersyerlestir(self,__ders):
        gun_saat = []
        for i in range(len(__ders.day)):
            gun_saat += [[__ders.day[i], __ders.time[i]]]

        for gs in gun_saat:
            __saat=gs[1].split("/")
            __baslangic = [__saat[0][:2], __saat[0][2:4]]
            __bitis = [__saat[1][:2], str(int(__saat[1][2:4])+1)]
            if(__bitis[1]=="60"):
                __bitis[1]="00"
                __bitis[0]=str(int(__bitis[0])+1)
                if (int(__bitis[0]) < 10):
                    __bitis[0] = "0" + __bitis[0]
            __imlec=__baslangic
            while(int(__bitis[0])>int(__imlec[0]) or int(__bitis[1])>int(__imlec[1])):
                # self.tableWidget.item(0,0).background().color().name()#000000
                __ders.cells.append(self.tableWidget.item(saatler[__imlec[0]+__imlec[1]],gunler[gs[0]]))
                if(__imlec[1]=="00"):
                    __imlec[1]="30"
                else:
                    __imlec[1]="00"
                    __imlec[0] = str(int(__imlec[0]) + 1)
                if (int(__imlec[0]) < 10):
                    __imlec[0] = "0" + str(int(__imlec[0]))

        __ders.color.append(random.randint(0,255))
        __ders.color.append(random.randint(0,255))
        __ders.color.append(random.randint(0,255))

        for c in __ders.cells:
            boyalihucreler=[]
            for d in secilidersler:
                boyalihucreler+=d.cells
            if c not in boyalihucreler:
                c.setBackground(QtGui.QColor(__ders.color[0],__ders.color[1],__ders.color[2]))
                c.setText(__ders.code)
            else:
                c.setBackground(QtGui.QColor(139, 0, 0))
                c.setText("ÇAKIŞTI")

        secilidersler.append(__ders)

        if (self.cakismaVarmi()):
            self.statusbar.showMessage("AGA DERSLER ÇAKIŞTI AGA")
        else:
            self.statusbar.showMessage("")

    def derskaldir(self,__ders):
        for __i, __eski in enumerate(secilidersler):
            if(__eski==__ders):
                secilidersler.pop(__i)

        for c in __ders.cells:
            for d in secilidersler:
                if c in d.cells:
                    c.setBackground(QtGui.QColor(d.color[0],d.color[1],d.color[2]))
                    c.setText(d.code)
                else:
                    c.setBackground(QtGui.QColor(255, 255, 255))
                    c.setText("")
            if len(secilidersler)==0:
                for __row in range(0, 20):
                    for __col in range(0, 5):
                        self.tableWidget.item(__row,__col).setText("")
                        self.tableWidget.item(__row,__col).setBackground(QtGui.QColor(255,255,255))
        if(self.cakismaVarmi()):
            self.statusbar.showMessage("AGA DERSLER ÇAKIŞTI AGA")
        else:
            self.statusbar.showMessage("")

    def cakismaVarmi(self):
        cakisma=False
        for __row in range(0, 20):
            for __col in range(0, 5):
                if(self.tableWidget.item(__row,__col).text()=="ÇAKIŞTI"):
                    cakisma=True

        return cakisma



    def acilanders1Degisti(self,acilanders):
        global acilanders1_text
        if acilanders1_text!="":
            crn=acilanders1_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu1.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders1_text=acilanders

    
    def acilanders2Degisti(self,acilanders):
        global acilanders2_text
        if acilanders2_text!="":
            crn=acilanders2_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu2.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders2_text=acilanders

    def acilanders3Degisti(self,acilanders):
        global acilanders3_text
        if acilanders3_text!="":
            crn=acilanders3_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu3.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders3_text=acilanders

    def acilanders4Degisti(self,acilanders):
        global acilanders4_text
        if acilanders4_text!="":
            crn=acilanders4_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu4.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders4_text=acilanders

    def acilanders5Degisti(self,acilanders):
        global acilanders5_text
        if acilanders5_text!="":
            crn=acilanders5_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu5.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders5_text=acilanders

    def acilanders6Degisti(self,acilanders):
        global acilanders6_text
        if acilanders6_text!="":
            crn=acilanders6_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu6.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders6_text=acilanders

    def acilanders7Degisti(self,acilanders):
        global acilanders7_text
        if acilanders7_text!="":
            crn=acilanders7_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu7.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders7_text=acilanders

    def acilanders8Degisti(self,acilanders):
        global acilanders8_text
        if acilanders8_text!="":
            crn=acilanders8_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu8.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders8_text=acilanders

    def acilanders9Degisti(self,acilanders):
        global acilanders9_text
        if acilanders9_text!="":
            crn=acilanders9_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu9.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders9_text=acilanders

    def acilanders10Degisti(self,acilanders):
        global acilanders10_text
        if acilanders10_text!="":
            crn=acilanders10_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu10.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders10_text=acilanders

    def acilanders11Degisti(self,acilanders):
        global acilanders11_text
        if acilanders11_text!="":
            crn=acilanders11_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu11.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders11_text=acilanders

    def acilanders12Degisti(self,acilanders):
        global acilanders12_text
        if acilanders12_text!="":
            crn=acilanders12_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu12.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders12_text=acilanders

    def acilanders13Degisti(self,acilanders):
        global acilanders13_text
        if acilanders13_text!="":
            crn=acilanders13_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu13.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders13_text=acilanders

    def acilanders14Degisti(self,acilanders):
        global acilanders14_text
        if acilanders14_text!="":
            crn=acilanders14_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu14.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders14_text=acilanders

    def acilanders15Degisti(self,acilanders):
        global acilanders15_text
        if acilanders15_text!="":
            crn=acilanders15_text.split(" | ")[0]

            for kod in bolumkodlari:
                if kod in cekilenbolumler:
                    for k in cekilenbolumler[kod]:
                        if k.crn==crn:
                            self.derskaldir(k)
        if acilanders != "":
            crn=acilanders.split(" | ")[0]
            kod=self.bolumkodu15.currentText()
            for k in cekilenbolumler[kod]:
                if k.crn==crn:
                    self.dersyerlestir(k)
                    acilanders15_text=acilanders


    def derskodu1Degisti(self,derskodu):
        acilandersler = [""]
        kod = self.bolumkodu1.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code==derskodu:
                        gun_saat=""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat+="{}-{},".format(k.day[i],k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn,k.title,k.instructor,gun_saat))
                self.acilanders1.clear()
                self.acilanders1.addItems(acilandersler)
            else:
                self.acilanders1.clear()
                self.acilanders1.addItem("***HATA***")

    def derskodu2Degisti(self,derskodu):
        acilandersler = [""]
        kod = self.bolumkodu2.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code==derskodu:
                        gun_saat=""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat+="{}-{},".format(k.day[i],k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn,k.title,k.instructor,gun_saat))
                self.acilanders2.clear()
                self.acilanders2.addItems(acilandersler)
            else:
                self.acilanders2.clear()
                self.acilanders2.addItem("***HATA***")

    def derskodu3Degisti(self, derskodu):
        acilandersler = [""]
        kod = self.bolumkodu3.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code == derskodu:
                        gun_saat = ""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat += "{}-{},".format(k.day[i], k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn, k.title, k.instructor, gun_saat))
                self.acilanders3.clear()
                self.acilanders3.addItems(acilandersler)
            else:
                self.acilanders3.clear()
                self.acilanders3.addItem("***HATA***")

    def derskodu4Degisti(self, derskodu):
        acilandersler = [""]
        kod = self.bolumkodu4.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code == derskodu:
                        gun_saat = ""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat += "{}-{},".format(k.day[i], k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn, k.title, k.instructor, gun_saat))
                self.acilanders4.clear()
                self.acilanders4.addItems(acilandersler)
            else:
                self.acilanders4.clear()
                self.acilanders4.addItem("***HATA***")
    
    def derskodu5Degisti(self,derskodu):
        acilandersler = [""]
        kod = self.bolumkodu5.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code==derskodu:
                        gun_saat=""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat+="{}-{},".format(k.day[i],k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn,k.title,k.instructor,gun_saat))
                self.acilanders5.clear()
                self.acilanders5.addItems(acilandersler)
            else:
                self.acilanders5.clear()
                self.acilanders5.addItem("***HATA***")

    def derskodu6Degisti(self, derskodu):
        acilandersler = [""]
        kod = self.bolumkodu6.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code == derskodu:
                        gun_saat = ""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat += "{}-{},".format(k.day[i], k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn, k.title, k.instructor, gun_saat))
                self.acilanders6.clear()
                self.acilanders6.addItems(acilandersler)
            else:
                self.acilanders6.clear()
                self.acilanders6.addItem("***HATA***")

    def derskodu7Degisti(self, derskodu):
        acilandersler = [""]
        kod = self.bolumkodu7.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code == derskodu:
                        gun_saat = ""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat += "{}-{},".format(k.day[i], k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn, k.title, k.instructor, gun_saat))
                self.acilanders7.clear()
                self.acilanders7.addItems(acilandersler)
            else:
                self.acilanders7.clear()
                self.acilanders7.addItem("***HATA***")

    def derskodu8Degisti(self, derskodu):
        acilandersler = [""]
        kod = self.bolumkodu8.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code == derskodu:
                        gun_saat = ""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat += "{}-{},".format(k.day[i], k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn, k.title, k.instructor, gun_saat))
                self.acilanders8.clear()
                self.acilanders8.addItems(acilandersler)
            else:
                self.acilanders8.clear()
                self.acilanders8.addItem("***HATA***")

    def derskodu9Degisti(self, derskodu):
        acilandersler = [""]
        kod = self.bolumkodu9.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code == derskodu:
                        gun_saat = ""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat += "{}-{},".format(k.day[i], k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn, k.title, k.instructor, gun_saat))
                self.acilanders9.clear()
                self.acilanders9.addItems(acilandersler)
            else:
                self.acilanders9.clear()
                self.acilanders9.addItem("***HATA***")

    def derskodu10Degisti(self, derskodu):
        acilandersler = [""]
        kod = self.bolumkodu10.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code == derskodu:
                        gun_saat = ""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat += "{}-{},".format(k.day[i], k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn, k.title, k.instructor, gun_saat))
                self.acilanders10.clear()
                self.acilanders10.addItems(acilandersler)
            else:
                self.acilanders10.clear()
                self.acilanders10.addItem("***HATA***")

    def derskodu11Degisti(self, derskodu):
        acilandersler = [""]
        kod = self.bolumkodu11.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code == derskodu:
                        gun_saat = ""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat += "{}-{},".format(k.day[i], k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn, k.title, k.instructor, gun_saat))
                self.acilanders11.clear()
                self.acilanders11.addItems(acilandersler)
            else:
                self.acilanders11.clear()
                self.acilanders11.addItem("***HATA***")

    def derskodu12Degisti(self, derskodu):
        acilandersler = [""]
        kod = self.bolumkodu12.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code == derskodu:
                        gun_saat = ""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat += "{}-{},".format(k.day[i], k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn, k.title, k.instructor, gun_saat))
                self.acilanders12.clear()
                self.acilanders12.addItems(acilandersler)
            else:
                self.acilanders12.clear()
                self.acilanders12.addItem("***HATA***")

    def derskodu13Degisti(self, derskodu):
        acilandersler = [""]
        kod = self.bolumkodu13.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code == derskodu:
                        gun_saat = ""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat += "{}-{},".format(k.day[i], k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn, k.title, k.instructor, gun_saat))
                self.acilanders13.clear()
                self.acilanders13.addItems(acilandersler)
            else:
                self.acilanders13.clear()
                self.acilanders13.addItem("***HATA***")

    def derskodu14Degisti(self, derskodu):
        acilandersler = [""]
        kod = self.bolumkodu14.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code == derskodu:
                        gun_saat = ""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat += "{}-{},".format(k.day[i], k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn, k.title, k.instructor, gun_saat))
                self.acilanders14.clear()
                self.acilanders14.addItems(acilandersler)
            else:
                self.acilanders14.clear()
                self.acilanders14.addItem("***HATA***")

    def derskodu15Degisti(self, derskodu):
        acilandersler = [""]
        kod = self.bolumkodu15.currentText()
        if derskodu != "":
            if kod in cekilenbolumler.keys():
                for k in cekilenbolumler[kod]:
                    if k.code == derskodu:
                        gun_saat = ""
                        for i in range(len(k.day)):
                            if i != range(len(k.day))[-1]:
                                gun_saat += "{}-{},".format(k.day[i], k.time[i])
                            else:
                                gun_saat += "{}-{}".format(k.day[i], k.time[i])
                        acilandersler.append("{} | {} | {} | {}".format(k.crn, k.title, k.instructor, gun_saat))
                self.acilanders15.clear()
                self.acilanders15.addItems(acilandersler)
            else:
                self.acilanders15.clear()
                self.acilanders15.addItem("***HATA***")

    def bolumKodu1Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu1.clear()
                self.derskodu1.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu1.clear()
                self.derskodu1.addItems(derskodlari)

    def bolumKodu2Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu2.clear()
                self.derskodu2.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu2.clear()
                self.derskodu2.addItems(derskodlari)

    def bolumKodu3Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu3.clear()
                self.derskodu3.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu3.clear()
                self.derskodu3.addItems(derskodlari)

    def bolumKodu4Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu4.clear()
                self.derskodu4.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu4.clear()
                self.derskodu4.addItems(derskodlari)

    def bolumKodu5Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu5.clear()
                self.derskodu5.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu5.clear()
                self.derskodu5.addItems(derskodlari)

    def bolumKodu6Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu6.clear()
                self.derskodu6.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu6.clear()
                self.derskodu6.addItems(derskodlari)

    def bolumKodu7Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu7.clear()
                self.derskodu7.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu7.clear()
                self.derskodu7.addItems(derskodlari)

    def bolumKodu8Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu8.clear()
                self.derskodu8.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu8.clear()
                self.derskodu8.addItems(derskodlari)

    def bolumKodu9Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu9.clear()
                self.derskodu9.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu9.clear()
                self.derskodu9.addItems(derskodlari)


    def bolumKodu10Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu10.clear()
                self.derskodu10.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu10.clear()
                self.derskodu10.addItems(derskodlari)


    def bolumKodu11Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu11.clear()
                self.derskodu11.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu11.clear()
                self.derskodu11.addItems(derskodlari)


    def bolumKodu12Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu12.clear()
                self.derskodu12.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu12.clear()
                self.derskodu12.addItems(derskodlari)


    def bolumKodu13Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu13.clear()
                self.derskodu13.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu13.clear()
                self.derskodu13.addItems(derskodlari)


    def bolumKodu14Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu14.clear()
                self.derskodu14.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu14.clear()
                self.derskodu14.addItems(derskodlari)


    def bolumKodu15Degisti(self,kod):
        derskodlari = [""]
        if kod!="":
            if kod in cekilenbolumler.keys():
                derskodlari+=[k.code for k in cekilenbolumler[kod]]
                self.derskodu15.clear()
                self.derskodu15.addItems(derskodlari)
            else:
                cekilenbolumler[kod] = getCourseClasses(kod)
                for k in cekilenbolumler[kod]:
                    if k.code not in derskodlari:
                        derskodlari.append(k.code)
                self.derskodu15.clear()
                self.derskodu15.addItems(derskodlari)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "İTÜ Asistan"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Asistan"))
        self.otomatik.setText(_translate("MainWindow", "Otomatik"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "8:30-8:59"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "9:00-9:29"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "9:30-9:59"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "10:00-10:29"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "10:30-10:59"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "11:00-11:29"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "11:30-11:59"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "12:00-12:29"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "12:30-12:59"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "13:00-13:29"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "13:30-13:59"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "14:00-14:29"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "14:30-14:59"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "15:00-15:29"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15:30-15:59"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16:00-16:29"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "16:30-16:59"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "17:00-17:29"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "17:30-17:59"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "18:00-18:29"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pazartesi"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Salı"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Çarşamba"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Perşembe"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cuma"))
        self.renkLabel.setText(_translate("MainWindow", "Renk"))
        self.bolumLabel.setText(_translate("MainWindow", "Bölüm Kodu"))
        self.dersKoduLabel.setText(_translate("MainWindow", "Ders Kodu"))
        self.acilanlarLabel.setText(_translate("MainWindow", "Açılan Dersler"))
        self.menuProfil.setTitle(_translate("MainWindow", "Profilim"))
        self.menuDersler.setTitle(_translate("MainWindow", "Dersler"))
        self.actionBilgilerim.setText(_translate("MainWindow", "Bilgilerim"))
        self.actionDers_Plan.setText(_translate("MainWindow", "Ders Planı"))
        self.actionNot_Hesapla.setText(_translate("MainWindow", "Not Hesapla"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.bolumkodu1.addItems(bolumkodlari)
    ui.bolumkodu2.addItems(bolumkodlari)
    ui.bolumkodu3.addItems(bolumkodlari)
    ui.bolumkodu4.addItems(bolumkodlari)
    ui.bolumkodu5.addItems(bolumkodlari)
    ui.bolumkodu6.addItems(bolumkodlari)
    ui.bolumkodu7.addItems(bolumkodlari)
    ui.bolumkodu8.addItems(bolumkodlari)
    ui.bolumkodu9.addItems(bolumkodlari)
    ui.bolumkodu10.addItems(bolumkodlari)
    ui.bolumkodu11.addItems(bolumkodlari)
    ui.bolumkodu14.addItems(bolumkodlari)
    ui.bolumkodu13.addItems(bolumkodlari)
    ui.bolumkodu14.addItems(bolumkodlari)
    ui.bolumkodu15.addItems(bolumkodlari)

    MainWindow.show()
    sys.exit(app.exec_())
