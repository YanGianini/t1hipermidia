class Estado():
    def __init__(self, nome, sigla, url_img):
        self.nome = nome
        self.sigla = sigla
        self.url_img = url_img
        self.noticias = []
    
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    
    def get_sigla(self):
        return self.sigla

    def set_sigla(self, sigla):
        self.sigla = sigla

    
    def get_url_img(self):
        return self.url_img

    def set_url_img(self, url):
        self.url_img = url


    def get_noticias(self):
        return self.noticias

    def set_noticias(self, noticia):
        self.noticias.append(noticia)
    