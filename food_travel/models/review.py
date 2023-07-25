import uuid

class Review:
    
    def __init__(self, id_destino, id_usuario, calificacion, comentario, animo):
        self.id = int(uuid.uuid4().int)
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def a_json(self):
        return {"id": self.id, "tipo":"Review", "id_destino":self.id_destino, "id_usuario":self.id_usuario, "calificacion":self.calificacion, "comentario":self.comentario, "animo":self.animo}