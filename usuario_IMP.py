
class Usuario_IMP:
    def _init_(self,atrs):
        self.nome = atrs.nome
        self.sobrenome = atrs.sobrenome
        self.nascDt = atrs.nascDt
        self.senha = atrs.senha
        self.email = atrs.email
        self.cpf = atrs.cpf
        self.endereco = atrs.endereco
        self.telefone = atrs.telefone

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
    if alts.cpf is not None:
        self.cpf = alts.cpf
    if alts.endereco is not None:
        self.endereco = alts.endereco
    if alts.telefone is not None:
        self.telefone = alts.telefone

def obtem_atributos(self):
        """Retorna um dicionário Python com os atributos do usuário,
        exceto identificador."""

def obtem_id(self):
        """Devolve uma cadeia consistindo das letras 'U-' e 8 algarismos decimais,
        que identifica unicamente o usuário. Este identificador é 
        atribuído na criação do usuário e não pode ser alterado."""
