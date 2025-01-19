from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Hello World")

        button = QPushButton("Click")
        self.setCentralWidget(button)

        button.clicked.connect(self.helloWorld)

    def helloWorld(self):
        print("Hello World")
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
