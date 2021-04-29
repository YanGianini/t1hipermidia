from application import app
from flask import render_template, redirect, request, url_for
from application.model.dao.estadoDAO import EstadoDAO
from application.model.dao.noticiaDAO import NoticiaDAO

@app.route("/")
def index():
    estadoDAO = EstadoDAO()
    lista_estados = estadoDAO.lista_estados()
    noticiaDao = NoticiaDAO()
    lista_noticias = noticiaDao.lista_noticias()

    return render_template("index.html", lista_estados=lista_estados, lista_noticias=lista_noticias)


@app.route("/noticias/<id>")
def noticias(id):
    noticias = NoticiaDAO()
    noticia = noticias.filtrar_id(id)
    return render_template("noticia.html", noticia=noticia)
