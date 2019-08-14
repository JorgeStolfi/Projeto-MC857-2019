from carrinho_IMP import *

class Carrinho():
    def __init__(self, marca, nome, ano, preco, descricao):
        #Inicializa a classe carrinho
        self.__carrinho = Carrinho_IMP(marca, nome, ano, preco, descricao)
    
    def marca(self):
        #retorna a marca
        return self.__carrinho.marca
    
    def nome(self):
        #retorna o nome
        return self.__carrinho.nome
    
    def ano(self):
        #retorna o ano
        return self.__carrinho.ano
    
    def preco(self):
        #retorna o preco
        return self.__carrinho.preco
    
    def descricao(self):
        #retorna a descricao
        return self.__carrinho.descricao

    def muda_marca(self,marca):
        #muda a marca do carro
        self.__carrinho.muda_marca(marca)
    
    def muda_nome(self,nome):
        #muda o nome
        self.__carrinho.muda_nome(nome)
    
    def muda_ano(self,ano):
        #muda o ano
        self.__carrinho.muda_ano(ano)
    
    def muda_preco(self,preco):
        #muda o preco
        self.__carrinho.muda_preco(preco)
    
    def muda_descricao(self,descricao):
        #muda a descricao
        self.__carrinho.muda_descricao(descricao)
