class Noticia():
    def __init__(self, id, url_video, url_img, titulo, texto, data):
        self.id = id
        self.url_video = url_video
        self.url_img = url_img
        self.titulo = titulo
        self.texto = texto
        self.data = data


    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id


    def get_url_video(self):
        return self.url_video
    
    def set_url_video(self, url_video):
        self.url_video = url_video


    def get_url_img(self):
        return self.url_img
    
    def set_url_img(self, url_img):
        self.url_img = url_img


    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    
    def get_texto(self):
        return self.texto

    def set_texto(self, texto):
        self.text = texto


    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

