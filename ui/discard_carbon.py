# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'discard_carbon.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys

from PyQt5 import QtCore, QtGui, QtWidgets

# from qdarkstyle.light.palette import LightPalette
# app = QtWidgets.QApplication(sys.argv)
# window = QtWidgets.QMainWindow()
# import qdarkstyle
# app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))

extra = {
    # Button colors
    'danger': '#dc3545',
    'warning': '#ffc107',
    'success': '#17a2b8',
    # Font
    'font_family': '等线',
}


from qt_material import apply_stylesheet
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
apply_stylesheet(app, theme='light_blue.xml', extra=extra)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1412, 663)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 17)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.pushButton_main_price = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_main_price.setFont(font)
        self.pushButton_main_price.setObjectName("pushButton_main_price")
        self.verticalLayout_6.addWidget(self.pushButton_main_price)
        self.pushButton_main_count = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_main_count.setFont(font)
        self.pushButton_main_count.setObjectName("pushButton_main_count")
        self.verticalLayout_6.addWidget(self.pushButton_main_count)
        self.pushButton_main_elec = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_main_elec.setFont(font)
        self.pushButton_main_elec.setObjectName("pushButton_main_elec")
        self.verticalLayout_6.addWidget(self.pushButton_main_elec)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.stackedWidget_main = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_main.setObjectName("stackedWidget_main")
        self.page_pricepre = QtWidgets.QWidget()
        self.page_pricepre.setObjectName("page_pricepre")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_pricepre)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_price_data = QtWidgets.QPushButton(self.page_pricepre)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.pushButton_price_data.setFont(font)
        self.pushButton_price_data.setObjectName("pushButton_price_data")
        self.verticalLayout_2.addWidget(self.pushButton_price_data)
        self.pushButton_price_buildmodle = QtWidgets.QPushButton(self.page_pricepre)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.pushButton_price_buildmodle.setFont(font)
        self.pushButton_price_buildmodle.setObjectName("pushButton_price_buildmodle")
        self.verticalLayout_2.addWidget(self.pushButton_price_buildmodle)
        self.pushButton = QtWidgets.QPushButton(self.page_pricepre)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_price_pred = QtWidgets.QPushButton(self.page_pricepre)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.pushButton_price_pred.setFont(font)
        self.pushButton_price_pred.setObjectName("pushButton_price_pred")
        self.verticalLayout_2.addWidget(self.pushButton_price_pred)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.price_pre_stack = QtWidgets.QStackedWidget(self.page_pricepre)
        self.price_pre_stack.setObjectName("price_pre_stack")
        self.price_pre_data = QtWidgets.QWidget()
        self.price_pre_data.setObjectName("price_pre_data")
        self.gridLayout = QtWidgets.QGridLayout(self.price_pre_data)
        self.gridLayout.setObjectName("gridLayout")
        self.price_pre_data_input_load_button = QtWidgets.QPushButton(self.price_pre_data)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.price_pre_data_input_load_button.setFont(font)
        self.price_pre_data_input_load_button.setObjectName("price_pre_data_input_load_button")
        self.gridLayout.addWidget(self.price_pre_data_input_load_button, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 0, 1, 3)
        self.price_pre_data_input_slectpath_button = QtWidgets.QPushButton(self.price_pre_data)
        self.price_pre_data_input_slectpath_button.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.price_pre_data_input_slectpath_button.setFont(font)
        self.price_pre_data_input_slectpath_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.price_pre_data_input_slectpath_button.setObjectName("price_pre_data_input_slectpath_button")
        self.gridLayout.addWidget(self.price_pre_data_input_slectpath_button, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.price_pre_data)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.price_pre_data_canbox = QtWidgets.QGroupBox(self.price_pre_data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.price_pre_data_canbox.sizePolicy().hasHeightForWidth())
        self.price_pre_data_canbox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.price_pre_data_canbox.setFont(font)
        self.price_pre_data_canbox.setAlignment(QtCore.Qt.AlignCenter)
        self.price_pre_data_canbox.setObjectName("price_pre_data_canbox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.price_pre_data_canbox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout.addWidget(self.price_pre_data_canbox, 3, 0, 1, 3)
        self.price_pre_data_input_lineEdit = QtWidgets.QLineEdit(self.price_pre_data)
        self.price_pre_data_input_lineEdit.setText("")
        self.price_pre_data_input_lineEdit.setObjectName("price_pre_data_input_lineEdit")
        self.gridLayout.addWidget(self.price_pre_data_input_lineEdit, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.price_pre_data)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.price_pre_data)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.price_pre_data)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)
        self.price_pre_stack.addWidget(self.price_pre_data)
        self.price_pre_buildmodle = QtWidgets.QWidget()
        self.price_pre_buildmodle.setObjectName("price_pre_buildmodle")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.price_pre_buildmodle)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.price_pre_buildmodle)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_12 = QtWidgets.QLabel(self.price_pre_buildmodle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 3, 0, 1, 2)
        self.price_pre__modle_slectpath_button_1 = QtWidgets.QPushButton(self.price_pre_buildmodle)
        self.price_pre__modle_slectpath_button_1.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.price_pre__modle_slectpath_button_1.setFont(font)
        self.price_pre__modle_slectpath_button_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.price_pre__modle_slectpath_button_1.setObjectName("price_pre__modle_slectpath_button_1")
        self.gridLayout_3.addWidget(self.price_pre__modle_slectpath_button_1, 2, 1, 1, 1)
        self.price_pre_modle_lineEdit_5 = QtWidgets.QLineEdit(self.price_pre_buildmodle)
        self.price_pre_modle_lineEdit_5.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.price_pre_modle_lineEdit_5.setFont(font)
        self.price_pre_modle_lineEdit_5.setObjectName("price_pre_modle_lineEdit_5")
        self.gridLayout_3.addWidget(self.price_pre_modle_lineEdit_5, 4, 0, 1, 1)
        self.price_pre__modle_slectpath_button_2 = QtWidgets.QPushButton(self.price_pre_buildmodle)
        self.price_pre__modle_slectpath_button_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.price_pre__modle_slectpath_button_2.setFont(font)
        self.price_pre__modle_slectpath_button_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.price_pre__modle_slectpath_button_2.setObjectName("price_pre__modle_slectpath_button_2")
        self.gridLayout_3.addWidget(self.price_pre__modle_slectpath_button_2, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.price_pre_buildmodle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 2)
        self.price_pre_modle_lineEdit_4 = QtWidgets.QLineEdit(self.price_pre_buildmodle)
        self.price_pre_modle_lineEdit_4.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.price_pre_modle_lineEdit_4.setFont(font)
        self.price_pre_modle_lineEdit_4.setObjectName("price_pre_modle_lineEdit_4")
        self.gridLayout_3.addWidget(self.price_pre_modle_lineEdit_4, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.price_pre_buildmodle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 5, 0, 1, 1)
        self.price_pre_modle_lineEdit_6 = QtWidgets.QLineEdit(self.price_pre_buildmodle)
        self.price_pre_modle_lineEdit_6.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.price_pre_modle_lineEdit_6.setFont(font)
        self.price_pre_modle_lineEdit_6.setObjectName("price_pre_modle_lineEdit_6")
        self.gridLayout_3.addWidget(self.price_pre_modle_lineEdit_6, 6, 0, 1, 2)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.label_4 = QtWidgets.QLabel(self.price_pre_buildmodle)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.price_pre_buildmodle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 6, 1, 1)
        self.price_pre_modle_lineEdit_3 = QtWidgets.QLineEdit(self.price_pre_buildmodle)
        self.price_pre_modle_lineEdit_3.setMaximumSize(QtCore.QSize(125, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.price_pre_modle_lineEdit_3.setFont(font)
        self.price_pre_modle_lineEdit_3.setObjectName("price_pre_modle_lineEdit_3")
        self.gridLayout_2.addWidget(self.price_pre_modle_lineEdit_3, 0, 7, 1, 1)
        self.price_pre_modle_slecectmodle = QtWidgets.QComboBox(self.price_pre_buildmodle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price_pre_modle_slecectmodle.sizePolicy().hasHeightForWidth())
        self.price_pre_modle_slecectmodle.setSizePolicy(sizePolicy)
        self.price_pre_modle_slecectmodle.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.price_pre_modle_slecectmodle.setFont(font)
        self.price_pre_modle_slecectmodle.setObjectName("price_pre_modle_slecectmodle")
        self.price_pre_modle_slecectmodle.addItem("")
        self.price_pre_modle_slecectmodle.addItem("")
        self.gridLayout_2.addWidget(self.price_pre_modle_slecectmodle, 0, 1, 1, 1)
        self.price_pre_modle_lineEdit_2 = QtWidgets.QLineEdit(self.price_pre_buildmodle)
        self.price_pre_modle_lineEdit_2.setMaximumSize(QtCore.QSize(125, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.price_pre_modle_lineEdit_2.setFont(font)
        self.price_pre_modle_lineEdit_2.setObjectName("price_pre_modle_lineEdit_2")
        self.gridLayout_2.addWidget(self.price_pre_modle_lineEdit_2, 0, 5, 1, 1)
        self.price_pre_modle_lineEdit_1 = QtWidgets.QLineEdit(self.price_pre_buildmodle)
        self.price_pre_modle_lineEdit_1.setMaximumSize(QtCore.QSize(125, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.price_pre_modle_lineEdit_1.setFont(font)
        self.price_pre_modle_lineEdit_1.setObjectName("price_pre_modle_lineEdit_1")
        self.gridLayout_2.addWidget(self.price_pre_modle_lineEdit_1, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.price_pre_buildmodle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.price_pre_buildmodle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.price_pre_buildmodle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.price_pre_modle_lossbox = QtWidgets.QGroupBox(self.price_pre_buildmodle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.price_pre_modle_lossbox.sizePolicy().hasHeightForWidth())
        self.price_pre_modle_lossbox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.price_pre_modle_lossbox.setFont(font)
        self.price_pre_modle_lossbox.setAlignment(QtCore.Qt.AlignCenter)
        self.price_pre_modle_lossbox.setObjectName("price_pre_modle_lossbox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.price_pre_modle_lossbox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4.addWidget(self.price_pre_modle_lossbox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_4.setStretch(3, 2)
        self.verticalLayout_4.setStretch(4, 10)
        self.price_pre_stack.addWidget(self.price_pre_buildmodle)
        self.horizontalLayout_3.addWidget(self.price_pre_stack)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 8)
        self.stackedWidget_main.addWidget(self.page_pricepre)
        self.page_countpre = QtWidgets.QWidget()
        self.page_countpre.setObjectName("page_countpre")
        self.stackedWidget_main.addWidget(self.page_countpre)
        self.horizontalLayout.addWidget(self.stackedWidget_main)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_main.setCurrentIndex(0)
        self.price_pre_stack.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "主要功能"))
        self.pushButton_main_price.setText(_translate("MainWindow", "碳交易价格预测"))
        self.pushButton_main_count.setText(_translate("MainWindow", "碳成交量预测"))
        self.pushButton_main_elec.setText(_translate("MainWindow", "电力系统碳交易价格分析"))
        self.pushButton_price_data.setText(_translate("MainWindow", "数据加载"))
        self.pushButton_price_buildmodle.setText(_translate("MainWindow", "模型构建"))
        self.pushButton.setText(_translate("MainWindow", "模型测试"))
        self.pushButton_price_pred.setText(_translate("MainWindow", "数据预测"))
        self.price_pre_data_input_load_button.setText(_translate("MainWindow", "加载数据"))
        self.price_pre_data_input_slectpath_button.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "数据类型"))
        self.price_pre_data_canbox.setTitle(_translate("MainWindow", "数据查看"))
        self.comboBox.setItemText(0, _translate("MainWindow", "EXCEL"))
        self.comboBox.setItemText(1, _translate("MainWindow", "CSV"))
        self.comboBox.setItemText(2, _translate("MainWindow", "TXT"))
        self.label_6.setText(_translate("MainWindow", "数据路径"))
        self.label_2.setText(_translate("MainWindow", "数据加载"))
        self.label_5.setText(_translate("MainWindow", "模型信息"))
        self.label_12.setText(_translate("MainWindow", "超参数储存路径"))
        self.price_pre__modle_slectpath_button_1.setText(_translate("MainWindow", "..."))
        self.price_pre__modle_slectpath_button_2.setText(_translate("MainWindow", "..."))
        self.label_11.setText(_translate("MainWindow", "模型储存路径"))
        self.label_13.setText(_translate("MainWindow", "模型命名（前缀）"))
        self.label_4.setText(_translate("MainWindow", "参数设置"))
        self.label_9.setText(_translate("MainWindow", "epochs数量"))
        self.price_pre_modle_slecectmodle.setItemText(0, _translate("MainWindow", "LSTM"))
        self.price_pre_modle_slecectmodle.setItemText(1, _translate("MainWindow", "Transformer"))
        self.label_8.setText(_translate("MainWindow", "batch_size"))
        self.label_7.setText(_translate("MainWindow", "训练集比率"))
        self.label_10.setText(_translate("MainWindow", "模型选择"))
        self.price_pre_modle_lossbox.setTitle(_translate("MainWindow", "Loss图像"))
