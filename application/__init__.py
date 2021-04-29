from flask import Flask
import os
from application.model.entity.estado import Estado
from application.model.entity.noticia import Noticia


app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))


estado1 = Estado("Rio de Janeiro", "RJ", "url rio")
estado2 = Estado("São Paulo", "SP", "url sp")
estado3 = Estado("Minas Gerais", "MG", "url mg")
estado4 = Estado("Espirito Santo", "ES", "url es")

estado_list = [estado1, estado2, estado3, estado4]

noticia1 = Noticia(1, "url 1", "url img 1", "titulo 1", "texto 1", "12/03/2021")
noticia2 = Noticia(2, "url 2", "url img 2", "titulo 2", "texto 2", "12/03/2021")
noticia3 = Noticia(3, "url 3", "url img 3", "titulo 3", "texto 3", "12/03/2021")
noticia4 = Noticia(4, "url 4", "url img 4", "titulo 4", "texto 4", "12/03/2021")

noticia_list = [noticia1, noticia2, noticia3, noticia4]

estado1.set_noticias(noticia1)
estado2.set_noticias(noticia2)
estado3.set_noticias(noticia3)
estado4.set_noticias(noticia4)


from application.controller import index_controller