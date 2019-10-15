
.PHONY: todos_os_testes teste_unico

# Módulos na ordem a testar:
MODULOS := \
  utils_testes \
  base_sql \
  identificador \
  tabela_generica \
  conversao_sql \
   \
  usuario \
  produto \
  sessao \
  itens_de_compras \
  compra \
   \
  tabelas \
   \
  gera_html_elem \
   \
  gera_html_botao \
  gera_html_form \
  gera_html_pag \
   \
  processa_comando_http \
   \
  comando_menu_cadastrar_usuario \
  comando_menu_entrar \
  comando_menu_sair \
  comando_menu_ver_carrinho \
  comando_submit_acrescentar_produto \
  comando_submit_buscar_produtos \
  comando_submit_cadastrar_usuario \
  comando_submit_comprar_produto \
  comando_submit_alterar_qt_de_produto \
  comando_submit_entrar \
  comando_submit_excluir_item_de_compra \
  comando_submit_finalizar_compra \
  comando_menu_ver_todas_as_compras \
  comando_submit_ver_compra \
  comando_submit_ver_produto

# O que "make" deve fazer:
all: todos_os_testes
# all: teste_unico
# all: roda_servidor

# Roda todos os módulos de teste:
todos_os_testes:
	for modulo in ${MODULOS} ; do \
	  { ./testa.sh $${modulo} ; echo "" ; } ; \
        done

# MODULO := identificador
# MODULO := conversao_sql
# MODULO := base_sql
# MODULO := tabela_generica
# MODULO := usuario
# MODULO := produto
# MODULO := sessao 
# MODULO := compra
# MODULO := gera_html_elem

teste_unico:
	./testa.sh ${MODULO}

roda_servidor:
	./cria_base_de_teste.py
	( ./servidor.py & sleep 1000 )
