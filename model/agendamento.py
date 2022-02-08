class agendamento():
    def __init__(self, id, Data,Horario,Local):
        
        self.id = id 
        self.Data = Data
        self.Horario = Horario
        self.Local = Local
    
    def imprime(self):
        print(f'{self.id}, {self.nome}, {self.telefone}')