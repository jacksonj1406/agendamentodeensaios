from msilib.schema import File
from model.clientes import Clientes
from qt_core import *
from controller.cadastre_se import cadastrese


FILE_UI = "view/janela_de_entrada.ui" 
File_ui='view/novo_cadastro.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(None)
        uic.loadUi(FILE_UI, self,File_ui, self)

        self.novo_cadastro=None
 
        self.cadastrese_btn.clicked.connect(self.cadastrese)

    def show_cadastrese(self):

        self.novo_cadastro=NovoCadastro()

        self.novo_cadastro.show() 