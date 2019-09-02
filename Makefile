
.PHONY: todos_os_testes

all: todos_os_testes

# Roda todos os módulos de teste:
todos_os_testes:
	for ff in `cd testes && ls *_TST.py` ; do \
	  module="$${ff%%_TST.py}" ; \
          { echo "=== $${module} ===" ; \
            ./testa.sh $${module} ; \
            echo "==============================" ; \
          } \
        done
