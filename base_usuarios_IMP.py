#Essa classe é usada para simular o comportamento de uma referência de um banco de dados.
import base
class BancoReferencia:
    def __init__(self, nome_banco, nome_usuario, senha):
        self.__nome_banco = nome_banco
        self.__nome_usuario = nome_usuario
        self.__senha = senha

    def conexao(self):
        '''
        Nesse caso vai sempre conectar
        '''
        return True

    def executa_busca(self, busca):
        console.log("Resultado da busca")
        return

#Connect to dabase


def acrescenta(bd_referencia, usr):
    '''
    Acrescenta um novo usuario
    '''

    console.log(f"Usuario {usr.name} created")
    return True

def busca_id(bd_referencia, id):
    '''
    Devolve usuario numa busca por id
    '''
    sql=("SElECT nome,sobrenome,nascDt,senha,email,cpf,endereco,telefone FROM usuarios WHERE id = " + id)
    base.executa_query(sql)
    console.log(f"Usuario {id} devolvido")
    return True

def busca_email(bd_referencia, email):
    '''
    Retorna usuario por email se existente.
    '''
    
    sql=("SElECT nome,sobrenome,nascDt,senha,email,cpf,endereco,telefone FROM usuarios WHERE email = " + email)
    base.executa_query(sql)
    console.log(f"Usuario {email} devolvido")
    return True

def atualiza(bd_referencia, usr):
    '''
    Atualiza usuario com as propriedades de usr
    '''
    console.log(f"Usuario {usr.id} updated")
    return True

def deleta(bd_referencia, usr_id):
    '''
    Deleta o usuario com id usr_id
    '''
    console.log(f"Usuario {usr_id} deletado")
    return True
