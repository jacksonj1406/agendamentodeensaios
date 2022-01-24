from qt_core import *
from controller.cad_cliente import clientes
FILE_UI = "view/MainWindow.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)


       
        