from qt_core import *
from controller.main_window import *

class cad_cliente (QWidget):
    def salvar(self):
        nome = self.nome.text()
        telefone = self.telefone.text()

class clientes (QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)
        

       

       