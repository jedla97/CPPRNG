import sys
import time

import pyperclip
from PyQt5.uic.uiparser import QtCore

import mainLib as Lib
from PyQt5.QtCore import pyqtSlot, QBasicTimer
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi


class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('C:\\Users\Jakub\PycharmProjects\CKPRNG\mainwindow.ui', self)
        x = self.fill_combo_box()
        self.generateNum.clicked.connect(self.take_text)
        self.copy.clicked.connect(self.on_click)

    # get selection from multiple chooses
    def take_text(self):
        low = self.get_min()
        high = self.get_max()
        if low == -1 and high == -1:
            self.result.setStyleSheet("font-weight: bold; color: red;")
            self.result.setText("Invalid input in both input field")
        elif low == -1:
            self.result.setStyleSheet("font-weight: bold; color: red;")
            self.result.setText("Invalid input in lower input field")
        elif high == -1:
            self.result.setStyleSheet("font-weight: bold; color: red;")
            self.result.setText("Invalid input in higher input field")
        else:
            help_num_res = Lib.compare_numbers(low, high)
            x = self.comboBox.currentText()
            if x == "safe generate":
                number1 = Lib.safe_gen()
                number2 = Lib.safe_gen()
                self.result.setText(str(number1) + " " + str(number2))
            else:
                if help_num_res == 2 or help_num_res == 1:
                    if help_num_res == 2:
                        help_num = low
                        low = high
                        high = help_num
                    if x == "          audio generate":
                        seed = Lib.generate_audio()
                        number = Lib.generate_in_range(low, high, seed)
                        self.result.setText(str(number))
                    elif x == "   show graphs for testing":
                        Lib.generate_plot()
                    elif x == "           time generate":
                        seed = Lib.generate_time()
                        number = Lib.generate_in_range(low, high, seed)
                        self.result.setText(str(number))
                    elif x == "       memory generate":
                        seed = Lib.generate_memory()
                        number = Lib.generate_in_range(low, high, seed)
                        self.result.setText(str(number))
                    elif x == "          safe generate":
                        number1 = Lib.safe_gen()
                        number2 = Lib.safe_gen()
                        self.result.setText(str(number1) + " " + str(number2))
                else:
                    self.result.setStyleSheet("font-weight: bold; color: red;")
                    self.result.setText("Invalid input range is a same number")

    # testing function when click on generate button
    def on_click_gen(self):
        # numbers = self.plainTextEdit_higher.toPlainText()
        numbers = self.comboBox.toPlainText()
        self.textEdit_output.setText(str(numbers))

    def on_click(self):
        pyperclip.copy(self.result.text())

    # fill combo box from multiple selection
    def fill_combo_box(self):
        options = ["          safe generate", "       memory generate", "           time generate",
                   "          audio generate", "   show graphs for testing"]
        for i in options:
            self.comboBox.addItem(i)

    def get_min(self):
        number = self.low.text()
        if not number:
            return 0
        elif number.isdigit():
            if 0 <= int(number) <= (2 ** 32 - 1):
                return int(number)
            else:
                return -1
        else:
            return -1

    def get_max(self):
        number = self.high.text()
        if not number:
            return 2 ** 32
        elif number.isdigit():
            if 1 <= int(number) <= (2 ** 32):
                return int(number)
            else:
                return -1
        else:
            return -1


app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())
