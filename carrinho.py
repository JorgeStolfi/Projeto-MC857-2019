import carrinho_IMP
from carrinho_IMP import Carrinho_IMP

def cria(usr):
    """Cria uma nova instância com um usuário"""
    Carrinho_IMP.cria(usr)

class Carrinho(Carrinho_IMP):
    def pega_itens(self):
        """Retorna os itens e sua quantidade"""
        return super().pega_itens(self)

    def calcula_total(self):
        """Retorna o preco total do carrinho"""
        return super().calcula_total(self)

    def acrescenta_item(self, prod, qt):
        """
            Acrescenta um novo item no carrinho

            Parametros
            -----------
            prod : Produto
                Objeto produto que será acrescentado no carrinho
            
            qt : int
                Quantidade de itens que serão comprados do produto
        """
        super().acrescenta_item(self, prod, qt)

    def troca_qtd(self, prod, qt):
        """
            Modifica a quantidade de um item
            
            Parametros
            -----------
            prod : Produto
                Objeto produto que terá sua quantidade trocada
            
            qt : int
                Nova quantidade do produto
        """
        super().troca_qtd(self, prod, qt)

    def elimina_prod(self, prod):
        """
            Remove um produto do carrinho
            
            Parametro
            -----------
            prod : Produto
                Objeto produto que será removido do carrinho
        """
        super().elimina_prod(self, prod)
