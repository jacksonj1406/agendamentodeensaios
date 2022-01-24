
lista_clientes = []


def adicionar(novo_cliente):

    novo_id = len(lista_clientes)
    novo_cliente.id =  novo_id
  
    lista_clientes.append(novo_cliente)




def pegarClientes(id):
    
    for clientes in lista_clientes:
        if clientes.id == id: 
            return clientes  

    
    return None 



def editar(cliente):
  
    for index in range(0, len(lista_clientes)):
        
        cliente_atual = lista_clientes[index]
        if cliente.id == cliente_atual.id:
           
            lista_clientes[index] = cliente




def excuir(id_cliente):
    for index in range(0, len(lista_clientes)):
        cliente_atual = lista_clientes[index]
        if id_cliente == cliente_atual.id:
            del lista_clientes[index]
          
            return  




def listar_todos():
   
    for cliente in lista_clientes:
        cliente.imprime()




def lista_cliente(id):
    pass
