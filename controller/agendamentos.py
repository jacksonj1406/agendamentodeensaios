from controller.cad_agendamento import FILE_UI, agendamentoWindow 
from model.agendamento_dao import*
from qt_core import*  

FILE_UI = 'View/agendamento.ui'

class agendamento(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.agentamento_window = None
        self.carrega_dados() 
        
        self.Agendar_btn.clicked.connect(self.Agendar)

        self.tabela.verticalHeader().setVisible(False)

        