from qt_core import *

FILE_UI = 'view/novo_cadastro.ui'

class cadastrese(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)