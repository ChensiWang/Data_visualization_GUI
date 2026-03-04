import sys
import pandas as pd
import numpy as np
import os
import linecache
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QDateTime
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
from matplotlib.figure import Figure
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-


class UnitForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1120, 767)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        Form.setFont(font)
        Form.setMouseTracking(True)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.showfolder = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showfolder.sizePolicy().hasHeightForWidth())
        self.showfolder.setSizePolicy(sizePolicy)
        self.showfolder.setObjectName("showfolder")
        self.horizontalLayout_5.addWidget(self.showfolder)
        self.folder_path = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folder_path.sizePolicy().hasHeightForWidth())
        self.folder_path.setSizePolicy(sizePolicy)
        self.folder_path.setObjectName("folder_path")
        self.horizontalLayout_5.addWidget(self.folder_path)
        self.Search = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Search.sizePolicy().hasHeightForWidth())
        self.Search.setSizePolicy(sizePolicy)
        self.Search.setObjectName("Search")
        self.horizontalLayout_5.addWidget(self.Search)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.Tool = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tool.sizePolicy().hasHeightForWidth())
        self.Tool.setSizePolicy(sizePolicy)
        self.Tool.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Tool.setEditable(True)
        self.Tool.setObjectName("Tool")
        self.horizontalLayout_2.addWidget(self.Tool)
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Device = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Device.sizePolicy().hasHeightForWidth())
        self.Device.setSizePolicy(sizePolicy)
        self.Device.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Device.setEditable(True)
        self.Device.setObjectName("Device")
        self.horizontalLayout_2.addWidget(self.Device)
        self.label_3 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.Step = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Step.sizePolicy().hasHeightForWidth())
        self.Step.setSizePolicy(sizePolicy)
        self.Step.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Step.setEditable(True)
        self.Step.setObjectName("Step")
        self.horizontalLayout_2.addWidget(self.Step)
        self.label_4 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.Recipe = QtWidgets.QComboBox(Form)
        self.Recipe.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Recipe.sizePolicy().hasHeightForWidth())
        self.Recipe.setSizePolicy(sizePolicy)
        self.Recipe.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Recipe.setAcceptDrops(False)
        self.Recipe.setEditable(True)
        self.Recipe.setObjectName("Recipe")
        self.horizontalLayout_2.addWidget(self.Recipe)
        self.label_5 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.Test_ID = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Test_ID.sizePolicy().hasHeightForWidth())
        self.Test_ID.setSizePolicy(sizePolicy)
        self.Test_ID.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Test_ID.setEditable(True)
        self.Test_ID.setObjectName("Test_ID")
        self.horizontalLayout_2.addWidget(self.Test_ID)
        self.label_6 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.Lot_ID = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lot_ID.sizePolicy().hasHeightForWidth())
        self.Lot_ID.setSizePolicy(sizePolicy)
        self.Lot_ID.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Lot_ID.setEditable(True)
        self.Lot_ID.setObjectName("Lot_ID")
        self.horizontalLayout_2.addWidget(self.Lot_ID)
        self.label_7 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.Wafer = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Wafer.sizePolicy().hasHeightForWidth())
        self.Wafer.setSizePolicy(sizePolicy)
        self.Wafer.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Wafer.setEditable(True)
        self.Wafer.setObjectName("Wafer")
        self.horizontalLayout_2.addWidget(self.Wafer)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Label_9 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_9.sizePolicy().hasHeightForWidth())
        self.Label_9.setSizePolicy(sizePolicy)
        self.Label_9.setMaximumSize(QtCore.QSize(16777215, 49))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Label_9.setFont(font)
        self.Label_9.setObjectName("Label_9")
        self.horizontalLayout.addWidget(self.Label_9)
        self.Starttime = QtWidgets.QDateTimeEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Starttime.sizePolicy().hasHeightForWidth())
        self.Starttime.setSizePolicy(sizePolicy)
        self.Starttime.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Starttime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.Starttime.setObjectName("Starttime")
        self.horizontalLayout.addWidget(self.Starttime)
        self.label_8 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 49))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.Endtime = QtWidgets.QDateTimeEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Endtime.sizePolicy().hasHeightForWidth())
        self.Endtime.setSizePolicy(sizePolicy)
        self.Endtime.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Endtime.setObjectName("Endtime")
        self.horizontalLayout.addWidget(self.Endtime)
        self.D1 = QtWidgets.QCheckBox(Form)
        self.D1.setMaximumSize(QtCore.QSize(16777215, 19))
        self.D1.setObjectName("D1")
        self.horizontalLayout.addWidget(self.D1)
        self.W1 = QtWidgets.QCheckBox(Form)
        self.W1.setMaximumSize(QtCore.QSize(16777215, 19))
        self.W1.setObjectName("W1")
        self.horizontalLayout.addWidget(self.W1)
        self.W2 = QtWidgets.QCheckBox(Form)
        self.W2.setMaximumSize(QtCore.QSize(16777215, 19))
        self.W2.setObjectName("W2")
        self.horizontalLayout.addWidget(self.W2)
        self.M1 = QtWidgets.QCheckBox(Form)
        self.M1.setMaximumSize(QtCore.QSize(16777215, 19))
        self.M1.setObjectName("M1")
        self.horizontalLayout.addWidget(self.M1)
        self.M2 = QtWidgets.QCheckBox(Form)
        self.M2.setMaximumSize(QtCore.QSize(16777215, 19))
        self.M2.setObjectName("M2")
        self.horizontalLayout.addWidget(self.M2)
        spacerItem = QtWidgets.QSpacerItem(16777215, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Apply = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Apply.sizePolicy().hasHeightForWidth())
        self.Apply.setSizePolicy(sizePolicy)
        self.Apply.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setBold(True)
        font.setWeight(75)
        self.Apply.setFont(font)
        self.Apply.setObjectName("Apply")
        self.horizontalLayout.addWidget(self.Apply)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 0, 1, 1)
        self.Waferinfo = QtWidgets.QTextBrowser(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Waferinfo.sizePolicy().hasHeightForWidth())
        self.Waferinfo.setSizePolicy(sizePolicy)
        self.Waferinfo.setMaximumSize(QtCore.QSize(16777215, 140))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Waferinfo.setFont(font)
        self.Waferinfo.setObjectName("Waferinfo")
        self.gridLayout_3.addWidget(self.Waferinfo, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        spacerItem1 = QtWidgets.QSpacerItem(16777215, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.Saveplot = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Saveplot.sizePolicy().hasHeightForWidth())
        self.Saveplot.setSizePolicy(sizePolicy)
        self.Saveplot.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Saveplot.setObjectName("Saveplot")
        self.horizontalLayout_4.addWidget(self.Saveplot)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.Max = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Max.sizePolicy().hasHeightForWidth())
        self.Max.setSizePolicy(sizePolicy)
        self.Max.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Max.setObjectName("Max")
        self.horizontalLayout_3.addWidget(self.Max)
        self.label_13 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.Min = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Min.sizePolicy().hasHeightForWidth())
        self.Min.setSizePolicy(sizePolicy)
        self.Min.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Min.setObjectName("Min")
        self.horizontalLayout_3.addWidget(self.Min)
        self.label_14 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.step = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step.sizePolicy().hasHeightForWidth())
        self.step.setSizePolicy(sizePolicy)
        self.step.setMaximumSize(QtCore.QSize(16777215, 25))
        self.step.setObjectName("step")
        self.horizontalLayout_3.addWidget(self.step)
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.SetScale = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SetScale.sizePolicy().hasHeightForWidth())
        self.SetScale.setSizePolicy(sizePolicy)
        self.SetScale.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setBold(True)
        font.setWeight(75)
        self.SetScale.setFont(font)
        self.SetScale.setObjectName("SetScale")
        self.horizontalLayout_3.addWidget(self.SetScale)
        self.label_15 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.recipe_out = QtWidgets.QTextBrowser(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recipe_out.sizePolicy().hasHeightForWidth())
        self.recipe_out.setSizePolicy(sizePolicy)
        self.recipe_out.setMinimumSize(QtCore.QSize(250, 0))
        self.recipe_out.setMaximumSize(QtCore.QSize(350, 25))
        self.recipe_out.setObjectName("recipe_out")
        self.horizontalLayout_3.addWidget(self.recipe_out)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        self.DataPlot = QtWidgets.QGraphicsView(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataPlot.sizePolicy().hasHeightForWidth())
        self.DataPlot.setSizePolicy(sizePolicy)
        self.DataPlot.setMaximumSize(QtCore.QSize(16777215, 300))
        self.DataPlot.setObjectName("DataPlot")
        self.gridLayout_2.addWidget(self.DataPlot, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.CT4 = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CT4.sizePolicy().hasHeightForWidth())
        self.CT4.setSizePolicy(sizePolicy)
        self.CT4.setMaximumSize(QtCore.QSize(83, 17))
        self.CT4.setObjectName("CT4")
        self.gridLayout.addWidget(self.CT4, 3, 0, 1, 1)
        self.T7 = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T7.sizePolicy().hasHeightForWidth())
        self.T7.setSizePolicy(sizePolicy)
        self.T7.setMinimumSize(QtCore.QSize(0, 0))
        self.T7.setMaximumSize(QtCore.QSize(200, 30))
        self.T7.setObjectName("T7")
        self.gridLayout.addWidget(self.T7, 6, 1, 1, 1)
        self.T6 = QtWidgets.QTextBrowser(Form)
        self.T6.setMaximumSize(QtCore.QSize(200, 30))
        self.T6.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.T6.setObjectName("T6")
        self.gridLayout.addWidget(self.T6, 5, 1, 1, 1)
        self.T2 = QtWidgets.QTextBrowser(Form)
        self.T2.setEnabled(True)
        self.T2.setMaximumSize(QtCore.QSize(200, 30))
        self.T2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.T2.setObjectName("T2")
        self.gridLayout.addWidget(self.T2, 1, 1, 1, 1)
        self.T4 = QtWidgets.QTextBrowser(Form)
        self.T4.setMaximumSize(QtCore.QSize(200, 30))
        self.T4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.T4.setObjectName("T4")
        self.gridLayout.addWidget(self.T4, 3, 1, 1, 1)
        self.CT1 = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CT1.sizePolicy().hasHeightForWidth())
        self.CT1.setSizePolicy(sizePolicy)
        self.CT1.setMaximumSize(QtCore.QSize(83, 17))
        self.CT1.setObjectName("CT1")
        self.gridLayout.addWidget(self.CT1, 0, 0, 1, 1)
        self.CT2 = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CT2.sizePolicy().hasHeightForWidth())
        self.CT2.setSizePolicy(sizePolicy)
        self.CT2.setMaximumSize(QtCore.QSize(83, 17))
        self.CT2.setObjectName("CT2")
        self.gridLayout.addWidget(self.CT2, 1, 0, 1, 1)
        self.CT3 = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CT3.sizePolicy().hasHeightForWidth())
        self.CT3.setSizePolicy(sizePolicy)
        self.CT3.setMaximumSize(QtCore.QSize(83, 17))
        self.CT3.setObjectName("CT3")
        self.gridLayout.addWidget(self.CT3, 2, 0, 1, 1)
        self.T1 = QtWidgets.QTextBrowser(Form)
        self.T1.setMaximumSize(QtCore.QSize(200, 30))
        self.T1.setMouseTracking(False)
        self.T1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.T1.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.T1.setObjectName("T1")
        self.gridLayout.addWidget(self.T1, 0, 1, 1, 1)
        self.T5 = QtWidgets.QTextBrowser(Form)
        self.T5.setMaximumSize(QtCore.QSize(200, 30))
        self.T5.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.T5.setObjectName("T5")
        self.gridLayout.addWidget(self.T5, 4, 1, 1, 1)
        self.CT5 = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CT5.sizePolicy().hasHeightForWidth())
        self.CT5.setSizePolicy(sizePolicy)
        self.CT5.setMaximumSize(QtCore.QSize(83, 17))
        self.CT5.setObjectName("CT5")
        self.gridLayout.addWidget(self.CT5, 4, 0, 1, 1)
        self.T3 = QtWidgets.QTextBrowser(Form)
        self.T3.setMaximumSize(QtCore.QSize(200, 30))
        self.T3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.T3.setObjectName("T3")
        self.gridLayout.addWidget(self.T3, 2, 1, 1, 1)
        self.CT6 = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CT6.sizePolicy().hasHeightForWidth())
        self.CT6.setSizePolicy(sizePolicy)
        self.CT6.setMaximumSize(QtCore.QSize(83, 17))
        self.CT6.setObjectName("CT6")
        self.gridLayout.addWidget(self.CT6, 5, 0, 1, 1)
        self.CT7 = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CT7.sizePolicy().hasHeightForWidth())
        self.CT7.setSizePolicy(sizePolicy)
        self.CT7.setMaximumSize(QtCore.QSize(83, 17))
        self.CT7.setObjectName("CT7")
        self.gridLayout.addWidget(self.CT7, 6, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 6, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 7, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.number = QtWidgets.QComboBox(Form)
        self.number.setMinimumSize(QtCore.QSize(230, 0))
        self.number.setObjectName("number")
        self.horizontalLayout_6.addWidget(self.number)
        spacerItem2 = QtWidgets.QSpacerItem(16777215, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 8, 0, 1, 1)
        self.Wafermap = QtWidgets.QGraphicsView(Form)
        self.Wafermap.setMinimumSize(QtCore.QSize(0, 140))
        self.Wafermap.setObjectName("Wafermap")
        self.gridLayout_3.addWidget(self.Wafermap, 9, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.showfolder, self.folder_path)
        Form.setTabOrder(self.folder_path, self.Tool)
        Form.setTabOrder(self.Tool, self.Device)
        Form.setTabOrder(self.Device, self.Step)
        Form.setTabOrder(self.Step, self.Recipe)
        Form.setTabOrder(self.Recipe, self.Test_ID)
        Form.setTabOrder(self.Test_ID, self.Lot_ID)
        Form.setTabOrder(self.Lot_ID, self.Wafer)
        Form.setTabOrder(self.Wafer, self.Starttime)
        Form.setTabOrder(self.Starttime, self.Endtime)
        Form.setTabOrder(self.Endtime, self.D1)
        Form.setTabOrder(self.D1, self.W1)
        Form.setTabOrder(self.W1, self.W2)
        Form.setTabOrder(self.W2, self.M1)
        Form.setTabOrder(self.M1, self.M2)
        Form.setTabOrder(self.M2, self.Apply)
        Form.setTabOrder(self.Apply, self.Waferinfo)
        Form.setTabOrder(self.Waferinfo, self.Max)
        Form.setTabOrder(self.Max, self.Min)
        Form.setTabOrder(self.Min, self.step)
        Form.setTabOrder(self.step, self.recipe_out)
        Form.setTabOrder(self.recipe_out, self.CT1)
        Form.setTabOrder(self.CT1, self.CT2)
        Form.setTabOrder(self.CT2, self.CT3)
        Form.setTabOrder(self.CT3, self.CT4)
        Form.setTabOrder(self.CT4, self.CT5)
        Form.setTabOrder(self.CT5, self.CT6)
        Form.setTabOrder(self.CT6, self.CT7)
        Form.setTabOrder(self.CT7, self.DataPlot)
        Form.setTabOrder(self.DataPlot, self.Wafermap)
        Form.setTabOrder(self.Wafermap, self.T4)
        Form.setTabOrder(self.T4, self.T5)
        Form.setTabOrder(self.T5, self.T6)
        Form.setTabOrder(self.T6, self.T3)
        Form.setTabOrder(self.T3, self.T2)
        Form.setTabOrder(self.T2, self.T1)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.showfolder.setText(_translate("Form", "Please select misd folder path"))
        self.folder_path.setText(_translate("Form", "folder path"))
        self.Search.setText(_translate("Form", "Search"))
        self.label.setText(_translate("Form", "Tool"))
        self.label_2.setText(_translate("Form", " Device"))
        self.label_3.setText(_translate("Form", " Step"))
        self.label_4.setText(_translate("Form", " Recipe"))
        self.label_5.setText(_translate("Form", " Test ID"))
        self.label_6.setText(_translate("Form", " Lot ID"))
        self.label_7.setText(_translate("Form", " Wafer"))
        self.Label_9.setText(_translate("Form", "Time"))
        self.Starttime.setDisplayFormat(_translate("Form", "yyyy/M/d HH:mm"))
        self.label_8.setText(_translate("Form", "to"))
        self.Endtime.setDisplayFormat(_translate("Form", "yyyy/M/d H:mm"))
        self.D1.setText(_translate("Form", "1D"))
        self.W1.setText(_translate("Form", "1W"))
        self.W2.setText(_translate("Form", "2W"))
        self.M1.setText(_translate("Form", "1M"))
        self.M2.setText(_translate("Form", "2M"))
        self.Apply.setText(_translate("Form", "APPLY"))
        self.label_9.setText(_translate("Form", "Wafer Information:"))
        self.Waferinfo.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\',\'新宋体\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'新宋体\'; font-size:9pt;\"><br /></p></body></html>"))
        self.label_12.setText(_translate("Form", "CD Plot:"))
        self.Saveplot.setText(_translate("Form", "Save"))
        self.label_10.setText(_translate("Form", "   Maximun CD"))
        self.label_13.setText(_translate("Form", "   Minimum CD"))
        self.label_14.setText(_translate("Form", "   Step"))
        self.SetScale.setText(_translate("Form", "Set"))
        self.label_15.setText(_translate("Form", "          Recipe"))
        self.CT4.setText(_translate("Form", "Target4"))
        self.T2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'新宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.CT1.setText(_translate("Form", "Target1"))
        self.CT2.setText(_translate("Form", "Target2"))
        self.CT3.setText(_translate("Form", "Target3"))
        self.T1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'新宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.CT5.setText(_translate("Form", "Target5"))
        self.CT6.setText(_translate("Form", "Target6"))
        self.CT7.setText(_translate("Form", "Target7"))
        self.label_11.setText(_translate("Form", "Wafer Map:"))
        self.label_16.setText(_translate("Form", "    Number"))


class MyWindow(QWidget, UnitForm):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Inline Data Review")
        self.listall = None
        self.Tool_a = None
        self.Device_a = None
        self.Step_a = None
        self.Recipe_a = None
        self.Test_ID_a = None
        self.Lot_ID_a = None
        self.Wafer_a = None
        self.Time_a = None
        self.Filename_a = None
        self.Index_a = None
        self.Start_time = None
        self.End_time = None
        self.active = None
        self.flag = False
        self.result = None
        self.final_result = None
        self.final_filename = None
        self.description_sel = None
        self.misd_path = []
        self.wafermap_misd = []
        self.fi = None
        self.misd_pathwm = []
        self.plot = None
        self.ChooseTarget = None
        self.setflag = False
        self.plotmark = None
        self.maxcd = None
        self.mincd = None
        self.df1 = None
        self.scale = None
        self.a1 = None
        self.dataflag = None
        self.wafer_lot = None

        self.Endtime.setDateTime(QDateTime.currentDateTime())
        self.Starttime.setMaximumDateTime(QDateTime.currentDateTime())
        self.Starttime.setDate(QtCore.QDate(2021, 1, 1))
        self.Starttime.setTime(QtCore.QTime(0, 0, 0))

        self.folder_path.clicked.connect(self.select_folder)
        self.Search.clicked.connect(self.openfilepath)

        self.Recipe.addItem("")
        self.Lot_ID.addItem("")
        self.Wafer.addItem("")
        self.Step.addItem("")
        self.Device.addItem("")
        self.Tool.addItem("")
        self.Test_ID.addItem("")
        self.number.addItem("")
        self.step.setMinimum(0.05)
        self.step.setSingleStep(0.5)
        self.Min.setMinimum(0)
        self.Min.setSingleStep(0.5)
        self.Max.setMinimum(0)
        self.Max.setSingleStep(0.5)

        self.Recipe.activated.connect(self.selection_change)
        self.Tool.activated.connect(self.selection_change)
        self.Device.activated.connect(self.selection_change)
        self.Step.activated.connect(self.selection_change)
        self.Lot_ID.activated.connect(self.selection_change)
        self.Wafer.activated.connect(self.selection_change)
        self.Starttime.dateTimeChanged.connect(self.get_time)
        self.Endtime.dateTimeChanged.connect(self.get_time)
        self.Apply.clicked.connect(self.filter_data_all)
        self.CT1.clicked.connect(self.select_target1)
        self.CT2.clicked.connect(self.select_target2)
        self.CT3.clicked.connect(self.select_target3)
        self.CT4.clicked.connect(self.select_target4)
        self.CT5.clicked.connect(self.select_target5)
        self.CT6.clicked.connect(self.select_target6)
        self.CT7.clicked.connect(self.select_combo)
        self.number.activated.connect(self.select_number)
        self.SetScale.clicked.connect(self.set_plot)
        self.Wafermap.mousePressEvent = self.large_shrink
        self.Saveplot.clicked.connect(self.save_plot)

    def select_folder(self):
        foldername = QFileDialog.getExistingDirectory(self, "Select Directory", "./")
        self.showfolder.setText(foldername)

    def save_plot(self):
        if self.flag is True:
            Min_CD = self.Min.value()
            Max_CD = self.Max.value()
            Step = self.step.value()
            figure = Figure_Canvas(self.plot, Max_CD, Min_CD, Step, self.ChooseTarget, 12, 2.5)
            figure.plot()


    def large_shrink(self, e):
        if (self.flag is True) & (self.plotmark is True) & (self.scale > 1) & (self.scale < 12):
            if e.buttons() == Qt.LeftButton:
                self.scale = self.scale + 0.5
                self.Wafermap.setObjectName("Wafermap")
                dr2 = Figure_Canvas_map(self.df1, self.maxcd, self.mincd, self.scale, self.scale, self.a1)
                dr2.wafer_plot()
                graphicscene2 = QtWidgets.QGraphicsScene()
                graphicscene2.addWidget(dr2)
                self.Wafermap.setScene(graphicscene2)
                self.Wafermap.show()
            elif e.buttons() == Qt.RightButton:
                    self.scale = self.scale - 0.5
                    self.Wafermap.setObjectName("Wafermap")
                    dr2 = Figure_Canvas_map(self.df1, self.maxcd, self.mincd, self.scale, self.scale, self.a1)
                    dr2.wafer_plot()
                    graphicscene2 = QtWidgets.QGraphicsScene()
                    graphicscene2.addWidget(dr2)
                    self.Wafermap.setScene(graphicscene2)
                    self.Wafermap.show()

    def set_plot(self):
        if self.flag is True:
            Max_CD = self.Max.value()
            Min_CD = self.Min.value()
            Step = self.step.value()

            if (Step <= 0) | (Min_CD >= Max_CD):
                QMessageBox.information(self, "Information", "Wrong Scale")
            else:
                self.DataPlot.setObjectName("DataPlot")
                dr = Figure_Canvas(self.plot, Max_CD, Min_CD, Step, self.ChooseTarget, 18, 5)
                dr.test()
                graphicscene = QtWidgets.QGraphicsScene()
                graphicscene.addWidget(dr)
                self.DataPlot.setScene(graphicscene)
                self.DataPlot.show()

    def traverse(self, root_path):
        list_path = os.listdir(root_path)
        for path in list_path:
            spath = os.path.join(root_path, path)
            if os.path.isfile(spath):
                if spath[-5:] == '.misd':
                    self.misd_path.append(spath.replace("\\", "/"))
            elif os.path.isdir(spath):
                self.traverse(spath)
        return self.misd_path

    def openfilepath(self):
        self.Waferinfo.clear()
        self.Recipe.clear()
        self.Lot_ID.clear()
        self.Wafer.clear()
        self.Step.clear()
        self.Device.clear()
        self.Tool.clear()
        self.Test_ID.clear()

        self.Recipe.addItem("")
        self.Lot_ID.addItem("")
        self.Wafer.addItem("")
        self.Step.addItem("")
        self.Device.addItem("")
        self.Tool.addItem("")
        self.Test_ID.addItem("")
        self.listall = []

        self.Tool_a = []
        self.Device_a = []
        self.Step_a = []
        self.Recipe_a = []
        self.Test_ID_a = []
        self.Lot_ID_a = []
        self.Wafer_a = []
        self.Time_a = []
        self.Filename_a = []
        self.misd_path = []
        self.Index_a = [2, 3, 6, 11, 19, 24, 23, 30]

        root_path = self.showfolder.text()
        if os.path.isdir(root_path) is not True:
            QMessageBox.information(self, "Information", "Please input a right path")
        else:
            filenames = self.traverse(root_path)
            #print(len(filenames))
            for file in filenames:
                if os.path.isfile(file)is True:
                    for j in self.Index_a:
                        lines = linecache.getline(file, j)
                        if j == 2:
                            self.Filename_a.append(file)
                            self.Lot_ID_a.append(lines.split("{")[1].split("}")[0].replace('"', '').split(",")[0])
                        elif j == 3:
                            self.Wafer_a.append(lines.split("{")[1].split("}")[0].replace('"', '').split(",")[0])
                        elif j == 6:
                            self.Time_a.append(lines.split("{")[1].split("}")[0].replace('"', '').replace("'",''))
                        elif j == 11:
                            self.Test_ID_a.append(lines.split("{")[1].split("}")[0].replace('"', '').split(",")[0])
                        elif j == 19:
                            self.Recipe_a.append(lines.split("{")[1].split("}")[0].replace('"', '').split(",")[0])
                        elif j == 24:
                            self.Step_a.append(lines.split("{")[1].split("}")[0].replace('"', '').split(",")[0])
                        elif j == 23:
                            self.Device_a.append(lines.split("{")[1].split("}")[0].replace('"', '').split(",")[0])
                        elif j == 30:
                            self.Tool_a.append(lines.split("{")[1].split("}")[0].replace('"', '')
                                               .split(",")[0].split('-')[0])

            self.listall.append(self.Filename_a)
            self.listall.append(self.Recipe_a)
            self.listall.append(self.Lot_ID_a)
            self.listall.append(self.Step_a)
            self.listall.append(self.Time_a)
            self.listall.append(self.Test_ID_a)
            self.listall.append(self.Wafer_a)
            self.listall.append(self.Step_a)

            #print(self.Filename_a)

            self.Recipe.addItems(set(self.Recipe_a))
            self.Lot_ID.addItems(set(self.Lot_ID_a))
            self.Wafer.addItems(set(self.Wafer_a))
            self.Step.addItems(set(self.Step_a))
            self.Device.addItems(set(self.Device_a))
            self.Tool.addItems(set(self.Tool_a))
            self.Test_ID.addItems(set(self.Test_ID_a))

    def selection_change(self):
        df = pd.DataFrame({'Filename': self.Filename_a})
        df['Tool'] = self.Tool_a
        df['Time'] = self.Time_a
        df['Device'] = self.Device_a
        df['Step'] = self.Step_a
        df['Recipe'] = self.Recipe_a
        df['Test ID'] = self.Test_ID_a
        df['Lot ID'] = self.Lot_ID_a
        df['Wafer'] = self.Wafer_a

        self.result = df

        if self.Tool.currentText() != "":
            self.result = self.result[self.result['Tool'] == self.Tool.currentText()]

            if self.Recipe.currentText() == "":
                self.Recipe.clear()
                self.Recipe.addItem("")
                for i in range(0, len(self.result['Recipe'].drop_duplicates())):
                    self.Recipe.addItem(self.result['Recipe'].drop_duplicates().values[i])

            if self.Device.currentText() == "":
                self.Device.clear()
                self.Device.addItem("")
                for i in range(0, len(self.result['Device'].drop_duplicates())):
                    self.Device.addItem(self.result['Device'].drop_duplicates().values[i])

            if self.Step.currentText() == "":
                self.Step.clear()
                self.Step.addItem("")
                for i in range(0, len(self.result['Step'].drop_duplicates())):
                    self.Step.addItem(self.result['Step'].drop_duplicates().values[i])

            if self.Lot_ID.currentText() == "":
                self.Lot_ID.clear()
                self.Lot_ID.addItem("")
                for i in range(0, len(self.result['Lot ID'].drop_duplicates())):
                    self.Lot_ID.addItem(self.result['Lot ID'].drop_duplicates().values[i])

            if self.Wafer.currentText() == "":
                self.Wafer.clear()
                self.Wafer.addItem("")
                for i in range(0, len(self.result['Wafer'].drop_duplicates())):
                    self.Wafer.addItem(self.result['Wafer'].drop_duplicates().values[i])

            if self.Test_ID.currentText() == "":
                self.Test_ID.clear()
                self.Test_ID.addItem("")
                for i in range(0, len(self.result['Test ID'].drop_duplicates())):
                    self.Test_ID.addItem(self.result['Test ID'].drop_duplicates().values[i])

        if self.Device.currentText() != "":
            self.result = df[df['Device'] == self.Device.currentText()]

            if self.Recipe.currentText() == "":
                self.Recipe.clear()
                self.Recipe.addItem("")
                for i in range(0, len(self.result['Recipe'].drop_duplicates())):
                    self.Recipe.addItem(self.result['Recipe'].drop_duplicates().values[i])

            if self.Tool.currentText() == "":
                self.Tool.clear()
                self.Tool.addItem("")
                for i in range(0, len(self.result['Tool'].drop_duplicates())):
                    self.Tool.addItem(self.result['Tool'].drop_duplicates().values[i])

            if self.Step.currentText() == "":
                self.Step.clear()
                self.Step.addItem("")
                for i in range(0, len(self.result['Step'].drop_duplicates())):
                    self.Step.addItem(self.result['Step'].drop_duplicates().values[i])

            if self.Lot_ID.currentText() == "":
                self.Lot_ID.clear()
                self.Lot_ID.addItem("")
                for i in range(0, len(self.result['Lot ID'].drop_duplicates())):
                    self.Lot_ID.addItem(self.result['Lot ID'].drop_duplicates().values[i])

            if self.Wafer.currentText() == "":
                self.Wafer.clear()
                self.Wafer.addItem("")
                for i in range(0, len(self.result['Wafer'].drop_duplicates())):
                    self.Wafer.addItem(self.result['Wafer'].drop_duplicates().values[i])

            if self.Test_ID.currentText() == "":
                self.Test_ID.clear()
                self.Test_ID.addItem("")
                for i in range(0, len(self.result['Test ID'].drop_duplicates())):
                    self.Test_ID.addItem(self.result['Test ID'].drop_duplicates().values[i])

        if self.Step.currentText() != "":
            self.result = df[df['Step'] == self.Step.currentText()]

            if self.Recipe.currentText() == "":
                self.Recipe.clear()
                self.Recipe.addItem("")
                for i in range(0, len(self.result['Recipe'].drop_duplicates())):
                    self.Recipe.addItem(self.result['Recipe'].drop_duplicates().values[i])

            if self.Tool.currentText() == "":
                self.Tool.clear()
                self.Tool.addItem("")
                for i in range(0, len(self.result['Tool'].drop_duplicates())):
                    self.Tool.addItem(self.result['Tool'].drop_duplicates().values[i])

            if self.Device.currentText() == "":
                self.Device.clear()
                self.Device.addItem("")
                for i in range(0, len(self.result['Device'].drop_duplicates())):
                    self.Device.addItem(self.result['Device'].drop_duplicates().values[i])

            if self.Lot_ID.currentText() == "":
                self.Lot_ID.clear()
                self.Lot_ID.addItem("")
                for i in range(0, len(self.result['Lot ID'].drop_duplicates())):
                    self.Lot_ID.addItem(self.result['Lot ID'].drop_duplicates().values[i])

            if self.Wafer.currentText() == "":
                self.Wafer.clear()
                self.Wafer.addItem("")
                for i in range(0, len(self.result['Wafer'].drop_duplicates())):
                    self.Wafer.addItem(self.result['Wafer'].drop_duplicates().values[i])

            if self.Test_ID.currentText() == "":
                self.Test_ID.clear()
                self.Test_ID.addItem("")
                for i in range(0, len(self.result['Test ID'].drop_duplicates())):
                    self.Test_ID.addItem(self.result['Test ID'].drop_duplicates().values[i])

        if self.Recipe.currentText() != "":
            self.result = self.result[self.result['Recipe'] == self.Recipe.currentText()]

            if self.Device.currentText() == "":
                self.Device.clear()
                self.Device.addItem("")
                for i in range(0, len(self.result['Device'].drop_duplicates())):
                    self.Device.addItem(self.result['Device'].drop_duplicates().values[i])

            if self.Tool.currentText() == "":
                self.Tool.clear()
                self.Tool.addItem("")
                for i in range(0, len(self.result['Tool'].drop_duplicates())):
                    self.Tool.addItem(self.result['Tool'].drop_duplicates().values[i])

            if self.Step.currentText() == "":
                self.Step.clear()
                self.Step.addItem("")
                for i in range(0, len(self.result['Step'].drop_duplicates())):
                    self.Step.addItem(self.result['Step'].drop_duplicates().values[i])

            if self.Lot_ID.currentText() == "":
                self.Lot_ID.clear()
                self.Lot_ID.addItem("")
                for i in range(0, len(self.result['Lot ID'].drop_duplicates())):
                    self.Lot_ID.addItem(self.result['Lot ID'].drop_duplicates().values[i])

            if self.Wafer.currentText() == "":
                self.Wafer.clear()
                self.Wafer.addItem("")
                for i in range(0, len(self.result['Wafer'].drop_duplicates())):
                    self.Wafer.addItem(self.result['Wafer'].drop_duplicates().values[i])

            if self.Test_ID.currentText() == "":
                self.Test_ID.clear()
                self.Test_ID.addItem("")
                for i in range(0, len(self.result['Test ID'].drop_duplicates())):
                    self.Test_ID.addItem(self.result['Test ID'].drop_duplicates().values[i])

        if self.Test_ID.currentText() != "":
            self.result = self.result[self.result['Test ID'] == self.Test_ID.currentText()]

            if self.Device.currentText() == "":
                self.Device.clear()
                self.Device.addItem("")
                for i in range(0, len(self.result['Device'].drop_duplicates())):
                    self.Device.addItem(self.result['Device'].drop_duplicates().values[i])

            if self.Tool.currentText() == "":
                self.Tool.clear()
                self.Tool.addItem("")
                for i in range(0, len(self.result['Tool'].drop_duplicates())):
                    self.Tool.addItem(self.result['Tool'].drop_duplicates().values[i])

            if self.Recipe.currentText() == "":
                self.Recipe.clear()
                self.Recipe.addItem("")
                for i in range(0, len(self.result['Recipe'].drop_duplicates())):
                    self.Recipe.addItem(self.result['Recipe'].drop_duplicates().values[i])

            if self.Step.currentText() == "":
                self.Step.clear()
                self.Step.addItem("")
                for i in range(0, len(self.result['Step'].drop_duplicates())):
                    self.Step.addItem(self.result['Step'].drop_duplicates().values[i])

            if self.Lot_ID.currentText() == "":
                self.Lot_ID.clear()
                self.Lot_ID.addItem("")
                for i in range(0, len(self.result['Lot ID'].drop_duplicates())):
                    self.Lot_ID.addItem(self.result['Lot ID'].drop_duplicates().values[i])

            if self.Wafer.currentText() == "":
                self.Wafer.clear()
                self.Wafer.addItem("")
                for i in range(0, len(self.result['Wafer'].drop_duplicates())):
                    self.Wafer.addItem(self.result['Wafer'].drop_duplicates().values[i])

        if self.Lot_ID.currentText() != "":
            self.result = self.result[self.result['Lot ID'] == self.Lot_ID.currentText()]

            if self.Device.currentText() == "":
                self.Device.clear()
                self.Device.addItem("")
                for i in range(0, len(self.result['Device'].drop_duplicates())):
                    self.Device.addItem(self.result['Device'].drop_duplicates().values[i])

            if self.Tool.currentText() == "":
                self.Tool.clear()
                self.Tool.addItem("")
                for i in range(0, len(self.result['Tool'].drop_duplicates())):
                    self.Tool.addItem(self.result['Tool'].drop_duplicates().values[i])

            if self.Step.currentText() == "":
                self.Step.clear()
                self.Step.addItem("")
                for i in range(0, len(self.result['Step'].drop_duplicates())):
                    self.Step.addItem(self.result['Step'].drop_duplicates().values[i])

            if self.Recipe.currentText() == "":
                self.Recipe.clear()
                self.Recipe.addItem("")
                for i in range(0, len(self.result['Recipe'].drop_duplicates())):
                    self.Recipe.addItem(self.result['Recipe'].drop_duplicates().values[i])

            if self.Wafer.currentText() == "":
                self.Wafer.clear()
                self.Wafer.addItem("")
                for i in range(0, len(self.result['Wafer'].drop_duplicates())):
                    self.Wafer.addItem(self.result['Wafer'].drop_duplicates().values[i])

            if self.Test_ID.currentText() == "":
                self.Test_ID.clear()
                self.Test_ID.addItem("")
                for i in range(0, len(self.result['Test ID'].drop_duplicates())):
                    self.Test_ID.addItem(self.result['Test ID'].drop_duplicates().values[i])

        if self.Wafer.currentText() != "":
            self.result = self.result[self.result['Wafer'] == self.Wafer.currentText()]

            if self.Device.currentText() == "":
                self.Device.clear()
                self.Device.addItem("")
                for i in range(0, len(self.result['Device'].drop_duplicates())):
                    self.Device.addItem(self.result['Device'].drop_duplicates().values[i])

            if self.Tool.currentText() == "":
                self.Tool.clear()
                self.Tool.addItem("")
                for i in range(0, len(self.result['Tool'].drop_duplicates())):
                    self.Tool.addItem(self.result['Tool'].drop_duplicates().values[i])

            if self.Step.currentText() == "":
                self.Step.clear()
                self.Step.addItem("")
                for i in range(0, len(self.result['Step'].drop_duplicates())):
                    self.Step.addItem(self.result['Step'].drop_duplicates().values[i])

            if self.Recipe.currentText() == "":
                self.Recipe.clear()
                self.Recipe.addItem("")
                for i in range(0, len(self.result['Recipe'].drop_duplicates())):
                    self.Recipe.addItem(self.result['Recipe'].drop_duplicates().values[i])

            if self.Lot_ID.currentText() == "":
                self.Lot_ID.clear()
                self.Lot_ID.addItem("")
                for i in range(0, len(self.result['Lot ID'].drop_duplicates())):
                    self.Lot_ID.addItem(self.result['Lot ID'].drop_duplicates().values[i])

            if self.Test_ID.currentText() == "":
                self.Test_ID.clear()
                self.Test_ID.addItem("")
                for i in range(0, len(self.result['Test ID'].drop_duplicates())):
                    self.Test_ID.addItem(self.result['Test ID'].drop_duplicates().values[i])

    def get_time(self):
        #print(QDateTime.currentDateTime().addDays(-1).toString("MM-dd-yy HH:mm:ss"))

        if (self.D1.isChecked() is False) & (self.W1.isChecked() is False) & (self.W2.isChecked() is False) & (self.M1.isChecked() is False) & (self.M2.isChecked() is False):
            self.active = True
        else:
            self.active = False

    def get_wafermap_info(self):
        self.scale = 4
        self.df1 = []
        misd_path = self.wafermap_misd
        #print(misd_path)
        wflag = False
        title = []
        value_all = []
        diey = []
        diex = []
        description = []
        AVG = []
        count = 0
        number = []
        counta = 0

        fi = open(misd_path, "r")
        for line in fi:
            if "Statistic Data" in line:
                wflag = True
                continue
            if wflag is True:
                count = count + 1
                if count == 1:
                    title = line.split(",")
                elif line != '\n':
                    counta = counta + 1
                    value = line.replace("\n", "").split(",")
                    value_all.append(value)
                if line == '\n':
                    wflag = False
                    break
        fi.close()

        Average = locals()
        #print(count)

        if count >= 25000:
            QMessageBox.information(self, "Information", "Statistic Data too large")

        elif count > 1 & count < 25000:
            for i in range(0, len(title)):
                if "DIEIDX" in title[i]:
                    for j in range(0, len(value_all)):
                        diex.append(value_all[j][i])
                if "DIEIDY" in title[i]:
                    for j in range(0, len(value_all)):
                        diey.append(value_all[j][i])
                if ("description" in title[i]) | ("DESCRIPTION" in title[i]) | ("description" in title[i]):
                    for j in range(0, len(value_all)):
                        description.append(value_all[j][i])
                if "Average" in title[i]:
                    Average[title[i]] = []
                    number.append(i)
                    AVG.append(title[i])
                    for j in range(0, len(value_all)):
                        Average[title[i]].append(value_all[j][i])

            AvgValue = self.ChooseTarget.replace(")", "").split("(")[1]
            DescpValue = self.ChooseTarget.replace(")", "").split("(")[0]

            df = pd.DataFrame({"DIEIDX": diex})
            df["DIEIDY"] = diey
            df["Description"] = description

            for i in range(0, len(AVG)):
                df[AVG[i]] = Average[title[number[i]]]
            # trans function
            df = df[df["Description"] == DescpValue]

            #print(len(df))
            if len(df) >= 2:
                data_frame = df.loc[:, ("DIEIDX", "DIEIDY", AvgValue)]
                data_frame[str(AvgValue)] = data_frame[str(AvgValue)].astype("float")

                # data_frame = data_frame.groupby(["DIEIDX", "DIEIDY"]).agg({AVG[0]: [np.mean]})
                #print(data_frame)

                data_frame['DIEIDY'] = data_frame['DIEIDY'].astype("int")
                data_frame['DIEIDX'] = data_frame['DIEIDX'].astype("int")

                #print(data_frame)
                # data_frame = data_frame[data_frame[AVG[0]] > 0]

                max_cd = data_frame[AvgValue].max()
                min_cd = data_frame[AvgValue].min()
                self.maxcd = max_cd
                self.mincd = min_cd
                df2 = data_frame[AvgValue]
                #print(len(df2))

                Averagecd = []
                for i in range(0, len(df2)):
                    Averagecd.append(df2.values[i])

                df1 = data_frame.pivot(index='DIEIDY', columns='DIEIDX', values=AvgValue)
                df1 = df1.round(2)
                self.df1 = df1
                #print(df1)
                self.plotmark = True

                self.a1 = ('Max:' + str(round(max_cd, 2)) + "  " + 'Min:' + str(round(min_cd, 2)) + "  " + 'Range:'
                           + str(round(max_cd - min_cd, 2)) + "  " + 'std:' + str(round(float(np.std(Averagecd)), 2)))
                #print(self.a1)
                self.Wafermap.setObjectName("Wafermap")
                dr2 = Figure_Canvas_map(df1, max_cd, min_cd, 4, 4, self.a1)
                dr2.wafer_plot()
                graphicscene2 = QtWidgets.QGraphicsScene()
                graphicscene2.addWidget(dr2)
                self.Wafermap.setScene(graphicscene2)
                self.Wafermap.show()
            else:
                QMessageBox.information(self, "Information", "No data in " + DescpValue)
                self.plotmark = False

        else:
            QMessageBox.information(self, "Information", "No data in Statistic Data.")
            self.plotmark = False

    def filter_data_all(self):
        self.CT1.setCheckState(2)
        self.Waferinfo.clear()
        self.misd_pathwm = []
        self.final_filename = []
        self.wafer_lot = []
        description_v = []
        misd_path = []
        misd_wafermap = []

        if (self.D1.isChecked() is False) & (self.W1.isChecked() is False) & (self.W2.isChecked() is False) & (self.M1.isChecked() is False) & (self.M2.isChecked() is False):
            self.active = True
        else:
            self.active = False
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', -1)

        df = pd.DataFrame({'Filename': self.Filename_a})
        df['Tool'] = self.Tool_a
        df['Time'] = pd.to_datetime(self.Time_a)
        df['Device'] = self.Device_a
        df['Step'] = self.Step_a
        df['Recipe'] = self.Recipe_a
        df['Test ID'] = self.Test_ID_a
        df['Lot ID'] = self.Lot_ID_a
        df['Wafer'] = self.Wafer_a
        df['Wafer_Lot'] = df['Lot ID'] + "-" + df['Wafer']

        #print(df['Wafer_Lot'])

        self.final_result = df
        #print(len(self.Filename_a))

        if self.Recipe.currentText() != "":
            self.final_result = self.final_result[self.final_result['Recipe'] == self.Recipe.currentText()]

        if self.Device.currentText() != "":
            self.final_result = self.final_result[self.final_result['Device'] == self.Device.currentText()]

        if self.Step.currentText() != "":
            self.final_result = self.final_result[self.final_result['Step'] == self.Step.currentText()]

        if self.Lot_ID.currentText() != "":
            self.final_result = self.final_result[self.final_result['Lot ID'] == self.Lot_ID.currentText()]

        if self.Wafer.currentText() != "":
            self.final_result = self.final_result[self.final_result['Wafer'] == self.Wafer.currentText()]

        if self.Test_ID.currentText() != "":
            self.final_result = self.final_result[self.final_result['Test ID'] == self.Test_ID.currentText()]

        #print(self.final_result)

        if self.active:
            self.End_time = self.Endtime.date().toString("MM-dd-yy") + " " + self.Endtime.time().toString("HH:mm:ss")
            self.Start_time = self.Starttime.date().toString("MM-dd-yy") + " " + self.Starttime.time().toString("HH:mm:ss")
            self.final_result = self.final_result[(self.final_result["Time"] <= self.End_time)& (self.final_result["Time"] >= self.Start_time)]
        elif self.D1.isChecked() is True:
            self.final_result = self.final_result[(self.final_result["Time"] >= QDateTime.currentDateTime().addDays(-1).toString("MM-dd-yy HH:mm:ss"))]
            self.End_time = QDateTime.currentDateTime().toString("MM-dd-yy HH:mm:ss")
            self.Start_time = QDateTime.currentDateTime().addDays(-1).toString("MM-dd-yy HH:mm:ss")

        elif self.W1.isChecked() is True:
            self.final_result = self.final_result[(self.final_result["Time"] >= QDateTime.currentDateTime().addDays(-7).toString("MM-dd-yy HH:mm:ss"))]
            self.End_time = QDateTime.currentDateTime().toString("MM-dd-yy HH:mm:ss")
            self.Start_time = QDateTime.currentDateTime().addDays(-7).toString("MM-dd-yy HH:mm:ss")

        elif self.W2.isChecked() is True:
            self.final_result = self.final_result[ (self.final_result["Time"] >= QDateTime.currentDateTime().addDays(-14).toString("MM-dd-yy HH:mm:ss"))]
            self.End_time = QDateTime.currentDateTime().toString("MM-dd-yy HH:mm:ss")
            self.Start_time = QDateTime.currentDateTime().addDays(-14).toString("MM-dd-yy HH:mm:ss")

        elif self.M1.isChecked() is True:
            self.final_result = self.final_result[ (self.final_result["Time"] >= QDateTime.currentDateTime().addDays(-31).toString("MM-dd-yy HH:mm:ss"))]
            self.End_time = QDateTime.currentDateTime().toString("MM-dd-yy HH:mm:ss")
            self.Start_time = QDateTime.currentDateTime().addDays(-31).toString("MM-dd-yy HH:mm:ss")

        elif self.M2.isChecked() is True:
            self.final_result = self.final_result[ (self.final_result["Time"] >= QDateTime.currentDateTime().addDays(-62).toString("MM-dd-yy HH:mm:ss"))]
            self.End_time = QDateTime.currentDateTime().toString("MM-dd-yy HH:mm:ss")
            self.Start_time = QDateTime.currentDateTime().addDays(-62).toString("MM-dd-yy HH:mm:ss")

        if len(self.final_result.index) == 0:
            QMessageBox.information(self, "Information", "No data exist.")
            self.flag = False
        elif (len(set(self.result['Recipe'].values)) == 1) & (len(set(self.result['Test ID'].values)) == 1):
            self.recipe_out.setText(self.result['Recipe'].drop_duplicates().values[0])
            self.Waferinfo.insertPlainText('Status: Success.')
            self.flag = True
        else:
            self.Waferinfo.insertPlainText('Status: Fail with duplicate data.')
            self.recipe_out.setText(self.result['Recipe'].drop_duplicates().values[0])
            self.flag = False

        self.final_result.sort_values(by='Time', ascending=True, inplace=True)

        self.final_filename = self.final_result["Filename"]

        for i in range(0, len(self.final_filename)):
            misd_path.append(self.final_filename.values[i])
            self.misd_pathwm.append(self.final_filename.values[i])
            self.wafer_lot.append(self.final_result['Wafer_Lot'].values[i])

        time1 = self.final_result["Time"].to_string(index=False).split("\n")

        time = time1[0]
        if len(time1) > 1:
            for i in range(1, len(time1)):
                time = time + "; " + time1[i]

        Text1 = ('Tool:' + str(set(self.final_result['Tool'].values)).replace("{'", "").replace("'}", "").replace("set()", "None").replace("', '", "; ")
                 + "  " + 'Recipe:' + str(set(self.final_result['Recipe'].values)).replace("{'", "").replace("'}", "").replace("set()", "None").replace("', '", "; ")
                 + "  " + 'Lot:' + str(set(self.final_result['Lot ID'].values)).replace("{'", "").replace("'}", "").replace("set()", "None").replace("', '", "; ")
                 + "  " + 'Wafer:' + str(set(self.final_result['Wafer'].values)).replace("{'", "").replace("'}", "").replace("set()", "None").replace("', '", "; "))

        Text2 = ('Date:' + time + "  " + "From:"+ str(self.Start_time) + " to " + str(self.End_time))

        self.Waferinfo.append(Text1)
        self.Waferinfo.append(Text2)

        # open folder
        wflag = False
        title = []
        value_all = []
        index_v = 0
        y = []
        ymax = []
        ymin = []
        number = []
        number1 = []
        future = []
        description_full = []
        description =[]
        Min = []
        Max = []
        Ave = []
        Count = []
        totalcount = 0
        wafer_lot_x = []

        #print(self.wafer_lot)

        for file in misd_path:
            count = 0
            wafer_lot = self.wafer_lot[index_v]
            #print(wafer_lot)
            index_v = index_v + 1
            fi = open(file, "r")
            for line in fi:
                if "Statistic Data Summary" in line:
                    wflag = True
                    continue
                if wflag is True:
                    count = count + 1
                    if count == 1:
                        title = ("number" + "," + "wafer_lot" + "," + line).split(",")
                    elif line != '\n':
                        totalcount = totalcount + 1
                        value = (str(index_v) + "," + wafer_lot + "," + line).replace("\n", "").split(",")
                        value_all.append(value)
                    if line == '\n':
                        wflag = False
                        break
            fi.close()

        #print(value_all)

        #print(totalcount)
        if totalcount >= (len(misd_path)):
            self.dataflag = True
            for i in range(0, len(title)):
                if "number" in title[i]:
                    for j in range(0, len(value_all)):
                        number.append(value_all[j][i])
                if "wafer_lot" in title[i]:
                    for j in range(0, len(value_all)):
                        wafer_lot_x.append(value_all[j][i])
                if "feature" in title[i]:
                    for j in range(0, len(value_all)):
                        future.append(value_all[j][i])
                if ("Description" in title[i]) | ("DESCRIPTION" in title[i]) | ("description" in title[i]):
                    for j in range(0, len(value_all)):
                        description.append(value_all[j][i])
                if "Min" in title[i]:
                    for j in range(0, len(value_all)):
                        Min.append(value_all[j][i])
                if "Max" in title[i]:
                    for j in range(0, len(value_all)):
                        Max.append(value_all[j][i])
                if "Ave" in title[i]:
                    for j in range(0, len(value_all)):
                        Ave.append(value_all[j][i])
                if "Count" in title[i]:
                    for j in range(0, len(value_all)):
                        Count.append(value_all[j][i])

            df1 = pd.DataFrame({"feature": future})
            df1["number"] = number
            df1["wafer_lot"] = wafer_lot_x
            df1["Description"] = description
            df1["Min"] = pd.to_numeric(Min)
            df1["Max"] = pd.to_numeric(Max)
            df1["Ave"] = pd.to_numeric(Ave)
            df1["Count"] = pd.to_numeric(Count)
            df1 = df1[df1["Ave"] > 0]
            df1 = df1[df1["Min"] > 0]
            df1 = df1[df1["Max"] > 0]
            del df1["Count"]
            df1["Full Name"] = df1["Description"] + "(" + df1["feature"] + ")"
            del df1["feature"]
            df1 = df1.groupby(['number', 'wafer_lot', 'Full Name', 'Description']).agg({'Min': [np.min], 'Max': [np.max], 'Ave': [np.mean]})
            df1 = df1.reset_index()
            df1["number"] = df1["number"].astype(int)
            df1.sort_values(by='number', ascending=True, inplace=True)

            for i in range(0, len(df1["Full Name"])):
                description_full.append(df1["Full Name"].values[i])

            for i in description_full:
                if i not in description_v:
                    description_v.append(i)

            self.description_sel = description_v
            self.CT2.setCheckState(0)
            self.CT3.setCheckState(0)
            self.CT4.setCheckState(0)
            self.CT5.setCheckState(0)
            self.CT6.setCheckState(0)
            self.CT7.setCheckState(0)
            self.T1.clear()
            self.T2.clear()
            self.T3.clear()
            self.T4.clear()
            self.T5.clear()
            self.T6.clear()
            self.T7.clear()
            self.number.clear()

            if len(description_v) > 0 & len(description_v) <= 7:

                self.T1.setText(description_v[0])
                if len(description_v) - 1 >= 1:
                    self.T2.setText(description_v[1])
                if len(description_v) - 1 >= 2:
                    self.T3.setText(description_v[2])
                if len(description_v) - 1 >= 3:
                    self.T4.setText(description_v[3])
                if len(description_v) - 1 >= 4:
                    self.T5.setText(description_v[4])
                if len(description_v) - 1 >= 5:
                    self.T6.setText(description_v[5])
                if len(description_v) - 1 >= 6:
                    self.T7.addItem(description_v[6])
            elif len(description_v) > 7:
                self.T1.setText(description_v[0])
                self.T2.setText(description_v[1])
                self.T3.setText(description_v[2])
                self.T4.setText(description_v[3])
                self.T5.setText(description_v[4])
                self.T6.setText(description_v[5])
                self.T7.addItem("")
                for i in range(6, len(description_v)):
                    self.T7.addItem(description_v[i])

            self.plot = df1

            #print(self.plot)

            Des = description_v[0]

            df1 = df1[df1["Full Name"] == Des]

            wafer_lot1 = []
            for i in range(0, len(df1["Ave"])):
                number1.append(df1["number"].values[i])
                wafer_lot1.append(str(df1["wafer_lot"].values[i]) + "_" + str(df1["number"].values[i]))
                y.append(float(df1["Ave"].values[i]))
                ymax.append(float(df1["Max"].values[i]))
                ymin.append(float(df1["Min"].values[i]))

            for i in range(0, len(number1)):
                self.number.addItem(wafer_lot1[i])

            Max_CD = max(y)
            Min_CD = min(y)

            if (Max_CD-Min_CD) >= 10:
                Step = (Max_CD - Min_CD) / 10
            elif (Max_CD-Min_CD) < 0.15:
                Step = 0.05
            else:
                Step = (Max_CD - Min_CD) / 3

            self.Min.setValue(Min_CD)
            self.Max.setValue(Max_CD)
            self.step.setValue(Step)

            self.ChooseTarget = Des
            if self.flag is True:
                self.DataPlot.setObjectName("DataPlot")
                dr = Figure_Canvas(df1, Max_CD, Min_CD, Step, Des, 18, 5)
                dr.test()
                graphicscene = QtWidgets.QGraphicsScene()
                graphicscene.addWidget(dr)
                self.DataPlot.setScene(graphicscene)
                self.DataPlot.show()
        else:
            QMessageBox.information(self, "Information", "No data in Statistic Data Summary.")

    def select_target1(self):
        y = []
        Min_CD = []
        Max_CD = []
        Step = []
        setted = False
        if self.CT1.isChecked() is True:
            self.CT2.setCheckState(0)
            self.CT3.setCheckState(0)
            self.CT4.setCheckState(0)
            self.CT5.setCheckState(0)
            self.CT6.setCheckState(0)
            self.CT7.setCheckState(0)
            setted = True
        if self.flag is True:
            if self.setflag is True:
                Min_CD = self.Min.value()
                Max_CD = self.Max.value()
                Step = self.step.value()
            if (self.CT1.isChecked() is False) & (self.CT2.isChecked() is False) & (self.CT3.isChecked() is False)&(
                    self.CT4.isChecked() is False) & (self.CT5.isChecked() is False) & (self.CT6.isChecked() is False)&(self.CT7.isChecked() is False):
                QMessageBox.information(self, "Information", "Please select a target.")

            if (self.CT1.isChecked() is True) & (len(self.description_sel) - 1 >= 0) & (setted is True):
                if self.setflag is False:
                    df = self.plot[self.plot["Full Name"] == self.description_sel[0]]
                    for i in range(0, len(df["Ave"])):
                        y.append(float(df["Ave"].values[i]))
                    Min_CD = np.min(y)
                    Max_CD = np.max(y)
                    if (Max_CD - Min_CD) >= 10:
                        Step = (Max_CD - Min_CD) / 10
                    elif (Max_CD - Min_CD) < 0.15:
                        Step = 0.05
                    else:
                        Step = (Max_CD - Min_CD) / 3
                self.Min.setValue(Min_CD)
                self.Max.setValue(Max_CD)
                self.step.setValue(Step)

                self.ChooseTarget = self.description_sel[0]
                self.DataPlot.setObjectName("DataPlot")
                dr = Figure_Canvas(self.plot, Max_CD, Min_CD, Step, self.description_sel[0], 18, 5)
                dr.test()
                graphicscene = QtWidgets.QGraphicsScene()
                graphicscene.addWidget(dr)
                self.DataPlot.setScene(graphicscene)
                self.DataPlot.show()

    def select_target2(self):
        y = []
        setted = False
        if self.CT2.isChecked() is True:
            self.CT1.setCheckState(0)
            self.CT3.setCheckState(0)
            self.CT4.setCheckState(0)
            self.CT5.setCheckState(0)
            self.CT6.setCheckState(0)
            self.CT7.setCheckState(0)
            setted = True

        if self.flag is True:

            if self.setflag is True:

                Min_CD = self.Min.value()
                Max_CD = self.Max.value()
                Step = self.step.value()

            if (self.CT2.isChecked() is True) & (len(self.description_sel) - 2 >= 0) & (setted is True):
                if self.setflag is False:
                    df = self.plot[self.plot["Full Name"] == self.description_sel[1]]
                    #print(df)
                    for i in range(0, len(df["Ave"])):
                        y.append(float(df["Ave"].values[i]))
                    #print(y)
                    Min_CD = np.min(y)
                    Max_CD = np.max(y)
                    if (Max_CD - Min_CD) >= 10:
                        Step = (Max_CD - Min_CD) / 10
                    elif (Max_CD - Min_CD) < 0.15:
                        Step = 0.05
                    else:
                        Step = (Max_CD - Min_CD) / 3
                self.ChooseTarget = self.description_sel[1]
                self.Min.setValue(Min_CD)
                self.Max.setValue(Max_CD)
                self.step.setValue(Step)

                self.DataPlot.setObjectName("DataPlot")

                dr = Figure_Canvas(self.plot, Max_CD, Min_CD, Step, self.description_sel[1], 18, 5)
                dr.test()
                graphicscene = QtWidgets.QGraphicsScene()
                graphicscene.addWidget(dr)
                self.DataPlot.setScene(graphicscene)
                self.DataPlot.show()

    def select_target3(self):
        y = []
        if self.CT3.isChecked() is True:
            self.CT1.setCheckState(0)
            self.CT2.setCheckState(0)
            self.CT4.setCheckState(0)
            self.CT5.setCheckState(0)
            self.CT6.setCheckState(0)
            self.CT7.setCheckState(0)
        if self.flag is True:
            if self.setflag is True:
                Min_CD = self.Min.value()
                Max_CD = self.Max.value()
                Step = self.step.value()
            if (self.CT3.isChecked() is True) & (len(self.description_sel) - 3 >= 0):
                if self.setflag is False:
                    #print(self.plot)
                    df = self.plot[self.plot["Full Name"] == self.description_sel[2]]
                    for i in range(0, len(df["Ave"])):
                        y.append(float(df["Ave"].values[i]))
                    #print(y)
                    Min_CD = np.min(y)
                    Max_CD = np.max(y)
                    if (Max_CD - Min_CD) >= 10:
                        Step = (Max_CD - Min_CD) / 10
                    elif (Max_CD - Min_CD) < 0.15:
                        Step = 0.05
                    else:
                        Step = (Max_CD - Min_CD) / 3
                self.ChooseTarget = self.description_sel[2]
                self.Min.setValue(Min_CD)
                self.Max.setValue(Max_CD)
                self.step.setValue(Step)

                #print(self.description_sel[2])
                dr = Figure_Canvas(self.plot, Max_CD, Min_CD, Step, self.description_sel[2], 18, 5)
                dr.test()
                graphicscene = QtWidgets.QGraphicsScene()
                graphicscene.addWidget(dr)
                self.DataPlot.setScene(graphicscene)
                self.DataPlot.show()

    def select_target4(self):
        y = []
        #print(len(self.description_sel))
        if self.CT4.isChecked() is True:
            self.CT1.setCheckState(0)
            self.CT3.setCheckState(0)
            self.CT2.setCheckState(0)
            self.CT5.setCheckState(0)
            self.CT6.setCheckState(0)
            self.CT7.setCheckState(0)
        if self.flag is True:
            if self.setflag is True:
                Min_CD = self.Min.value()
                Max_CD = self.Max.value()
                Step = self.step.value()
            if (self.CT4.isChecked() is True) & (len(self.description_sel) - 4 >= 0):
                if self.setflag is False:
                    df = self.plot[self.plot["Full Name"] == self.description_sel[3]]
                    for i in range(0, len(df["Ave"])):
                        y.append(float(df["Ave"].values[i]))
                    #print(y)
                    Min_CD = np.min(y)
                    Max_CD = np.max(y)
                    if (Max_CD - Min_CD) >= 10:
                        Step = (Max_CD - Min_CD) / 10
                    elif (Max_CD - Min_CD) < 0.15:
                        Step = 0.05
                    else:
                        Step = (Max_CD - Min_CD) / 3
                self.ChooseTarget = self.description_sel[3]
                self.Min.setValue(Min_CD)
                self.Max.setValue(Max_CD)
                self.step.setValue(Step)

                dr = Figure_Canvas(self.plot, Max_CD, Min_CD, Step, self.description_sel[3], 18, 5)
                dr.test()
                graphicscene = QtWidgets.QGraphicsScene()
                graphicscene.addWidget(dr)
                self.DataPlot.setScene(graphicscene)
                self.DataPlot.show()

    def select_target5(self):
        y = []
        if self.CT5.isChecked() is True:
            self.CT1.setCheckState(0)
            self.CT3.setCheckState(0)
            self.CT4.setCheckState(0)
            self.CT2.setCheckState(0)
            self.CT6.setCheckState(0)
            self.CT7.setCheckState(0)
        if self.flag is True:
            if self.setflag is True:
                Min_CD = self.Min.value()
                Max_CD = self.Max.value()
                Step = self.step.value()
            if (self.CT5.isChecked() is True) & (len(self.description_sel) - 5 >= 0):
                if self.setflag is False:
                    df = self.plot[self.plot["Full Name"] == self.description_sel[4]]
                    for i in range(0, len(df["Ave"])):
                        y.append(float(df["Ave"].values[i]))
                    # print(y)
                    Min_CD = np.min(y)
                    Max_CD = np.max(y)
                    if (Max_CD - Min_CD) >= 10:
                        Step = (Max_CD - Min_CD) / 10
                    elif (Max_CD - Min_CD) < 0.15:
                        Step = 0.05
                    else:
                        Step = (Max_CD - Min_CD) / 3
                self.ChooseTarget = self.description_sel[4]
                self.Min.setValue(Min_CD)
                self.Max.setValue(Max_CD)
                self.step.setValue(Step)

                dr = Figure_Canvas(self.plot, Max_CD, Min_CD, Step, self.description_sel[4], 18, 5)
                dr.test()
                graphicscene = QtWidgets.QGraphicsScene()
                graphicscene.addWidget(dr)
                self.DataPlot.setScene(graphicscene)
                self.DataPlot.show()

    def select_target6(self):
        y = []
        if self.CT6.isChecked() is True:
            self.CT1.setCheckState(0)
            self.CT3.setCheckState(0)
            self.CT4.setCheckState(0)
            self.CT5.setCheckState(0)
            self.CT2.setCheckState(0)
            self.CT7.setCheckState(0)
        if self.flag is True:
            if self.setflag is True:
                Min_CD = self.Min.value()
                Max_CD = self.Max.value()
                Step = self.step.value()
            if (self.CT6.isChecked() is True) & (len(self.description_sel) - 6 >= 0):
                if self.setflag is False:
                    df = self.plot[self.plot["Full Name"] == self.description_sel[5]]
                    for i in range(0, len(df["Ave"])):
                        y.append(float(df["Ave"].values[i]))
                    # print(y)
                    Min_CD = np.min(y)
                    Max_CD = np.max(y)
                    if (Max_CD - Min_CD) >= 10:
                        Step = (Max_CD - Min_CD) / 10
                    elif (Max_CD - Min_CD) < 0.15:
                        Step = 0.05
                    else:
                        Step = (Max_CD - Min_CD) / 3
                self.ChooseTarget = self.description_sel[5]
                self.Min.setValue(Min_CD)
                self.Max.setValue(Max_CD)
                self.step.setValue(Step)

                dr = Figure_Canvas(self.plot, Max_CD, Min_CD, Step, self.description_sel[5], 18, 5)
                dr.test()
                graphicscene = QtWidgets.QGraphicsScene()
                graphicscene.addWidget(dr)
                self.DataPlot.setScene(graphicscene)
                self.DataPlot.show()

    def select_combo(self):
        y = []
        if self.CT7.isChecked() is True:
            self.CT1.setCheckState(0)
            self.CT3.setCheckState(0)
            self.CT4.setCheckState(0)
            self.CT5.setCheckState(0)
            self.CT6.setCheckState(0)
            self.CT2.setCheckState(0)
        if self.flag is True:
            if self.setflag is True:
                Min_CD = self.Min.value()
                Max_CD = self.Max.value()
                Step = self.step.value()
            if (self.CT7.isChecked() is True) & (len(self.description_sel) - 7 >= 0) & (self.T7.currentText() != ""):
                if self.setflag is False:
                    df = self.plot[self.plot["Full Name"] == self.T7.currentText()]
                    for i in range(0, len(df["Ave"])):
                        y.append(float(df["Ave"].values[i]))
                    # print(y)
                    Min_CD = np.min(y)
                    Max_CD = np.max(y)
                    if (Max_CD - Min_CD) >= 10:
                        Step = (Max_CD - Min_CD) / 10
                    elif (Max_CD - Min_CD) < 0.15:
                        Step = 0.05
                    else:
                        Step = (Max_CD - Min_CD) / 3
                self.ChooseTarget = self.T7.currentText()
                self.Min.setValue(Min_CD)
                self.Max.setValue(Max_CD)
                self.step.setValue(Step)

                dr = Figure_Canvas(self.plot, Max_CD, Min_CD, Step, self.T7.currentText(), 18, 5)
                dr.test()
                graphicscene = QtWidgets.QGraphicsScene()
                graphicscene.addWidget(dr)
                self.DataPlot.setScene(graphicscene)
                self.DataPlot.show()

    def select_number(self):
        if (self.number.currentText() != "") & (self.flag is True) & (self.ChooseTarget is not None):
            i = int(self.number.currentText().split("_")[-1])-1
            self.wafermap_misd = self.misd_pathwm[i]
            #print(self.misd_pathwm)
            self.get_wafermap_info()
        else:
            QMessageBox.information(self, "Information", "Lack of Data")


class Figure_Canvas(FigureCanvas):
    def __init__(self, plot, Max, Min, range, description, width, hight, parent=None):
        fig = Figure(figsize=(width, hight), dpi=75)
        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.plotB = plot
        self.description = description
        self.max = Max
        self.min = Min
        self.range = range
        self.ax = None
        self.setParent(parent)
        self.ax = fig.add_subplot(211)

    def test(self):
        y = []
        ymax = []
        ymin = []
        number1 = []
        wafer_lot = []

        df = self.plotB

        df = df[df["Full Name"] == self.description]

        for i in range(0, len(df["Ave"])):
            number1.append(df["number"].values[i])
            wafer_lot.append(str(df["wafer_lot"].values[i]) + "_" + str(df["number"].values[i]))
            y.append(float(df["Ave"].values[i]))
            ymax.append(float(df["Max"].values[i]))
            ymin.append(float(df["Min"].values[i]))

        #print(wafer_lot)

        Max_CD = self.max
        Min_CD = self.min
        Step_nm = self.range
        Step = int((Max_CD - Min_CD) / Step_nm)

        if Step == 0:
            Step = 2

        if Max_CD - Min_CD > 0.025:
            self.ax.set_ylim((Min_CD - (Max_CD-Min_CD)*0.025, Max_CD + (Max_CD-Min_CD)*0.025))
            self.ax.set_yticks(np.linspace(round(Max_CD,2), round(Min_CD,2), Step))
        else:
            self.ax.set_ylim((Min_CD - 0.05, Max_CD + 0.05))
            self.ax.set_yticks(np.linspace(round(Max_CD + 0.05, 2), round(Min_CD - 0.05, 2), Step))

        #self.ax.set_xlim(min(number1) - 0.2, max(number1) + 0.2)

        self.ax.grid(axis='y', linestyle=':')

        self.ax.plot(wafer_lot, y, color='steelblue', marker='o', linestyle='--', markersize=5)
        ###########
        xticks = range(0, len(wafer_lot), 1)
        self.ax.set_xticks(xticks)
        #print(xticks)

        for tick in self.ax.get_xticklabels():
            tick.set_rotation(25)
        #self.ax_a.set_xticklabels(["effort"])
        #self.ax_a.set_xticks(rotation=45)
        #print(wafer_lot)
        ##########
        for _x, _y in zip(df["number"], y):
           self.ax.text(_x-1, _y + (Max_CD - Min_CD)*0.02, '%.2f' % _y, ha='center', va='bottom', size=10)

        #self.ax.spines["bottom"].set_visible(False)
        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)

        a1 = ('Max:' + str(round(max(y), 2)) + "  " + 'Min:' + str(round(min(y), 2)) + "  " + 'Range:'
              + str(round(max(y) - min(y), 2)) + "  " + 'std:' + str(round(float(np.std(y)), 2)))
        self.ax.set_title(a1, fontdict={'size': '13', 'color': 'steelblue'})
       # self.ax.set_xlabel("wafer-lot", fontsize=8)
        self.ax.set_ylabel("CD", fontsize=10)


    def plot(self):
        figure = plt.figure()
        ax1 = figure.add_subplot(1, 1, 1)
        y = []
        ymax = []
        ymin = []
        number1 = []
        wafer_lot = []

        df = self.plotB

        df = df[df["Full Name"] == self.description]

        for i in range(0, len(df["Ave"])):
            number1.append(df["number"].values[i])
            wafer_lot.append(str(df["wafer_lot"].values[i]) + "_" + str(df["number"].values[i]))
            y.append(float(df["Ave"].values[i]))
            ymax.append(float(df["Max"].values[i]))
            ymin.append(float(df["Min"].values[i]))

        Max_CD = self.max
        Min_CD = self.min
        Step_nm = self.range
        Step = int((Max_CD - Min_CD) / Step_nm)

        if Step == 0:
            Step = 2

        if Max_CD - Min_CD > 0.025:
            plt.ylim((Min_CD - (Max_CD-Min_CD)*0.025, Max_CD + (Max_CD-Min_CD)*0.025))
            plt.yticks(np.linspace(round(Max_CD, 2), round(Min_CD,2), Step))
        else:
            plt.ylim((Min_CD - 0.05, Max_CD + 0.05))
            plt.yticks(np.linspace(round(Max_CD + 0.05, 2), round(Min_CD - 0.05, 2), Step))

        #plt.xlim(min(number1) - 0.2, max(number1) + 0.2)

        plt.grid(axis='y', linestyle=':')

        plt.xlabel("wafer-lot", fontsize=10)
        plt.ylabel("CD", fontsize=10)
        xticks = range(0, len(wafer_lot), 1)
        plt.xticks(xticks, rotation=30)
        #plt.xticklabels(wafer_lot, rotation=45)
        # self.ax_a.set_xticks(rotation=45)

        #plt.xticks(np.linspace(min(number1), max(number1), max(number1) - min(number1) + 1))

        plt.plot(wafer_lot, y, color='steelblue', marker='o', linewidth=1, linestyle='--', label="Avg", markersize=5)

        for _x, _y in zip(df["number"], y):
            plt.text(_x-1, _y + (Max_CD - Min_CD)*0.02, '%.2f' % _y, ha='center', va='bottom', size=11)
        #self.ax.spines["bottom"].set_visible(False)
        #self.ax.spines["top"].set_visible(False)
        #self.ax.spines["right"].set_visible(False)

        a1 = ('Max:' + str(round(max(y), 2)) + "  " + 'Min:' + str(round(min(y), 2)) + "  " + 'Range:'
              + str(round(max(y) - min(y), 2)) + "  " + 'std:' + str(round(float(np.std(y)), 2)))
        plt.title(a1, fontdict={'size': '13', 'color': 'steelblue'})
        plt.subplots_adjust(bottom=0.4)
        plt.show()


class Figure_Canvas_map(FigureCanvas):
    def __init__(self, df1, max_cd, min_cd, width, hight, txt, parent=None):
        fig1 = Figure(figsize=(width, hight), dpi=200)
        FigureCanvas.__init__(self, fig1)
        self.df1 = df1
        self.min_cd = min_cd
        self.max_cd = max_cd
        self.scaleF = width
        self.setParent(parent)
        self.title = txt
        self.ax_a = fig1.add_subplot(111)

    def wafer_plot(self):
        size1 = []

        font = {'family': 'sans-serif', 'color': 'k', 'weight': 'normal', 'size': 5}
        if len(self.df1.index) > 15 & len(self.df1.index) <= 20:
            size = (self.scaleF + 1)/2.2
            size1 = size + 1.5
        elif len(self.df1.index) > 20:
            size = (self.scaleF + 1) / 3
            size1 = size + 2
        elif len(self.df1.index) >= 24:
            size = (self.scaleF + 1) / 4.5
            size1 = size + 2.5
        else:
            size = self.scaleF + 1
            size1 = size

        self.ax_a.imshow(self.df1, cmap='jet')

        self.ax_a.set_xlabel('Die_x', fontsize=size1, color='k')
        self.ax_a.set_ylabel('Die_y', fontsize=size1, color='k')

        self.ax_a.set_yticks(np.arange(len(self.df1.index)))
        self.ax_a.set_xticks(np.arange(len(self.df1.columns)))

        self.ax_a.set_yticklabels(self.df1.index, fontsize=size1)
        self.ax_a.set_xticklabels(self.df1.columns, fontsize=size1)

        self.df1 = self.df1.fillna('')

        for i in range(len(self.df1.index)):
            for j in range(len(self.df1.columns)):
                text = self.ax_a.text(j, i, self.df1.values[i, j], ha="center", va="center", color="black", size=size)

        self.ax_a.set_title(self.title, fontsize=size1 + 0.5)


if __name__ == "__main__":
    #QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

