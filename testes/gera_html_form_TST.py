#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import gera_html_form
import sys

# !!! Precisa chamar todas as funções da interface, pelo menos uma vez, e gravar em arquivos ".html" separados. !!!

# Comandos:

html = gera_html_form.buscar_produtos()

html = html + "\n" # In case the fragment does not end with newline.

sys.stdout.buffer.write(html.encode('utf-8'))
