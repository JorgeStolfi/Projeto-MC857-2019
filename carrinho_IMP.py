# import produto
# from produto import Produto

class Carrinho_IMP:
    compras = dict()

    def cria(usr):
        instance = Carrinho_IMP()
        instance.usr = usr
        return instance

    def pega_itens(self):
        return compras.items()

    def calcula_total(self):
        return

    def acrescenta_item(self, prod, qt):
        self.compras[prod] = qt

    def troca_qtd( self, prod, qt):
        self.compras[prod] = qt

    def elimina_prod(self, prod):
        self.compras.pop(prod)
