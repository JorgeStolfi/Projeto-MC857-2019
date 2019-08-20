# Funções para gerenciar o banco de usuários.

# Implementação desta interface:


#Funções exportadas desta interface:
import base_usuario_IMP

#Conecta no banco
def conecta_ao_banco(nome_banco, nome_usuario, senha):
    '''
    Tenta conectar ao banco
    '''
    banco_referencia = base_usuario_IMP.conecta_ao_banco(nome_banco, nome_usuario, senha)

    if banco_referencia is None:
        console.log("Erro tentando conectar ao banco")
    return banco_referencia

def acrescenta(bd_referencia, usr):
    '''
    Acrescenta novo Usuario
    '''
    return base_usuario_IMP.acrescenta(bd_referencia, usr)

def busca_por_id(bd_referencia, id):
    '''
    Busca usuario por id
    '''
    return base_usuario_IMP.busca_por_id(bd_referencia, id)

def busca_por_email(bd_referencia, email):
    '''
    Busca usuario por email
    '''
    return base_usuario_IMP.busca_por_email(bd_referencia, email)

def atualiza(bd_referencia, usr):
    '''
    Atualiza usuario com as propriedades de usr
    '''
    return base_usuario_IMP.atualiza(bd_referencia, usr)

def deleta(bd_referencia, usr_id):
    '''
    Deleta usuario por id
    '''
    return base_usuario_IMP.deleta(usr_id)
