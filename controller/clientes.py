from qt_core import *
from controller.cad_cliente import *

FILE_UI = 'view/novo_cadastro.ui'

class cliente(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.novo_cadastro = None

        self.carrega_dados() 

        self.salvar_btn.clicked.connect(self.salvar)


    def novo_cadastro(self):
        self.novo_cadastro = novo_cadastreoWindow(self)
        self.novo_cadastro.show()