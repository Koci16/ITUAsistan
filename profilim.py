# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profilim.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Profilim(object):
    def setupUi(self, Profilim):
        Profilim.setObjectName("Profilim")
        Profilim.resize(570, 648)
        Profilim.setMinimumSize(QtCore.QSize(570, 246))
        Profilim.setMaximumSize(QtCore.QSize(570, 1000))
        self.centralwidget = QtWidgets.QWidget(Profilim)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 551, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.ogrenciFakulteCB = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.ogrenciFakulteCB.setObjectName("ogrenciFakulteCB")
        self.verticalLayout.addWidget(self.ogrenciFakulteCB)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.ogrenciBolumCB = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.ogrenciBolumCB.setObjectName("ogrenciBolumCB")
        self.verticalLayout.addWidget(self.ogrenciBolumCB)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.ogrenciDersPlaniCB = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.ogrenciDersPlaniCB.setObjectName("ogrenciDersPlaniCB")
        self.verticalLayout.addWidget(self.ogrenciDersPlaniCB)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.kaydet = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.kaydet.setMinimumSize(QtCore.QSize(0, 41))
        self.kaydet.setObjectName("kaydet")
        self.verticalLayout.addWidget(self.kaydet)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 240, 551, 401))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setEnabled(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 531, 371))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.capFakulteCB = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.capFakulteCB.setObjectName("capFakulteCB")
        self.verticalLayout_3.addWidget(self.capFakulteCB)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.capBolumCB = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.capBolumCB.setObjectName("capBolumCB")
        self.verticalLayout_3.addWidget(self.capBolumCB)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.capPlanCB = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.capPlanCB.setObjectName("capPlanCB")
        self.verticalLayout_3.addWidget(self.capPlanCB)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.yandalBolumCB = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.yandalBolumCB.setObjectName("yandalBolumCB")
        self.verticalLayout_3.addWidget(self.yandalBolumCB)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.yandalPlanCB = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.yandalPlanCB.setObjectName("yandalPlanCB")
        self.verticalLayout_3.addWidget(self.yandalPlanCB)
        self.verticalLayout_2.addWidget(self.groupBox)
        Profilim.setCentralWidget(self.centralwidget)

        self.retranslateUi(Profilim)
        QtCore.QMetaObject.connectSlotsByName(Profilim)

    def retranslateUi(self, Profilim):
        _translate = QtCore.QCoreApplication.translate
        Profilim.setWindowTitle(_translate("Profilim", "Profilim"))
        self.label.setText(_translate("Profilim", "Fakülte"))
        self.label_2.setText(_translate("Profilim", "Bölüm"))
        self.label_3.setText(_translate("Profilim", "Ders Planı"))
        self.kaydet.setText(_translate("Profilim", "Kaydet"))
        self.groupBox.setTitle(_translate("Profilim", "ÇAP / Yandal"))
        self.label_4.setText(_translate("Profilim", "ÇAP Fakülte"))
        self.label_5.setText(_translate("Profilim", "ÇAP Bölüm"))
        self.label_8.setText(_translate("Profilim", "ÇAP Plan"))
        self.label_6.setText(_translate("Profilim", "Yandal Bölüm"))
        self.label_7.setText(_translate("Profilim", "Yandal Plan"))

