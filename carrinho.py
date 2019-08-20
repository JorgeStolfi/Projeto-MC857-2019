from carrinho_IMP import *

class Carrinho(Carrinho_IMP):

    def pega_itens():
        """retorna uma tupla de itens e sua quantidade"""
        super().pega_itens()

    def calcula_total():
        """retorna o preco total do carrinho"""
        super().calcula_total()

    def acrescenta_item(self, prod, qt):
        """acrescenta um novo item no carrinho"""
        super().acrescenta_item(self, prod, qt)

    def troca_qtd( self, prod, qt):
        """modifica a quantidade de um item"""
        super().troca_qtd(self, prod, qt)

    def elimina_prod(self, prod):
        """elimina um produto do carrinho"""
        super().elimina_prod(self, prod)

    def cria(usr):
        """cria uma nova instância com um usuário"""
        instance = Carrinho()
        instance.usr = usr
        return instance
