from qt_core import *
from controller.main_window import *
from model.clientes import Clientes
 
 

FILE_UI = 'view/cad_cliente.ui'        

class novo_cadastro(QWidget):
    def __init__(self,janera_MainWindow):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.janela_MainWindow = janera_MainWindow
        
        self.cadastrese_btn.clicked.connect(self.cadastrese)
        self.Lista_de_ensaio_btn.clicked.connect(self.Lista_de_ensaio)


        

       

       