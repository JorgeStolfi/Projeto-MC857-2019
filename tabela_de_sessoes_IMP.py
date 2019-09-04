import base_sql

def busca_por_indice(bas,ind):
    cmd = "SELECT * FROM sessoes WHERE id=" +ind
    sessao = bas.executa_comando(cmd)
    return sessao

def acrescenta(bas,ses):
    nomes = "usr, sessao_aberta"
    usr = ses.obtem_usuario()
    uid = (usr.obtem_identificador() if usr != None else None)
    valores = \
      str(uid) + ", " + \
      str(ses.aberta())
    cmd = "INSERT INTO sessoes (" + nomes + ") VALUES (" + valores + ")"
    bas.executa_comando(cmd)
    return bas.indice_inserido()

def atualiza(bas,ind,ses):
    usr = ses.obtem_usuario()
    uid = (usr.obtem_identificador() if usr != None else None)
    pares = \
      "usr=" + str(uid) + ", " + \
      "sessao_aberta=" + str(ses.aberta())
    cmd = "UPDATE sessoes SET " + pares +  " WHERE id=" + str(ind)
    bas.executa_comando(cmd)

def cria_tabela(bas):
    cmd = "CREATE TABLE sessoes (" + \
          "id_sessao varchar(255)" + \
          "id_usuario varchar(255)" + \
          "aberta boolean" + \
          ");"
    sessao = bas.executa_comando(cmd)
    return sessao

def busca_por_identificador(bas, id_sessao):
    cmd = "SELECT * FROM sessoes WHERE id = " + id_sessao
    sessao = bas.executa_comando(cmd)
    return sessao
