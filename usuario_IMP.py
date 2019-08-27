import base_usuarios

class Usuario_IMP:
    id = ""
    nome = ""
    senha = ""
    email = ""
    CPF = ""
    nascDt = ""
    endereco = ""
    telefone = ""

    def _init_(self,atrs):
        self.id = None
        self.nome = atrs[nome]
        self.senha = atrs[senha]
        self.email = atrs[email]
        self.nascDt = atrs[nascDt]
        self.CPF = atrs[CPF]
        self.endereco = atrs[endereco]
        self.telefone = atrs[telefone] 

    def obtem_atributos(self):
        return self

    def cria(self, atrs):
        
        cpf_atual = atrs[]
        email_atual = atrs[email]

        # CPF ou email ja existe na base de usuarios
        if ( base_usuarios.busca_por_CPF(cpf_atual) or \
            base_usuarios.busca_por_email(email_atual) )
            usr = None
        else
            copia_atrs = copy.deepcopy(atrs)
            usr = Usuario_IMP(copia_atrs)
            # TODO verificar primeiro argumento da chamada {bas}
            # id = base_usuarios.acrescenta(usr)
            # Supor que volta id = 42
            idt = 42
            set_id(idt)
            
        return usr

    def muda_atributos(self, alts):
        # CPF ou email ja existe na base de usuarios
        if ( base_usuarios.busca_por_CPF(cpf_atual) or \
            base_usuarios.busca_por_email(email_atual) )
            return

        if alts.nome is not None:
            self.nome = alts.nome
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
        
         copia_atrs = copy.deepcopy(atrs)
         # TODO Primeiro argumento Base ?
         # base_usuarios.atualiza(get_id(), self)
         # base de usuarios nao eh modificada

    def obtem_atributos(self):
        return {self.nome, self.nascDt, self.email, self.CPF, \ 
        self.endereco, self.telefone}

    def obtem_identificador(self):
        return self.login

    # Metodo "privado" para set id
    def set_id(idt):
        self.id = idt;
    
    def get_id():
        return id