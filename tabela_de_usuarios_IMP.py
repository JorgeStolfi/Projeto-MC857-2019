#Essa classe é usada para simular o comportamento de uma referência de um banco de dados.
import base_sql
import identificador
import sys # Para depuração.

def cria_tabela(bas):
    campos =  \
    " indice integer NOT NULL PRIMARY KEY," + \
    " nome varchar(60) NOT NULL," + \
    " senha varchar(12) NOT NULL," + \
    " email varchar(60) NOT NULL," + \
    " CPF char(14) NOT NULL," + \
    " endereco varchar(180) NOT NULL," + \
    " CEP char(9) NOT NULL," + \
    " telefone varchar(24) NOT NULL"
    bas.executa_comando_CREATE_TABLE("usuarios", campos);

def acrescenta(bas, atrs):
    res = bas.executa_comando_INSERT("usuarios", )
    ind = bas.indice_inserido()
    id_usuario = identificador.de_indice("U", ind)
    return id_usuario

def busca_por_identificador(bas, id_usuario):
    ind = identificador.para_indice("U", id_usuario)
    cond = "indice = " + str(ind)
    colunas = ('nome','senha','email','CPF','endereco','CEP'',telefone')
    res = bas.executa_comando_SELECT("usuarios", cond, colunas)
    sys.stderr.write("res = " + str(res) + "\n")
    assert len(res) <= 1
    if len(res) == 0:
      return None
    else:
      valores = res[0]
      assert len(valores) == len(colunas)
      atrs = dict(zip(colunas, valores))
      return atrs

def busca_por_email(bas, em):
    cond = "email = '" + em + "'"
    res = bas.executa_comando_SELECT("usuarios", cond, ('indice'))
    sys.stderr.write("res = " + str(res) + "\n")
    assert len(res) <= 1
    if len(res) == 0:
      return None
    else:
      ind = res[0][0]
      id_usuario = identificador.de_indice("U", ind)
      return id_usuario

def busca_por_CPF(bas, CPF):
    cond = "CPF = '" + CPF + "'"
    res = bas.executa_comando_SELECT("usuarios", cond, ('indice'))
    sys.stderr.write("res = " + str(res) + "\n")
    assert len(res) <= 1
    if len(res) == 0:
      return None
    else:
      ind = res[0][0]
      id_usuario = identificador.de_indice("U", ind)
      return id_usuario

def atualiza(bas, id_usuario, atrs):
    ind = identificador.para_indice("U", id_usuario)
    cond = "indice = " + str(ind)
    res = bas.executa_comando_UPDATE("usuarios", cond, atrs)
    return
