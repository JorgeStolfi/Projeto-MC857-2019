# Este módulo implementa a classe de objetos {Produto} que
# representa um produto do catálogo da loja virtual.

import inspect

class Produto_IMP():
    _id = None
    
    
    def obtem_id(self):
        """Devolve uma cadeia consistindo das letras 'P-' e 8 algarismos decimais,
        que identifica unicamente o produto. Este identificador é 
        atribuído na criação do produto e não pode ser alterado."""
        return self._id
    
    def obtem_atributos(self):
        """Retorna um dicionário Python com os atributos do produto,
        exceto o identificador."""
        atrs = dict((name, getattr(self, name)) for name in dir(self) if (not name.startswith('_') and not inspect.ismethod(getattr(self, name) ) ) ) 
        return atrs
        
    def muda_atributos(self,alts):
        """Recebe um dicionário Python {alts} cujas chaves são um subconjunto
        dos nomes de atributos do produto, e troca os valores desses atributos 
        pels valores correspondentes em {alts}."""
        for key in alts:
            if key in dir(self):
                setattr(self, key, alts[key])
    
    def cria(self,atrs):
        """Cria um novo produto com um novo identificador único e os
        atributos especificados pelo dicionário Python {atrs}."""
        for key in atrs:
            setattr(self, key, atrs[key])
            
        return self
