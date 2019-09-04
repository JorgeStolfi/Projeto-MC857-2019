
.PHONY: todos_os_testes

# all: todos_os_testes
all: teste_unico

# Roda todos os módulos de teste:
todos_os_testes:
	for ff in `cd testes && ls *_TST.py` ; do \
	  modulo="$${ff%%_TST.py}" ; \
          { echo "=== $${modulo} ===" ; \
            ./testa.sh $${modulo} ; \
            echo "==============================" ; \
          } \
        done

MODULO := base_sql
teste_unico:
	@echo "=== ${MODULO} ==="
	./testa.sh ${MODULO}
	@echo "=============================="
