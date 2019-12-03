import sys
import pyperclip
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

import mainLib as Lib


# pyinstaller --onefile --icon=cube.ico --clean mainPage.py


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
        # if low or high value is out of range do nothing only show warning
        if low == -1 and high == -1:
            self.result.setStyleSheet("font-weight: bold; color: red;")
            self.result.setText("Invalid input in both input field")
        elif low == -1:
            self.result.setStyleSheet("font-weight: bold; color: red;")
            self.result.setText("Invalid input in lower input field")
        elif high == -1:
            self.result.setStyleSheet("font-weight: bold; color: red;")
            self.result.setText("Invalid input in higher input field")
        # if low or high is in range do something near in comments under
        else:
            # compare low and high when high is lower than low return code
            help_num_res = Lib.compare_numbers(low, high)
            x = self.comboBox.currentText()
            # generate two numbers in range from 100 to 999 for safer generator
            if x == "safe generate":
                number1 = Lib.safe_gen()
                number2 = Lib.safe_gen()
                self.result.setText(str(number1) + " " + str(number2))
                self.result.setStyleSheet("Background: white")
            # other option from combo box
            else:
                if help_num_res == 2 or help_num_res == 1:
                    # switch high to low
                    if help_num_res == 2:
                        help_num = low
                        low = high
                        high = help_num
                    # generate audio random number in range
                    if x == "audio generate":
                        seed = Lib.generate_audio()
                        number = Lib.generate_in_range(low, high, seed)
                        self.result.setText(str(number))
                        self.result.setStyleSheet("Background: white")
                    # generate random number from time in range
                    elif x == "time generate":
                        seed = Lib.generate_time()
                        number = Lib.generate_in_range(low, high, seed)
                        self.result.setText(str(number))
                        self.result.setStyleSheet("Background: white")
                    # generate random number from memory in range
                    elif x == "memory generate":
                        seed = Lib.generate_memory()
                        number = Lib.generate_in_range(low, high, seed)
                        self.result.setText(str(number))
                        self.result.setStyleSheet("Background: white")
                    # test for safe generate
                    elif x == "Tests for safe generator":
                        i = 0
                        numbers = []
                        # create array for tests
                        while i < 21:
                            seed = Lib.seed_for_save_gen()
                            number = Lib.generate_in_range(100, 999, seed)
                            numbers.append(number)
                            i = i + 1
                        # calling test function and testing them when all is valid return block go green,
                        # when one of them fail, return bloc go red and show which one failed
                        monoRes = Lib.mono_test(numbers)
                        aprRes = Lib.approx_test(numbers)
                        if monoRes and aprRes:
                            self.result.setText("All test is valid")
                            self.result.setStyleSheet("Background: green")
                        elif not monoRes:
                            self.result.setText("Mono bit test is invalid")
                            self.result.setStyleSheet("Background: red")
                        elif not aprRes:
                            self.result.setText("Approximate entropy test is invalid")
                            self.result.setStyleSheet("Background: red")
                        else:
                            self.result.setText("All test is invalid")
                            self.result.setStyleSheet("Background: red")
                        Lib.generate_plot_small(numbers)
                    # test for audio in user range
                    elif x == "Tests for audio":
                        i = 0
                        numbers = []
                        # create array for tests
                        while i < 21:
                            seed = Lib.generate_audio()
                            number = Lib.generate_in_range(low, high, seed)
                            numbers.append(number)
                            i = i + 1
                        # calling test function and testing them when all is valid return block go green,
                        # when one of them fail, return bloc go red and show which one failed
                        monoRes = Lib.mono_test(numbers)
                        aprRes = Lib.approx_test(numbers)
                        if monoRes and aprRes:
                            self.result.setText("All test is valid")
                            self.result.setStyleSheet("Background: green")
                        elif not monoRes:
                            self.result.setText("Mono bit test is invalid")
                            self.result.setStyleSheet("Background: red")
                        elif not aprRes:
                            self.result.setText("Approximate entropy test is invalid")
                            self.result.setStyleSheet("Background: red")
                        else:
                            self.result.setText("All test is invalid")
                            self.result.setStyleSheet("Background: red")
                        Lib.generate_plot_small(numbers)
                    elif x == "Graph for multiple numbers":
                        seed = Lib.seed_for_save_gen()
                        Lib.generate_plot(low, high, seed)
                else:
                    self.result.setStyleSheet("font-weight: bold; color: red;")
                    self.result.setText("Invalid input range is a same number")

    # function for copy number on output bloc
    def on_click(self):
        pyperclip.copy(self.result.text())

    # fill combo box from multiple selection
    def fill_combo_box(self):
        options = ["safe generate", "memory generate", "time generate",
                   "audio generate", "Tests for safe generator", "Tests for audio", "Graph for multiple numbers"]
        for i in options:
            self.comboBox.addItem(i)

    # function for getting minimum value from user input
    def get_min(self):
        number = self.low.text()
        # when user don't type nothing return 0 from minimum value
        if not number:
            return 0
        # when user type number in range 0 <= number <= 2 ** 32 return number
        elif number.isdigit():
            if 0 <= int(number) <= (2 ** 32 - 1):
                return int(number)
            # when number is out of range return -1 as fail code
            else:
                return -1
        # when number is something other than digit return -1 as fail code
        else:
            return -1

    # function for getting minimum value from user input
    def get_max(self):
        number = self.high.text()
        # when user don't type nothing return 0 from maximal value
        if not number:
            return 2 ** 32
        elif number.isdigit():
            if 1 <= int(number) <= (2 ** 32):
                return int(number)
            # when number is out of range return -1 as fail code
            else:
                return -1
        # when number is something other than digit return -1 as fail code
        else:
            return -1


# this is for show gui
app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())
