from qt_core import *
from controller.main_window import *

class cad_cliente (QWidget):
    def salvar(self):
        nome = self.nome.text()
        telefone = self.telefone.text()
       