# Funções para gerenciar o banco de usuários.

# Implementação desta interface:


#Funções exportadas desta interface:
import base_usuarios_IMP

#Conectar ao banco de dados
def conecta_ao_banco(nome_do_banco, nome_de_usuario, senha):
    '''
    Tenta conectar-se ao banco de dados
    '''
    referencia_ao_banco = base_usuarios_IMP.conecta_ao_banco(nome_do_banco, nome_de_usuario, senha)

    if referencia_ao_banco is None:
        console.log("Erro ao tentar conectar-se ao banco de dados")
    return referencia_ao_banco

def recupera_por_id(referencia_ao_banco, id):
    '''
    Recupera usuários através de seus id's
    '''
    return base_usuarios_IMP.recuperar_por_id(id)

def recupera_por_email(referencia_ao_banco, email):
    '''
    Recupera o usuário através de seu endereco de email
    '''
    return base_usuarios_IMP.recupera_por_email(email)

def deleta(referencia_ao_banco, id):
    '''
    Deleta o usuáro através de seu id
    '''
    return base_usuarios_IMP.deleta(id)

def executa_query(referencia_ao_banco, sql_query):
    '''
    Executa uma query que está indicada através da variável sql_query
    '''
    return base_usuarios_IMP.executa_query(sql_query)
