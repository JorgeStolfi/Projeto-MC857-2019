#Essa classe é usada para simular o comportamento de uma referência de um banco de dados.
import base

def busca_por_indice(bas,ind):
    sql="SELECT nome,senha,email,CPF,endereco,CEP,telefone FROM usuarios WHERE ind = " + ind
    resultado=base.executa_comando(sql)
    return resultado

def busca_por_email(bas,em):
    sql="SELECT nome,senha,CPF,endereco,CEP,telefone FROM usuarios WHERE email = " + em
    resultado=base.executa_comando(sql)
    return resultado

def busca_por_CPF(bas,CPF):
    sql="SELECT nome,senha,email,endereco,CEP,telefone FROM usuarios WHERE CPF = " + CPF
    resultado=base.executa_comando(sql)
    return resultado

def acrescenta(bas,usr):
    sql="INSERT INTO usuario (nome,senha,email,CPF,endereco,CEP,telefone) VALUES (" + usr.nome + ", " + usr.senha + ", " + usr.email + ", "
                                                                                    + usr.CPF + ", " + usr.endereco + ", " + usr.CEP + ", " + usr.telefone ");"
    base.executa_comando(sql)
    indice_inteiro=base.indice_inserido()
    return indice_inteiro

def atualiza(bas,ind,usr):
    sql="UPDATE usuario SET nome = " + usr.nome + ", senha = " + usr.senha + ", email = " + usr.email + ", CPF = " + usr.CPF + ", endereco = "
                                     + usr.endereco + ", CEP = " + usr.CEP + ", telefone = " + usr.telefone " WHERE ind = " + ind
