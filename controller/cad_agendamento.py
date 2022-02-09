from threading import local
from  model.agendamento_dao import *
from qt_core import*
from model.agendamento_dao import agendamento_dao

FILE_UI = 'View/agendamento.ui'


class agendamentoWindow(QWidget):
     def __init__(self,agendamento):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        self.janela_agendamento = agendamento

        self.Agendar_btn.clicked.connect(self.Agendar)


     def Agendar(self):
        Data = self.Data.text()
        Horario = self.Horario.text()
        Local = self.Local.text()

        
        nova_agendamento =  agendamentoWindow (None, Data, Horario, Local)
        agendamento_dao.adicionar( agendamentoWindow)

     
        self.janela_agendamento.carrega_dados()

    
        self.close()
 