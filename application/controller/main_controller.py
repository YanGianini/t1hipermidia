from application import app
from flask import render_template, redirect, request, url_for
from application.model.dao.estadoDAO import EstadoDAO
from application.model.dao.noticiaDAO import NoticiaDAO

@app.route("/")
def index():
    estadoDAO = EstadoDAO()
    lista_estados = estadoDAO.lista_estados()
    return render_template("index.html", lista_estados=lista_estados)


@app.route("/noticias")
def videos():
    return render_template("noticia.html")
