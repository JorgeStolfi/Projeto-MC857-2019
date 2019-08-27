import sys
import base
import base_compras
import compra
import usuario

atrs= {
    'nome': 'Usuario Teste',
    'senha': 'senhasecreta',
    'email': 'teste@teste.com',
    'CPF': '15398765433',
    'endereco': 'Rua Ruazita da Cidade',
    'CEP': '21345-000',
    'telefone': '(19) 99283-0099'
}
bas = base.conecta
usr = usuario.cria(atrs)
compra = compra.cria(usr)
sys.stderr.write(base_compras.busca_por_indice(bas,1))
sys.stderr.write(base_compras.acrescenta(bas,compra))
sys.stderr.write(base_compras.atualiza(bas,1,compra))