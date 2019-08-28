import base

def busca_por_indice(bas,ind):
    query = "SELECT * FROM sessao WHERE id=" +ind
    sessao = bas.executa_comando(query)
    return sessao

def acrescenta(sbas,es):
    query = "INSERT INTO sessao (usr, sessao_aberta) VALUES (" + str(es.obtem_usuario().obtem_identificador()) + ", " + str(es.sessao_aberta) + ")"
    sbas.executa_comando(query)
    return sbas.indice_inserido()

def atualiza(bas,ind,ses):
    query = "UPDATE sessao SET usr=" + str(ses.otem_usuario().obtem_identificador()) + ", sessao_aberta=" + str(ses.sessao_aberta) + "WHERE id=" + str(ind)
    bas.executa_comando(query)