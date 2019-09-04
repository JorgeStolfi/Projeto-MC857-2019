# -*- coding: utf-8 -*-

# Implementação do módulo {gera_html_botao}.

#####Funções <button>#####
def botao_simples(texto, cor_fundo):
  tam_fonte = "18px"
  fam_fonte = "Courier"
  return \
    "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "  background-color:" + cor_fundo + ";\n" + \
    "  text-align: center;\n" + \
    "\">\n" + \
    "  <button\n" + \
    "    type=\"button\"\n" + \
    "    onclick=\"alert('" + texto + "')\"\n" + \
    "  >" + texto + "</button>\n" + \
    "</span>"

def login():
  texto = "Login"
  cor_fundo = "#fff888"
  return botao_simples(texto,cor_fundo)

def logout():
  texto = "Logout"
  cor_fundo = "#fff888"
  return botao_simples(texto,cor_fundo)

def cadastra():
  texto = "Cadastrar"
  cor_fundo = "#fff888"
  return botao_simples(texto,cor_fundo)

#####Funções <submit>#####
def botao_submit(texto, cor_fundo):
  return \
    "<span style=\"background-color:" + cor_fundo + ";text-align: center;\">\n" + \
    "  <input type=\"submit\" value=\"" + texto + "\">" + \
    "</span>"

def submit_compra():
  texto = "Comprar"
  cor_fundo = "#fff888"
  return botao_submit(texto, cor_fundo)

def submit_busca():
  texto = "Buscar"
  cor_fundo = "#fff888"
  return botao_submit(texto, cor_fundo)

def submit_cadastra():
  texto = "Cadastrar"
  cor_fundo = "#fff888"
  return botao_submit(texto, cor_fundo)

def submit_login():
  texto = "Entrar"
  cor_fundo = "#fff888"
  return botao_submit(texto, cor_fundo)

def submit_logout():
  texto = "Sair"
  cor_fundo = "#fff888"
  return botao_submit(texto, cor_fundo)

