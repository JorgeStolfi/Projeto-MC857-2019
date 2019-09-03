#testes para gera_html_elem
import sys
sys.path.append('/home/cc2016/ra173711/mc857/data/173711')
import gera_html_elem

#teste para cabecalho
teste_cabecalho = gera_html_elem.cabecalho("TESTE")
f = open('teste_cabecalho.html', 'w')
f.write(teste_cabecalho)
f.close()

#teste para rodape
teste_rodape = gera_html_elem.rodape()
f = open('teste_rodape.html', 'w')
f.write(teste_rodape)
f.close()

#teste para menu_geral
teste_menu_geral = gera_html_elem.menu_geral()
f = open('teste_menu_geral.html', 'w')
f.write(teste_menu_geral)
f.close()

#teste para bloco_texto
teste_bloco_texto = gera_html_elem.bloco_texto("Hello World","Helvetica","18px","30px","center","#000000","#ff8800")
f = open('teste_bloco_texto.html', 'w')
f.write(teste_bloco_texto)
f.close()

#teste para bloco_de_produto
teste_bloco_de_produto = gera_html_elem.bloco_de_produto("nada")
f = open('teste_bloco_de_produto.html', 'w')
f.write(teste_bloco_de_produto)
f.close()

#teste para formulario_login
teste_formulario_login = gera_html_elem.formulario_login("800px","600px","solid","30px","35px")
f = open('teste_formulario_login.html', 'w')
f.write(teste_formulario_login)
f.close()