import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_1.clicked.connect(lambda: self.get_number_from_button_clicked('1'))
        self.ui.pushButton_2.clicked.connect(lambda: self.get_number_from_button_clicked('2'))
        self.ui.pushButton_3.clicked.connect(lambda: self.get_number_from_button_clicked('3'))
        self.ui.pushButton_4.clicked.connect(lambda: self.get_number_from_button_clicked('4'))
        self.ui.pushButton_5.clicked.connect(lambda: self.get_number_from_button_clicked('5'))
        self.ui.pushButton_6.clicked.connect(lambda: self.get_number_from_button_clicked('6'))
        self.ui.pushButton_7.clicked.connect(lambda: self.get_number_from_button_clicked('7'))
        self.ui.pushButton_8.clicked.connect(lambda: self.get_number_from_button_clicked('8'))
        self.ui.pushButton_9.clicked.connect(lambda: self.get_number_from_button_clicked('9'))
        self.ui.pushButton_0.clicked.connect(lambda: self.get_number_from_button_clicked('0'))
        self.ui.pushButton_00.clicked.connect(lambda: self.get_number_from_button_clicked('00'))
        self.ui.pushButton_backspace.clicked.connect(self.remove_last_element)

        self.ui.pushButton_min.clicked.connect(lambda: self.add_to_label('-'))
        self.ui.pushButton_plus.clicked.connect(lambda: self.add_to_label('+'))
        self.ui.pushButton_mul.clicked.connect(lambda: self.add_to_label('x'))
        self.ui.pushButton_div.clicked.connect(lambda: self.add_to_label('÷'))



        self.ui.pushButton_pi.clicked.connect(lambda: self.add_to_label('π'))

        self.ui.pushButton_clear.clicked.connect(self.clear_label)
        self.ui.pushButton_point.clicked.connect(lambda: self.add_to_label(','))
        # self.ui

    def get_number_from_button_clicked(self, number_from_button):
        self.correct_any_letters_present()
        return self.add_to_label(number_from_button)

        
    def add_to_label(self, char: str):
        text_before = self.ui.label_1.text()
        if self.check_if_length_more_than_0(text_before):
            if char in '+-÷x,':
                if not self.check_if_special_char_is_the_last_in_label():
                    self.ui.label_1.setText(text_before + char)
                else:
                    self.ui.label_1.setText(text_before[:-1]+char)
            elif char in 'π':
                if not self.check_if_pi_is_the_last_in_label():
                    self.ui.label_1.setText(text_before + char)
            elif char in "0123456789":
                if not self.check_if_pi_is_the_last_in_label():
                    self.ui.label_1.setText(text_before + char)

        elif char in "0123456789":
            self.ui.label_1.setText(text_before + char)


    def correct_any_letters_present(self):
        text_before = self.ui.label_1.text()
        if self.check_if_length_more_than_0(text_before):
            for char in text_before:
                condition1 = char in "+-÷x,"
                condition2 = char in "π"
                condition3 = char in "1234567890"
                if condition1 or condition2 or condition3:
                    text_before.replace(char, '')


    def check_if_special_char_is_the_last_in_label(self) -> bool:
        text_before = self.ui.label_1.text()

        if text_before[-1] in "+-÷x,":
            return True
        return False


    def check_if_pi_is_the_last_in_label(self) -> bool:
        text_before = self.ui.label_1.text()
        if self.check_if_length_more_than_0(text_before):
            if "π" in text_before[-1]:
                return True
        return False


    def check_if_length_more_than_0(self, text):
        if len(text) > 0:
            return True
        return False

    def remove_last_element(self):
        text_before = self.ui.label_1.text()
        if self.check_if_length_more_than_0(text_before):
            self.ui.label_1.setText(text_before[:-1])


    def clear_label(self):
        self.ui.label_1.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
