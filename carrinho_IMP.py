#from produto import Produto

class Carrinho_IMP:
    compras = dict()

    def pega_itens():
        return compras.items()

    def calcula_total():
        return

    def acrescenta_item(self, prod, qt):
        self.compras[prod] = qt

    def troca_qtd( self, prod, qt):
        self.compras[prod] = qt

    def elimina_prod(self, prod):
        self.compras.pop(prod)
