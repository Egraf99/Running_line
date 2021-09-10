from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer

from running_text import QTRunningLine
import sys


class App:
    def __init__(self, width_line, height_line):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setMinimumWidth(width_line)
        self.window.setWindowTitle('Бегущая строка')

        self.timer = QTimer()
        self.check_move = False
        self.timeout = 100
        self.first_column = 0
        self.width_text = 1

        self.width = width_line
        self.height = height_line
        self.list_of_qlabels = []

        self.init_run_line()

        self.layout = QVBoxLayout()

        self.made_display()
        self.add_display()

        self.start_but = QPushButton('Start')
        self.stop_but = QPushButton('Stop')
        self.layout.addWidget(self.start_but)
        self.layout.addWidget(self.stop_but)

        self.start_but.clicked.connect(self.start)
        self.stop_but.clicked.connect(self.stop)

        self.window.setLayout(self.layout)
        self.window.show()
        sys.exit(app.exec_())

    def init_run_line(self):
        self.run_line = QTRunningLine(self.width, self.height, 3)
        self.run_line.update_board()
        self.run_line.set_text('нннннн')

    def made_display(self):
        for string in self.run_line.board:
            self.list_of_qlabels.append(QLabel(string))

    def add_display(self):
        for label in self.list_of_qlabels:
            self.layout.addWidget(label)

    def start(self):
        if not self.check_move:
            self.check_move = True
            self.timer.start(self.timeout)
            self.timer.timeout.connect(self.show_run_line)

    def show_run_line(self):
        self.run_line.change_row_with_column()

        for n, qlabel in enumerate(self.list_of_qlabels):
            qlabel.setText(self.run_line.board[n])

    def stop(self):
        self.check_move = False
        self.timer.stop()
        try:
            self.timer.timeout.disconnect()
        except TypeError:
            pass


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Oбнаружена ошибка !:", tb)
    # QtWidgets.QApplication.quit()             # !!! если вы хотите, чтобы событие завершилось


sys.excepthook = excepthook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    App(50, 7)
