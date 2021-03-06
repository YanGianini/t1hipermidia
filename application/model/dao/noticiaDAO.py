from application.model.entity.noticia import Noticia
from application import noticia_list

class NoticiaDAO():
    def __init__(self):
        self.noticia_list = noticia_list

    def lista_noticias(self):
        return self.noticia_list

    def filtrar_id(self, id):
        for noticia in noticia_list:
            if str(noticia.id) == id:
                return noticia