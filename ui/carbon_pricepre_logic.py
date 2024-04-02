from PyQt6.QtCore import pyqtSignal, QTimer
from PyQt6.QtWidgets import QFileDialog, QCheckBox, QMessageBox, QLineEdit

from carbon_pricepre import Ui_carbon_price_pre_widget
from qtpy.QtWidgets import QApplication, QWidget
import carbon_pricepre_modle_logic


class price_pre_page(QWidget, Ui_carbon_price_pre_widget):

    def __init__(self):
        super(price_pre_page, self).__init__()
        self.setupUi(self)
        self.price_pre_stack.setCurrentIndex(0)

        self.pushButton_start_test_modle.setProperty('class', 'danger')
        self.pushButton_start_train.setProperty('class', 'danger')
        self.pushButton_autotune.setProperty('class', 'warning')
        self.pushButton_price_data.clicked.connect(lambda: self.goto_page_pre(0))
        self.pushButton_price_buildmodle.clicked.connect(lambda: self.goto_page_pre(1))
        self.pushButton_autotune.clicked.connect(lambda: self.goto_page_pre(2))
        self.pushButton_modletest.clicked.connect(lambda: self.goto_page_pre(3))
        self.pushButton_price_pred.clicked.connect(lambda: self.goto_page_pre(4))

        self.filepath_1b.clicked.connect(lambda: self.choosefile(1))
        self.filepath_2b.clicked.connect(lambda: self.choosepath(2))
        self.filepath_3b.clicked.connect(lambda: self.choosepath(3))
        self.filepath_4b.clicked.connect(lambda: self.choosefile(4))
        self.filepath_5b.clicked.connect(lambda: self.choosefile(5))
        self.filepath_6b.clicked.connect(lambda: self.choosefile(6))
        # self.filepath_7b.clicked.connect(lambda: self.choosefile(7))

        # self.column_names = None
        self.price_pre_data_input_load_button.clicked.connect(self.getdata)
        self.price_pre_data_input_load_button_2.clicked.connect(self.real_load_and_plot)
        # self.price_pre_data_input_load_button.clicked.connect(lambda: self.getdata(self.filepath_1t.text()))

        # 保存的变量
        self.df = None
        self.checkboxes_columns = []
    def getdata(self):
        path = self.filepath_1t.text()
        print(path)
        try:
            self.df, dfhead, column_names = carbon_pricepre_modle_logic.get_data(path, self.comboBox_datatype.currentText())
            self.load_columns(column_names)
        except Exception as e:
            QMessageBox.critical(self, '出错啦', str(e))

    def load_columns(self, column_names):
        try:
            for i, column_name in enumerate(column_names):
                row = i // 5  # 行索引
                column = i % 5  # 列索引
                checkbox = QCheckBox(column_name)
                self.checkboxes_columns.append(checkbox)
                self.price_pre_data_checkbox.addWidget(checkbox, row, column)
        except Exception as e:
            QMessageBox.critical(self, '出错啦', str(e))

        # for i, column_name in enumerate(column_names):
        #     row = i // 5  # 行索引
        #     column = i % 5  # 列索引
        #     checkbox = QCheckBox(column_name)
        #     checkbox.setChecked(True)
        #     self.price_pre_data_checkbox.addWidget(checkbox, row, column)

    def real_load_and_plot(self):
        selected_columns = []

        for checkbox in self.checkboxes_columns:
            if checkbox.isChecked():
                text = checkbox.text()
                selected_columns.append(text)

        # 输出被选中的列名
        print("被选中的列名：", selected_columns)

    def goto_page_pre(self, index):
        self.price_pre_stack.setCurrentIndex(index)

    def choosefile(self, index):
        fname, _ = QFileDialog.getOpenFileName(None, '选择文件')
        if fname:  # 如果用户选择了文件
            fname = str(fname)
            getattr(self, f"filepath_{index}t").setText(fname)
            # setattr(self, f"filepath_{index}t", fname)
            # self.status_label.setText("已选择文件{}".format(index))

    def choosepath(self, index):
        fname = QFileDialog.getExistingDirectory(None, '选择路径')
        if fname:  # 如果用户选择了文件
            fname = str(fname)
            getattr(self, f"filepath_{index}t").setText(fname)
            # setattr(self, f"filepath_{index}t", fname)
            # self.status_label.setText("已选择路径{}".format(index))
