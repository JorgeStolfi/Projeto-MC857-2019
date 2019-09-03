import tabela_de_usuarios
import identificador

class ObjUsuario_IMP:

  def _init_(self,atrs):
    self.id = None
    self.atrs = atrs.copy()

  def obtem_atributos(self):
    return self.atrs

  def muda_atributos(self, alts):
    # !!! Deveria verificar se 'CPF' está sendo alterado e reclamar. !!!
    
    # Verifica se novo email ja existe na base de usuarios:
    if 'email' in alts and self.atrs['email'] != alts['email']:
       res = tabela_de_usuarios.busca_por_email(alts['email'])
       if res != None and res.obtem_identificador() != self.obtem_identificador():
         # !!! Deveria devolver um string com mesnagem de erro ou algo assim !!!
         return 

    if "nome" in alts:
       self.alts["nome"] = alts["nome"]
    if "nascDt" in alts:
       self.alts["nascDt"] = alts["nascDt"]
    if "senha" in alts:
       self.alts["senha"] = alts["senha"]
    if "email" in alts:
       self.alts["email"] = alts["email"]
    if "endereco" in alts:
       self.alts["endereco"] = alts["endereco"]
    if "telefone" in alts:
       self.alts["telefone"] = alts["telefone"]
    
    # TODO Primeiro argumento Base_SQL ?
    # tabela_de_usuarios.atualiza(get_id(), self)
    # base de usuarios nao eh modificada

  def obtem_atributos(self):
    atrs = self.atrs.copy()

  def obtem_identificador(self):
    return self.alts["login"]

    # Metodo "privado" para set id
  def set_id(idt):
    self.id = idt;
    
  def get_id():
    return id

def cria(bas, atrs):
  for chave in ('CPF', 'email'):
    # Exige atributo {chave} único:
    if chave not in atrs:
      return "**erro: falta atributo '" + chave + "'"
    else:
      val = atrs[chave]
      if chave == 'CPF':
        ubus = tabela_de_usuarios.busca_por_CPF(bas,val)
      elif chave == 'email':
        ubus = tabela_de_usuarios.busca_por_email(bas,val)
      if ubus != None:
        return "**erro: atributo '" + chave + "' já existe"

  usr = ObjUsuario_IMP(atrs)
  uid = tabela_de_usuarios.acrescenta(bas,atrs)
  set_id(uid)

  return usr

