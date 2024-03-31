from PyQt5.QtCore import pyqtSignal

from carbon_pricepre import Ui_Form
from qtpy.QtWidgets import QApplication, QWidget

class price_pre_page(QWidget, Ui_Form):
    returnSignal = pyqtSignal()

    def __init__(self):
        super(price_pre_page, self).__init__()
        self.setupUi(self)

    def initUI(self):
        self.setLayout(self.gridLayout)
        self.returnButton.clicked.connect(self.returnSignal)

    def logic(self):
        print("logic")