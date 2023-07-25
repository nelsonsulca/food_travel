import uuid

class RutaVisitada:
    
    def __init__(self, nombre, destinos):
        self.id = int(uuid.uuid4().int)
        self.nombre = nombre
        self.destinos = destinos #Averiguar como agregar varias

    def a_json(self):
        return {"id": self.id, "tipo":"RutaVisitada", "nombre":self.nombre, "destinos":self.destinos}