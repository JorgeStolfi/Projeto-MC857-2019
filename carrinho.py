import carrinho_IMP


def cria(usr):
    """Cria uma nova instância com um usuário"""
    Carrinho_IMP.cria(usr)

class Carrinho(Carrinho_IMP):
    def pega_itens(self):
        """ Escolhe um item e o coloca no carrinho """
        return carrinho_IMP.pega_itens(self)

    def calcula_total(self):
        """ Retorna o preco total do carrinho"""
        return carrinho_IMP.calcula_total(self)

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
        return carrinho_IMP.acrescenta_item(self, prod, qt)

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
        return carrinho_IMP.troca_qtd(self, prod, qt)

    def elimina_prod(self, prod):
        """
            Remove um produto do carrinho
            
            Parametro
            -----------
            prod : Produto
                Objeto produto que será removido do carrinho
        """
        return carrinho_IMP.elimina_prod(self, prod)
