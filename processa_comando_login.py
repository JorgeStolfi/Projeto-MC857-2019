#!/usr/bin/python3

#Pedro Henrique Barcha Correia (PedroBarcha)
#158338
#Última Atualização: 20/08

#Funções que efetuam o login do usuário 

### IMPORTANTE ###
#Conforme conversado não participarei das aulas dos dias 20 e 27, devido à intervenção cirúrgica, portanto fiz algumas suposições no código
##################

#Implementação desta interface:
#(Comentada pois é inexistente ainda)
#import processa_comando_login_IMP

def conecta():
  """Abre conexao com a base de dados e retorna o objeto {MySQL} conexao_mysql. Essa função é chama no início da função login"""
  return processa_comando_login_IMP.conecta()

def desconecta(conexao_mysql):
  """Fecha a conexao {MySQL} conexao_mysql com a base de dados. Essa função é chama no fim da função login"""
  return processa_comando_login_IMP.desconecta(conexao_mysql)

def login(usuario, senha):
  """Conecta-se à base de dados, confere se as credenciais estão corretas e, caso estejam, conecta o usuário ao sistema. Ao fim, desconecta-se da base de dados"""
  return processa_comando_login_IMP.login(usuario, senha)