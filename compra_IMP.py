#! /usr/bin/python3

# Implementação do módulo {compra}.

# Interfaces importadas por esta interface:

# Implementações:

class Compra_IMP:
    def __init__(self, compra_id, items, cliente):
        self.compra_id = compra_id
        self.items = items
        self.cliente = cliente
        self.status = 'aberto'

    ## TODO:
    def obtem_identificador(self):
        return ''.join(random.choices(string.digits, k=8))

    def obtem_usuario(self):
        """ Esta função retorna o cliente do pedido de compra
        (um objeto da classe {Usuario})."""
        return self.cliente

    def obtem_status(self):
        """ Essa função retorna o status do pedido de compra, um string que, por enquanto, pode ser:
          1) 'aberto': O cliente ainda está montando o pedido.
          2) 'pagando':  O cliente fechou o pedido, e a loja está aguardando o pagamento.
          3) 'pago': A loja já recebeu o pagamento e mandou para despacho.
          4) 'despachado': A loja já colocou o pedido no correio ou transportadora.
          5) 'entregue': O pedido foi entregue ao cliente.
        Outros estados podem ser acrescentados no futuro."""
        return self.status

    def lista_itens(self):
        return self.items

    def calcula_total(self):
        total = 0
        for _ , preco in self.items.items:
            total += preco
        return total

    def acrescenta_item(self, prod, qt):
        self.items[prod] = qt

    def troca_qtd(self, prod, qt):
        self.items[prod] = qt

    def elimina_prod(self, prod):
        self.items.pop(prod)

    def cria(self, usr):
        return Compra_IMP(self.obtem_identificador, {}, usr)
