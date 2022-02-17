lista_agendamento= []


def adicionar( nova_agendamento):
    novo_id = len(lista_agendamento)
    nova_agendamento.id = novo_id
    lista_agendamento.append( nova_agendamento)

def pegaragendamento(id):
    for agendamento in lista_agendamento:
        if agendamento.id == id:
            return agendamento
    return None


def editar(agendamento):
    for i in range(0, len(lista_agendamento)):
        if agendamento.id == lista_agendamento[i].id:
            lista_agendamento[i] = agendamento


def excluir(id):
    for agendamento in lista_agendamento:
        if agendamento.id == id:
            lista_agendamento.remove(agendamento)