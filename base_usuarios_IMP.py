#Essa classe é usada para simular o comportamento de uma referência de um banco de dados.
import base

def busca_por_indice(bas, ind):
    '''
    Devolve usuario numa busca por ind
    '''
    sql=("SElECT nome,sobrenome,nascDt,senha,email,cpf,endereco,telefone FROM usuarios WHERE ind = " + ind)
    base.executa_query(sql)
    console.log(f"Usuario {ind} devolvido")
    return True

def busca_por_email(bas,em):
    '''
    Retorna usuario por email se existente.
    '''
    
    sql=("SElECT nome,senha,email,cpf,endereco,telefone FROM usuarios WHERE email = " + em)
    base.executa_comando(sql)
    console.log(f"Usuario {em} devolvido")
    return True

def acrescenta(bas,usr):
    '''
    Acrescenta um novo usuario
    '''

    console.log(f"Usuario {usr.name} created")
    return 12345

def atualiza(bas,ind,usr):
    '''
    Atualiza usuario com as propriedades de usr
    '''
    console.log(f"Usuario {usr.id} updated")
    return 
