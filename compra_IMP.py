#! /usr/bin/python3

# Implementação do módulo {compra}.

# Interfaces importadas por esta interface:

# Implementações:

class Compra_IMP:
    def __init__(self, compra_id, itens):
        self.compra_id = compra_id
        self.itens = itens

    def lista_itens(self):
        return self.itens

    def calcula_total(self):
        total = 0
        for elem in compras:
            total += elem
        return total

    def acrescenta_item(self, prod, qt):
        self.compras[prod] = qt

    def troca_qtd(self, prod, qt):
        self.compras[prod] = qt

    def elimina_prod(self, prod):
        self.compras.pop(prod)

def cria(compra_id, car):
    itens = car.pega_itens()
    prod = Compra_IMP(compra_id, itens)

    return prod
