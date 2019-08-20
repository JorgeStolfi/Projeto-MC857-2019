# Last edited on 2019-08-19 23:47:00 by stolfilocal

all:
	chmod a+x testa_html.py
	mkdir -p out
	./testa_html.py > out/teste.html
	pluma --encoding=utf-8 out/teste.html
