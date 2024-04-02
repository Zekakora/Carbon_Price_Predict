from PyQt6.QtWidgets import QMainWindow, QApplication
from carbon_morden import Ui_MainWindow
from carbon_pricepre_logic import price_pre_page
from PyQt6 import QtCore

"""
import sys

# from qdarkstyle.light.palette import LightPalette
# app = QtWidgets.QApplication(sys.argv)
# window = QtWidgets.QMainWindow()
# import qdarkstyle
# app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='PyQt6', palette=LightPalette()))

extra = {
    # Button colors
    'danger': '#dc3545',
    # 'warning': '#ffc107',
     'warning':'#CD9B1D',
    'success': '#17a2b8',
    # Font
    'font_family': '等线',
    'font_size': '24',
}


from qt_material import apply_stylesheet
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
apply_stylesheet(app, theme='light_blue.xml', extra=extra)
"""
import sys
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.stack_main.setCurrentIndex(0)
        self.pushButton_main_clean.setProperty('class', 'danger')
        self.pushButton_main_homepage.clicked.connect(lambda: self.goto_page_main(0))
        self.pushButton_main_price.clicked.connect(lambda: self.goto_page_main(1))
        self.pushButton_main_count.clicked.connect(lambda: self.goto_page_main(0))

        self.pricepage = price_pre_page()
        self.stack_main.addWidget(self.pricepage)
        # self.stack_main.addWidget(self.Qlable)
        # self.stack_main.addWidget(self.pricepage)
        # self.pushButton_main_elec.clicked.connect(lambda :self.goto_page_main(2))

    def goto_page_main(self, index):
        self.stack_main.setCurrentIndex(index)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    # app.installEventFilter(main)
    sys.exit(app.exec())
