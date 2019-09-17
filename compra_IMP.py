# Implementação do módulo {compra} e da classe {ObjCompra}.

# Interfaces importadas por esta interface:
import tabela_de_compras
import base_sql
import identificador
import sys

# Implementações:

class ObjCompra_IMP:
    def __init__(self, id_compra, itens, cliente):
        self.id_compra = id_compra
        self.itens = itens
        self.cliente = cliente
        self.status = 'aberto'

    ## TODO:
    def obtem_identificador(self):
        return self.id_compra

    def obtem_usuario(self):
         return self.cliente

    def obtem_status(self):
        return self.status

    def troca_status(self):
        if self.obtem_identificador == 'aberto':
          self.status = 'pagando'
        else: 
          if self.obtem_identificador == 'pagando':
            self.status = 'pago'
          else:
            if self.obtem_identificador == 'pago':
              self.status = 'despachado'
            else:
              self.obtem_identificador == 'despachado':
              self.status = 'entregue'

    def lista_itens(self):
        return self.itens

    def calcula_total(self):
        total = 0
        for prod, qt, prc in self.itens:
            total += prc
        return total

    def acrescenta_item(self, prod, qt):
        # Procura o produto na lista:
        for item in self.itens:
            if item[0] == prod:
                item[1] = qt
                item[2] = prod.calcula_preco(qt)
                sys.stderr.write("** produto " + str(prod) + " teve sua quantidade acrescentada em " + str(self.id_compra) + "\n")
                return

        # Caso nao exista, adiciona produto a compra:
        prc = prod.calcula_preco(qt)
        self.itens = self.itens + [ [ prod, qt, prc ] ]
        sys.stderr.write("** produto " + str(prod) + " foi acrescentado em " + str(self.id_compra) + "\n")

    def troca_qtd(self, prod, qt):
        # Procura o produto na lista:
        for item in self.itens:
          if item[0] == prod:
            item[1] = qt
            item[2] = prod.calcula_preco(qt)
            sys.stderr.write("** produto " + str(prod) + " na compra " + str(self.id_compra) + " teve sua quantidade trocada para " + str(qt) + "\n")
            return
        
        sys.stderr.write("** produto " + prod.obtem_identificador() + " nao encontrado em " + str(self.id_compra) + "\n")
        assert False

    def elimina_prod(self, prod):
        # !!! Deveria procurar o produto na lista de itens, e eliminar o item !!!
        for item in self.itens:
            if item[0] == prod:
                self.itens.remove(item)
                sys.stderr.write("** produto " + str(prod) + " eliminado de " + str(self.id_compra) + "\n")
                return
        
        sys.stderr.write("** produto " + prod.obtem_identificador() + " nao encontrado em " + str(self.id_compra) + "\n")
        assert False
    
    def fecha_compra(self):
      # Fecha uma dada compra, alterando seu status para pagando e salvando a 
      # alteração de status no banco
      self.troca_status
      id = self.obtem_identificador
      status = self.obtem_status
      atrs = {'status': status}
      Obj_Tabela_De_Compras_IMP.atualiza(self,id, atrs )
        

def cria(bas, usr):
    atrs = { 
      'id_usuario': usr.obtem_identificador(),
      'status': "aberto"
    }
    ind = tabela_de_compras.acrescenta(bas,atrs)
    id_compra = identificador.de_indice("C", ind)
    cpr = ObjCompra_IMP(id_compra,[],usr)
    return cpr
# ======================================================================
# Implementação do módulo {tabela_de_compras}.

import base_sql
import identificador
import sys # Para depuração.


class Obj_Tabela_De_Compras_IMP:
  
  def __init__(self,bas):
    # Base de dados:
    self.bas = bas
    # Nomes e tipos das colunas (menos 'indice'):
    self.colunas = (
      ('id_usuario', 'char(10) NOT NULL'),
      ('status', 'varchar(10) NOT NULL'),
    )
    campos = "indice integer NOT NULL PRIMARY KEY"
    for c in self.colunas:
      campos = campos + ", " + c[0] + " " + c[1]
    self.bas.executa_comando_CREATE_TABLE("compras", campos);

  def busca_por_identificador(self,compra_id):
    ind = identificador.para_indice("U", id_compra)
    cond = "indice = " + str(ind)
    col_nomes = ( c[0] for c in self.colunas )
    res = self.bas.executa_comando_SELECT("compras", cond, col_nomes)
    sys.stderr.write("res = " + str(res) + "\n")
    if res == None or len(res) == 0:
      return None
    else:
      assert len(res) == 1
      col_vals = res[0]
      assert len(col_vals) == len(col_nomes)
      atrs = dict(zip(col_nomes, col_vals))
      return atrs

    res = bas.executa_comando_SELECT("compras", 'indice', ind, ('id_usuario','status'))
    return res

  def acrescenta(self,atrs):
    ind = self.bas.executa_comando_INSERT("compras",atrs)
    return ind

  def atualiza(self, id_compra, atrs):
    ind = identificador.para_indice("C", id_compra)
    res = self.bas.executa_comando_UPDATE("produtos", ind, atrs)
    return


def cria_tabela(bas):
  return Obj_Tabela_De_Compras_IMP(bas)

# ======================================================================
# Implementação do módulo {tabela_de_itens_de_compras}.

import base_sql
import identificador
import sys # Para depuração.


class Obj_Tabela_De_Usuarios_IMP:
  
  def __init__(self,bas):
    # Base de dados:
    self.bas = bas
    # Nomes e tipos das colunas (menos 'indice'):
    self.colunas = (
      ('id_compra', 'char(10) NOT NULL'),
      ('id_produto', 'char(10) NOT NULL'),
      ('qt', 'float NOT NULL'),
      ('preco', 'float NOT NULL'),
    )
    campos = "indice integer NOT NULL PRIMARY KEY"
    for c in self.colunas:
      campos = campos + ", " + c[0] + " " + c[1]
    self.bas.executa_comando_CREATE_TABLE("itens_de_compras", campos);

  def acrescenta(self, atrs):
     ind = self.bas.executa_comando_INSERT("itens_de_compras", atrs)
     return   identificador.de_indice("I", ind)

  def busca_por_compra(self, id_compra):
     res = self.bas.executa_comando_SELECT("itens_de_compras", "id_compra = '" + id_compra + "'", ('id_produto','qt','preco'))
     return cpr

  def busca_por_produto(self, id_produto):
     res = self.bas.executa_comando_SELECT("itens_de_compras", "id_produto = '" + id_produto + "'", ('id_compra','qt','preco'))
     return cpr

  def atualiza(self, id_item, atrs):
     res = self.bas.executa_comando_UPDATE("itens_de_compras", "indice = " + str(ind), atrs);
     return

def cria_tabela(bas):
  return Obj_Tabela_De_Usuarios_IMP(bas)
