from model.clientes import Clientes
from qt_core import *
from controller.cadastre_se import cadastrese

FILE_UI = "view/MainWindow.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.cadastre_se = cadastrese()
        
        self.painel_principal.insertWidget(0, self.cadastre_se)

        self.cadastrese_btn.clicked.connect(self.show_cadastrese)
    
    def show_cadastrese(self):
        self.painel_principal.setCurrentIndex(0)    