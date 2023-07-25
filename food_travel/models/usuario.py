import uuid

class Usuario: 
    """¿Los usuarios son quienes crean las reviews y las rutas?"""

    def __init__(self, nombre, apellido, historial_rutas):
        self.id = int(uuid.uuid4().int)
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas
        # self.reviews = []

    def a_json(self):
        return {"id": self.id, "tipo":"Usuario", "nombre":self.nombre, "apellido":self.apellido, "historial_rutas":self.historial_rutas}