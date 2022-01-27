from qt_core import *

FILE_UI = "view/MainWindow.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)


       
        