
class Usuario_IMP:
    def _init_(self,atrs):
        self.nome = atrs.nome
        self.sobrenome = atrs.sobrenome
        self.nascDt = atrs.nascDt
        self.senha = atrs.senha
        self.email = atrs.email
        self.CPF = atrs.CPF
        self.endereco = atrs.endereco
        self.telefone = atrs.telefone
        
    def obtem_atributos(self):
        return self

def cria(atrs):
    """Cria um novo usuário com um novo identificador único e os
    atributos especificados pelo dicionário Python {atrs}."""
    usuario = Usuario_IMP(atrs)
    print("Bem vindo(a)" + usuario.nome + "a este e-commerce")
    return usuario

def muda_atributos(self,alts):
    """Recebe um dicionário Python {alts} cujas chaves são um subconjunto
    dos nomes de atributos do usuário, e troca os valores desses atributos 
    pels valores correspondentes em {alts}."""
    if alts.nome is not None:
        self.nome = alts.nome
    if alts.sobrenome is not None:
        self.sobrenome = alts.sobrenome
    if alts.nascDt is not None:
        self.nascDt = alts.nascDt
    if alts.senha is not None: 
        self.senha = alts.senha
    if alts.email is not None: 
        self.email = alts.email
    if alts.CPF is not None:
        self.CPF = alts.CPF
    if alts.endereco is not None:
        self.endereco = alts.endereco
    if alts.telefone is not None:
        self.telefone = alts.telefone

def obtem_atributos(self):
    """Retorna um dicionário Python com os atributos do usuário,
    exceto identificador."""
    return {self.nome, self.sobrenome, self.nascDt, self.email, self.CPF, self.endereco, self.telefone}

def obtem_identificador(self):
    """Devolve uma cadeia consistindo das letras 'U-' e 8 algarismos decimais,
    que identifica unicamente o usuário. Este identificador é 
    atribuído na criação do usuário e não pode ser alterado."""
    return self.login
