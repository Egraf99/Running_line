from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


class App:
    def __init__(self, width_line, height_line):
        app = QApplication([])
        window = QWidget()
        window.setMinimumWidth(width_line)
        window.setWindowTitle('Бегущая строка')

        self.width = width_line
        self.height = height_line
        self.list_of_labels = []

        self.layout = QVBoxLayout()

        self.made_display()
        self.add_display()

        self.button = QPushButton('TOP')
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.click)

        window.setLayout(self.layout)
        window.show()
        app.exec_()

    def made_display(self):
        for count_label in range(self.height):
            self.list_of_labels.append(QLabel("-" * self.width))

    def add_display(self):
        for label in self.list_of_labels:
            self.layout.addWidget(label)

    def click(self):
        for label in self.list_of_labels:
            label.setText("+" * self.width)


if __name__ == '__main__':
    App(100, 5)