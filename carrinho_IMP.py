class Carrinho_IMP:
    def __init__(self, marca, nome, ano, preco, descricao):
        self.marca = marca
        self.nome = nome
        self.ano = ano
        self.preco = preco
        self.descricao = descricao
        
    def muda_marca(self,marca):
        self.marca = marca
    
    def muda_nome(self,nome):
        self.nome = nome
    
    def muda_ano(self,ano):
        self.ano = ano
    
    def muda_preco(self,preco):
        self.preco = preco
    
    def muda_descricao(self,descricao):
        self.descricao = descricao
    
