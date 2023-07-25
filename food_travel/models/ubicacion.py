import uuid

class Ubicacion:

    def __init__(self, direccion, coordenadas):
        self.id = int(uuid.uuid4().int)
        self.direccion = direccion
        self.coordenadas = coordenadas


    def a_json(self):
        return {"id": self.id, "tipo":"Ubicacion", "direccion":self.direccion, "coordenadas":self.coordenadas}