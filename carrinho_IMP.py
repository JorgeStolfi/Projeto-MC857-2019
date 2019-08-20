""" import produto """
""" from produto import Produto """

class Carrinho_IMP:
    compras = dict()

    def cria(usr):
    """ Retorna instancia do carrinho onde usuario colocará produtos """
        instance = Carrinho_IMP()
        instance.usr = usr
        return instance

    def pega_itens(self):
    """ Retorna itens escolhidos pelo usuario """
        return compras.items()

    def calcula_total(self):
    """ Calcula valor dos itens escolhidos pelo usuario 
        no momento, aguardando a adicao do VALOR do produto
        para que o calculo seja correto """
        total = 0
        for elem in compras:
            total += elem
        return total

    def acrescenta_item(self, prod, qt):
    """ Acrescenta uma quantidade de produtos ao carrinho """
        self.compras[prod] = qt

    def troca_qtd(self, prod, qt):
    """ Muda a quantidade de produtos do carrinho """
        self.compras[prod] = qt

    def elimina_prod(self, prod):
    """ Elimina produto do carrinho """
        self.compras.pop(prod)
