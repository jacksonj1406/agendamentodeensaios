from model.clientes import Clientes
from qt_core import *
from controller.cadastre_se import cadastrese

FILE_UI = "view/janela_de_entrada.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(None)
        uic.loadUi(FILE_UI, self)
        self.novo_cadastro=None
 
        self.cadastrese_btn.clicked.connect(self.show_cadastrese)

    
    
    def show_cadastrese(self):
        self.janela_de_entrada.setCurrentIndex(0) 

       

        self.novo_cadastro.show() 