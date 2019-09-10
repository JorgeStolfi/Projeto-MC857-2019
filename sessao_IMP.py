# Imprementação do módulo {sessao} e da classe {ObjSessao}.

import base_sql
import tabela_de_sessoes
import identificador

class ObjSessao_IMP:
    def __init__(self):
        self.id_sessao = None
        self.usr = None

    def obtem_identificador(self):
        return self.id_sessao

    def aberta(self):
        return self.usr is not None

    def obtem_usuario(self):
        return self.usr

    def logout(self, bas):
        self.usr = None
        tabela_de_sessoes.atualiza(bas, self.id_sessao, self)
        

def cria(bas,usr):
    ses = ObjSessao_IMP()
    ids = tabela_de_sessoes.acrescenta(bas,ses)
    ses.usr = usr
    ses.id_sessao = ids
    return ses
# ======================================================================
# Implementação do módulo {tabela_de_sessoes}.

import base_sql
import identificador
import sys # Para depuração.

class Obj_Tabela_De_Sessoes_IMP:
  
  def __init__(self,bas):
    # Base de dados:
    self.bas = bas
    # Nomes e tipos das colunas (menos 'indice'):
    self.colunas = (
      ('id_usuario', 'char(10)'),
      ('aberta', 'boolean')
    )
    campos = "indice integer NOT NULL PRIMARY KEY"
    for c in self.colunas:
      campos = campos + ", " + c[0] + " " + c[1]
    self.bas.executa_comando_CREATE_TABLE("sessoes", campos);

  def acrescenta(self,ses):
    ind = self.bas.executa_comando_INSERT("sessoes", atrs)
    return id_sessao

  def atualiza(self,ind,ses):
    usr = ses.obtem_usuario()
    uid = (usr.obtem_identificador() if usr != None else None)
    pares = \
      "usr=" + str(uid) + ", " + \
      "sessao_aberta=" + str(ses.aberta())
    cmd = "UPDATE sessoes SET " + pares +  " WHERE id=" + str(ind)
    self.bas.executa_comando_UPDATE("sessoes", )

  def busca_por_identificador(self, id_sessao):
    cmd = "SELECT * FROM sessoes WHERE id = " + id_sessao
    sessao = self.bas.executa_comando_SELECT("sessoes", )
    return sessao

def cria_tabela(bas):
  return Obj_Tabela_De_Sessoes_IMP(bas)


