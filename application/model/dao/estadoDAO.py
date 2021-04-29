from application.model.entity.estado import Estado
from application import estado_list

class EstadoDAO():
    def __init__(self):
        self.estado_list = estado_list

    def lista_estados(self):
        return self.estado_list


