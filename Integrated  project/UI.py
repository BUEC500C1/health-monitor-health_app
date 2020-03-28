
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Reading_data import sensor_get
import threading 
import sys 
import trace 
import time 


class thread_with_trace(threading.Thread): 
  def __init__(self, *args, **keywords): 
    threading.Thread.__init__(self, *args, **keywords) 
    self.killed = False
  
  def start(self): 
    self.__run_backup = self.run 
    self.run = self.__run       
    threading.Thread.start(self) 
  
  def __run(self): 
    sys.settrace(self.globaltrace) 
    self.__run_backup() 
    self.run = self.__run_backup 
  
  def globaltrace(self, frame, event, arg): 
    if event == 'call': 
      return self.localtrace 
    else: 
      return None
  
  def localtrace(self, frame, event, arg): 
    if self.killed: 
      if event == 'line': 
        raise SystemExit() 
    return self.localtrace 
  
  def kill(self): 
    self.killed = True



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(60, 30, 451, 251))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_p = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_p.setObjectName("label_p")
        self.horizontalLayout_3.addWidget(self.label_p)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Pu = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_Pu.setObjectName("label_Pu")
        self.horizontalLayout.addWidget(self.label_Pu)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_O = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_O.setObjectName("label_O")
        self.horizontalLayout_2.addWidget(self.label_O)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 26))
        self.menubar.setObjectName("menubar")
        self.menumain = QtWidgets.QMenu(self.menubar)
        self.menumain.setObjectName("menumain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menumain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, value1='None', value2='None', value3='None'):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_p.setText(_translate("MainWindow", "Blood pressure"))
        self.label_3.setText(_translate("MainWindow", value3))
        self.label_Pu.setText(_translate("MainWindow", "Pulse"))
        self.label_2.setText(_translate("MainWindow", value2))
        self.label_O.setText(_translate("MainWindow", "Blood Oxygen"))
        self.label.setText(_translate("MainWindow", value1))
        self.menumain.setTitle(_translate("MainWindow", "main"))




def show_real_sensor_data(data):
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    def update_label():
      # getting data every 0.5s
      Blood_pressure = data[0]
      Blood_Oxygen = data[1]
      Pulse = data[2]

      ui.label.setText(Blood_Oxygen)
      ui.label_2.setText(Pulse)
      ui.label_3.setText(Blood_pressure)
      
    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(500)  # 0.5 s

    if not app.exec_():
        return 0
