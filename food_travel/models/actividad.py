import uuid

class Actividad:

    def __init__(self, nombre, destino_id, hora_inicio):
        self.id = int(uuid.uuid4().int)
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = hora_inicio

    def a_json(self):
        return {"id": self.id, "tipo":"Actividad", "nombre":self.nombre, "destino_id":self.destino_id, "hora_inicio":self.hora_inicio}