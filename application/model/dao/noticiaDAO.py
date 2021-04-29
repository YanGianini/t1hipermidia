from application.model.entity.noticia import Noticia
from application import noticia_list

class NoticiaDAO():
    def __init__(self):
        self.noticia_list = noticia_list

    def lista_noticia(self):
        return self.noticia_list

