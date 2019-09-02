#Essa classe é usada para simular o comportamento de uma referência de um banco de dados.
import base

def busca_por_indice(bas,ind):
    cmd="SELECT nome,senha,email,CPF,endereco,CEP,telefone FROM usuarios WHERE ind = " + ind
    resultado=bas.executa_comando(cmd)
    return resultado

def busca_por_email(bas,em):
    cmd="SELECT nome,senha,CPF,endereco,CEP,telefone FROM usuarios WHERE email = " + em
    resultado=bas.executa_comando(cmd)
    return resultado

def busca_por_CPF(bas,CPF):
    cmd="SELECT nome,senha,email,endereco,CEP,telefone FROM usuarios WHERE CPF = " + CPF
    resultado=bas.executa_comando(cmd)
    return resultado

def acrescenta(bas,usr):
    atrs = usr.obtem_atributos();
    nomes = "nome,senha,email,CPF,endereco,CEP,telefone"
    valores = \
      atrs["nome"] + ", " + \
      atrs["senha"] + ", " + \
      atrs["email"] + ", " + \
      atrs["CPF"] + ", " + \
      atrs["endereco"] + ", " + \
      atrs["CEP"] + ", " + \
      atrs["telefone"]
    cmd="INSERT INTO usuarios (" + nomes + ") VALUES (" + valores + ");"
    bas.executa_comando(cmd)
    indice_inteiro=base.indice_inserido()
    return indice_inteiro

def atualiza(bas,ind,usr):
    atrs = usr.obtem_atributos();
    pares = \
      "nome = " + atrs["nome"] + ", " + \
      "senha = " + atrs["senha"] + ", " + \
      "email = " + atrs["email"] + ", " + \
      "CPF = " + atrs["CPF"] + ", " + \
      "endereco = " + atrs["endereco"] + ", " + \
      "CEP = " + atrs["CEP"] + ", " + \
      "telefone = " + atrs["telefone"]
    cmd="UPDATE usuarios SET " + pares + " WHERE ind = " + ind
    bas.executa_comando(cmd)
