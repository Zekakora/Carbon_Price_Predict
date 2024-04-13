from PyQt6.QtCore import pyqtSignal, QTimer
from PyQt6.QtWidgets import QFileDialog, QCheckBox, QMessageBox, QLineEdit
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from carbon_pricepre import Ui_carbon_price_pre_widget
from qtpy.QtWidgets import QApplication, QWidget
import carbon_pricepre_modle_logic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# class MyFigure(FigureCanvas):
#     def __init__(self, width=5, height=4, dpi=100):
#         self.fig = Figure(figsize=(width, height), dpi=dpi)
#         super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
#         self.axes = self.fig.add_subplot(111)


class price_pre_page(QWidget, Ui_carbon_price_pre_widget):

    def __init__(self):
        super(price_pre_page, self).__init__()

        self.setupUi(self)
        self.price_pre_stack.setCurrentIndex(0)

        self.pushButton_start_test_modle.setProperty('class', 'danger')
        self.pushButton_start_train.setProperty('class', 'danger')
        self.pushButton_autotune.setProperty('class', 'warning')
        self.label_checkbox_notice.setProperty('class', 'warning')
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
        self.pushButton_start_train.clicked.connect(self.train_modle)
        self.pushButton_start_test_modle.clicked.connect(self.test_modle)
        # self.price_pre_data_input_load_button.clicked.connect(lambda: self.getdata(self.filepath_1t.text()))

        # 保存的变量
        self.df = None
        self.checkboxes_columns = []
        self.text_x, self.test_y, self.train_x, self.train_y = None, None, None, None

        # 绘图画布
        # self.pricepre_load_realcanva = FigureCanvas(plt.Figure())
        # self.pricepre_load_canva.addWidget(self.pricepre_load_realcanva)
        # self.pricepre_load_realcanva.figure.patch.set_facecolor('none')
        # self.pricepredata_figure = plt.subplots()
        # self.pricepredata_canva = FigureCanvas(self.pricepredata_figure)

        self.pic = Figure(figsize=(1000, 300), dpi=70)
        self.pic.patch.set_facecolor('none')

        self.losspic = Figure(figsize=(1000, 300), dpi=100)
        self.losspic.patch.set_facecolor('none')

        self.testpic = Figure(figsize=(1000, 400), dpi=80)
        self.testpic.patch.set_facecolor('none')

        # 加载区域
        self.canva_test = FigureCanvas(self.testpic)
        self.modletest_canva_area.addWidget(self.canva_test)

        self.canva_loaddata = FigureCanvas(self.pic)
        self.pricepre_load_picarea.addWidget(self.canva_loaddata)

        self.canva_loss = FigureCanvas(self.losspic)
        self.pricepre_lossarea.addWidget(self.canva_loss)

        """
        self.icloss = Figure(figsize=(5, 4), dpi=100)
        self.canvas_loss = FigureCanvas(self.icloss)
        self.verticalLayout.addWidget(self.canvas_loss)
        
        self.icloss.clf()
        self.canvas_loss.draw()
        Loss = self.icloss.add_subplot(111)
        Loss.plot(range(1, len(total_loss) + 1), total_loss, 'bo', label='trainloss')
        Loss.plot(range(1, len(total_vaildloss) + 1), total_vaildloss, 'r', label='validloss')
        Loss.set_title('loss_figure')
        Loss.set_ylabel('loss')
        Loss.set_xlabel('epoch_num')
        Loss.legend()
"""

    def train_modle(self):
        try:
            ratio = float(self.price_pre_modle_lineEdit_1.text())
            batch_size = int(self.price_pre_modle_lineEdit_2.text())
            epochs = int(self.price_pre_modle_lineEdit_3.text())
            mpath = self.filepath_2t.text()
            # ppath = self.filepath_3t.text()
            rename = self.price_pre_modle_lineEdit_6.text()
            if all(batch_size and ratio and epochs and mpath and rename):
                train_x, train_y, test_x, test_y, loss, val_loss = (
                    carbon_pricepre_modle_logic.train_model
                    (self.df, ratio=ratio, batch_size=batch_size, epochs=epochs,
                     mpath=mpath, rename=rename))
                # print(train_x, train_y, test_x, test_y, loss, val_loss)
                self.losspic.clf()
                self.canva_loss.draw()

                # 绘图
                loss_pic = self.losspic.add_subplot(111)
                loss_pic.plot(range(1, len(loss) + 1), loss, 'r', label='trainloss')
                loss_pic.plot(range(1, len(loss) + 1), val_loss, 'bo', label='validloss')
                loss_pic.patch.set_facecolor('none')
                loss_pic.legend()
                self.losspic.tight_layout()
                self.canva_loss.draw()
        except Exception as e:
            QMessageBox.critical(self, '出错啦', str(e))

    def test_modle(self):
        try:
            ratio = float(self.price_pre_modle_lineEdit_1.text())
            mpath = self.filepath_4t.text()
            if ratio and mpath:
                self.train_x, self.train_y, test_x, test_y = carbon_pricepre_modle_logic.cookdata(self.df, ratio=ratio)

                if (self.comboBox_2.currentIndex == 0):
                    # self.train_x = train_x
                    # self.train_y = train_y
                    data_x = self.train_x
                    data_y = self.train_y
                elif (self.comboBox_2.currentIndex == 1):
                    self.test_x = test_x
                    self.test_y = test_y
                    data_x = self.test_x
                    data_y = self.test_y
                else:
                    data_x = self.train_x
                    data_y = self.train_y

                result, mse, r2, mae = carbon_pricepre_modle_logic.test_model(mpath, data_x, data_y)

                self.testpic.clf()
                self.canva_test.draw()
                test_pic = self.testpic.add_subplot(111)
                test_pic.plot(data_y, 'r', label='Original')
                test_pic.plot(result, 'b', label='Predict')
                test_pic.patch.set_facecolor('none')
                test_pic.legend()
                self.testpic.tight_layout()
                self.canva_test.draw()

                self.price_test_RMSE_lable.setText(str(mse))
                self.price_test_RMSE_lable_2.setText(str(mae))
                self.price_test_RMSE_lable_3.setText(str(r2))

        except Exception as e:
            QMessageBox.critical(self, '出错啦', str(e))

    def getdata(self):
        path = self.filepath_1t.text()
        print(path)
        try:
            self.df, dfhead, column_names = carbon_pricepre_modle_logic.get_data(path,
                                                                                 self.comboBox_datatype.currentText())
            self.load_columns(column_names)
        except Exception as e:
            QMessageBox.critical(self, '出错啦', str(e))

    def load_columns(self, column_names):
        try:
            if self.checkboxes_columns:
                for checkbox in self.checkboxes_columns:
                    self.price_pre_data_checkbox.removeWidget(checkbox)
                    checkbox.deleteLater()
                self.checkboxes_columns = []
            else:
                pass

            for i, column_name in enumerate(column_names):
                row = i // 6  # 行索引
                column = i % 6  # 列索引
                checkbox = QCheckBox(column_name)
                checkbox.stateChanged.connect(self.check_box_notice)
                self.checkboxes_columns.append(checkbox)
                self.price_pre_data_checkbox.addWidget(checkbox, row, column)
        except Exception as e:
            QMessageBox.critical(self, '出错啦', str(e))

    def real_load_and_plot(self):
        try:

            self.pic.clf()
            self.canva_loaddata.draw()
            columns = self.get_checked_columns()
            df = self.df[columns]
            num_cols = len(columns)

            cookdata = self.comboBox_precaldata.currentIndex()
            if cookdata == 0:
                df = carbon_pricepre_modle_logic.iso_tree(df=df)
            else:
                pass

            for i in range(num_cols):
                column = columns[i]
                loaddata_pic = self.pic.add_subplot(num_cols, 1, i + 1)
                loaddata_pic.scatter(range(len(df[column])), df[column], s=5)
                loaddata_pic.patch.set_facecolor('none')
                loaddata_pic.set_title(column)
            self.pic.tight_layout()
            self.canva_loaddata.draw()

            self.df = df

        except Exception as e:
            QMessageBox.critical(self, '出错啦', str(e))

    def get_checked_columns(self):
        selected_columns = []
        for checkbox in self.checkboxes_columns:
            if checkbox.isChecked():
                text = checkbox.text()
                selected_columns.append(text)

        # 输出被选中的列名
        print("被选中的列名：", selected_columns)
        return selected_columns

    def check_box_notice(self):
        if len(self.get_checked_columns()) > 5:
            self.label_checkbox_notice.setText("变量过多可能会影响结果")
        else:
            self.label_checkbox_notice.setText("")

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
