import base_sql

def cria_tabela(bas):
    campos = \
      "indice integer PRIMARY KEY," + \
      "id_usuario char(10)," + \
      "aberta boolean"
    sessao = bas.executa_comando_CRIA_TABELA("sessoes",campos)
    return sessao

def acrescenta(bas,ses):
    ind = bas.executa_comando_INSERT("sessoes", atrs)
    return id_sessao

def atualiza(bas,ind,ses):
    usr = ses.obtem_usuario()
    uid = (usr.obtem_identificador() if usr != None else None)
    pares = \
      "usr=" + str(uid) + ", " + \
      "sessao_aberta=" + str(ses.aberta())
    cmd = "UPDATE sessoes SET " + pares +  " WHERE id=" + str(ind)
    bas.executa_comando_UPDATE("sessoes", )

def busca_por_identificador(bas, id_sessao):
    cmd = "SELECT * FROM sessoes WHERE id = " + id_sessao
    sessao = bas.executa_comando_SELECT("sessoes", )
    return sessao
