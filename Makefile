
.PHONY: todos_os_testes teste_unico

# Módulos na ordem a testar:
MODULOS := \
  base_sql \
  identificador \
   \
  tabela_de_usuarios \
  tabela_de_produtos \
  tabela_de_sessoes \
  tabela_de_compras \
  tabela_de_itens_de_compras \
   \
  usuario \
  produto \
  sessao \
  compra \
   \
  gera_html_elem \
   \
  gera_html_botao \
  gera_html_form \
  gera_html_pag \
   \
  processa_comando_http \
   \
  comando_botao_cadastrar \
  comando_botao_entrar \
  comando_botao_sair \
  comando_subm_buscar_produtos \
  comando_subm_cadastrar \
  comando_subm_comprar_produto \
  comando_subm_ver_produto \
   \
  servidor \


# O que "make" deve fazer:
# all: todos_os_testes
all: teste_unico

# Roda todos os módulos de teste:
todos_os_testes:
	for modulo in ${MODULOS} ; do \
	  { echo "=== $${modulo} ===" ; \
            ./testa.sh $${modulo} ; \
            echo "==============================" ; \
          } ; \
        done

# MODULO := identificador
# MODULO := conversao_sql
# MODULO := base_sql
# MODULO := tabela_generica
MODULO := usuario
# MODULO := sessao 
teste_unico:
	@echo "=== ${MODULO} ==="
	./testa.sh ${MODULO}
	@echo "=============================="
