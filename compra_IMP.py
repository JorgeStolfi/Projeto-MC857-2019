# Implementação do módulo {compra}.

# Interfaces importadas por esta interface:
import tabela_de_compras
import base_sql
import identificador

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

    def lista_itens(self):
        return self.itens

    def calcula_total(self):
        total = 0
        for prod, qt, prc in self.itens:
            total += prc
        return total

    def acrescenta_item(self, prod, qt):
        # !!! Deveria procurar se já existe {prod} !!!
        prc = prod.calcula_preco(qt)
        self.itens = self.itens + [ [ prod, qt, prc ] ]

    def troca_qtd(self, prod, qt):
        # Procura o produto na lista:
        for item in self.itens:
          if item[0] == prod:
            item[1] = qt
            item[2] = prod.calcula_preco(qt)
            return
        sys.stderr.write("** produto " + prod.obtem_identificador() + " nao encontrado em " + self.id_compra + "\n")
        assert False

    def elimina_prod(self, prod):
        # !!! Deveria procurar o produto na lista de itens, e eliminar o item !!!
        return

def cria(bas, usr):
    cpr = ObjCompra_IMP(None,[],usr)
    idc = tabela_de_compras.acrescenta(bas,cpr)
    cpr.id_compra = idc
    return cpr
