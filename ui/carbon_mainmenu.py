# Form implementation generated from reading ui file 'carbon_mainmenu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import base64
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon

from ui import icons

extra = {
    # Button colors
    'danger': '#dc3545',
    # 'warning': '#ffc107',
    'warning': '#CD9B1D',
    'success': '#17a2b8',
    # Font
    'font_family': ['等线','微软雅黑','楷体'],
    'font_size': '24',
}


from qt_material import apply_stylesheet
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
apply_stylesheet(app, theme='light_blue.xml', extra=extra)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1412, 590)

        icon = QIcon()
        icon.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage.fromData(base64.b64decode(icons.flower))))
        self.setWindowIcon(icon)
        MainWindow.setObjectName("MainWindow")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton_main_homepage = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        self.pushButton_main_homepage.setFont(font)
        self.pushButton_main_homepage.setObjectName("pushButton_main_homepage")
        self.verticalLayout.addWidget(self.pushButton_main_homepage)
        self.pushButton_main_price = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        self.pushButton_main_price.setFont(font)
        self.pushButton_main_price.setObjectName("pushButton_main_price")
        self.verticalLayout.addWidget(self.pushButton_main_price)
        self.pushButton_main_count = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        self.pushButton_main_count.setFont(font)
        self.pushButton_main_count.setObjectName("pushButton_main_count")
        self.verticalLayout.addWidget(self.pushButton_main_count)
        self.pushButton_main_elec = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        self.pushButton_main_elec.setFont(font)
        self.pushButton_main_elec.setObjectName("pushButton_main_elec")
        self.verticalLayout.addWidget(self.pushButton_main_elec)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_main_clean = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        self.pushButton_main_clean.setFont(font)
        self.pushButton_main_clean.setObjectName("pushButton_main_clean")
        self.verticalLayout.addWidget(self.pushButton_main_clean)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.stack_main = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stack_main.setObjectName("stack_main")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(parent=self.page)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.page)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.stack_main.addWidget(self.page)
        self.horizontalLayout.addWidget(self.stack_main)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "主要功能"))
        self.pushButton_main_homepage.setText(_translate("MainWindow", "首页/项目介绍"))
        self.pushButton_main_price.setText(_translate("MainWindow", "碳交易价格预测"))
        self.pushButton_main_count.setText(_translate("MainWindow", "碳成交量预测"))
        self.pushButton_main_elec.setText(_translate("MainWindow", "电力系统碳交易价格分析"))
        self.pushButton_main_clean.setText(_translate("MainWindow", "清空全部图像"))
        self.label_2.setText(_translate("MainWindow", "绿水青山就是金山银山"))
        self.label_3.setText(_translate("MainWindow", "                                --习近平"))
