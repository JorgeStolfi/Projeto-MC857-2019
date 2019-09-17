# Este módulo define as tabelas da base de dados da loja e as 
# classes de objetos que representam linhas dessas tabelas na memória.

# Implementação desta interface:
import tabelas_IMP

# Os principais objetos:
import usuario; # from usuario import ObjUsuario
import sessao; # from sessao import ObjSessao
import produto; # from produto import ObjProduto
import compra; # from compra import ObjCompra

def inicializa_todas(limpa):
  """Inicializa as tabelas da base de dados para os objetos
  das classes {ObjUsuario}, {ObjProduto}, {ObjCompra}, e {ObjSessao},
  criando-as se necessário, e criando os caches 
  de objetos na memória.   Nao retorna nenhum resultado.
  
  Se parâmetro booleano {limpa} for {True}, também apaga todas as
  entradas das tabelas no disco e reinicializa os contadores de linhas
  para 0.
  
  Note que a classe {ObjCompra} tem duas tabelas: 'compras' e 
  'itens_de_compras'.
  
  Esta função deve ser chamada apenas uma vez em cada execução do
  servidor, depois de executar {basesql.conecta(...)}."""
  tabelas_IMP.inicializa_todas(limpa)

def obj_para_indice(obj, tipo):
  """Dado um objeto {obj} da classe {tipo}
  (que deve ser uma das princiais classes de objetos acima),
  devolve seu índice inteiro na tabela correspondente.
  Se o objeto for {None}, devolve {None}.""" 
  return tabelas_IMP.obj_para_indice(obj, tipo)
  
def indice_para_obj(indice, tipo):
  """Dado o {indice} inteiro de uma linha da tabela
  de objetos da classe {tipo} (que deve ser uma das 
  princiais classes de objetos acima), devolve o 
  objeto dessa classe com esse índice.  Se não existir
  tal linha, devolve {None}."""
  return tabelas_IMP.indice_para_obj(indice, tipo)
