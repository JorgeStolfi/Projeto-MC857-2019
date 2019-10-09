#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import gera_html_form
import sys
import usuario
import identificador

# !!! Precisa chamar todas as funções da interface, pelo menos uma vez, e gravar em arquivos ".html" separados. !!!

# Comandos:
class ObjCompra_IMP:
  def __init__(self, id_compra, atrs, itens):
    global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
    self.id_compra = id_compra
    self.atrs = atrs # Inclui cliente e status
    self.itens = itens.copy()

cpr = ObjCompra_IMP("123", ["Cliente"], ["Computador"])

html = gera_html_form.buscar_produtos()

html = html + "<br/>" + gera_html_form.ver_produto("1234", 3)

html = html + "<br/>" + gera_html_form.comprar_produto("1234", 3)

html = html + "<br/>" + gera_html_form.cadastrar_usuario()

html = html + "<br/>" + gera_html_form.mostra_compra(cpr)

html = html + "<br/>" + gera_html_form.entrar()

html = html + "\n" # In case the fragment does not end with newline.

sys.stdout.buffer.write(html.encode('utf-8'))
