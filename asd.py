class DestinoCulinario:
    destinos = []

    def __init__(self, id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo,
                 popularidad, disponibilidad, id_ubicacion, imagen):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad 
        self.disponibilidad = disponibilidad 
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen

    @classmethod
    def crear_destinos_culinarios(cls):
        print("Ingrese los datos del nuevo destino:")
        nombre = input("Nombre: ")
        tipo_cocina = input("Tipo de cocina: ")
        ingredientes = input("Ingredientes (separados por comas): ").split(",")
        precio_minimo = float(input("Precio mínimo: "))
        precio_maximo = float(input("Precio máximo: "))
        popularidad = float(input("Índice de popularidad: ")) #Debería depender de las reviews
        disponibilidad = bool(input("Disponibilidad (True o False): ")) #Marcar una franja horaria y que un booleano marque la disponibilidad o no
        id_ubicacion = int(input("ID de ubicación: "))
        imagen = input("URL de la imagen: ")
        print()

        id = len(cls.destinos) + 1 
        ubicacion_encontrada = None
        for ubicacion in Ubicacion.ubicaciones:
            if ubicacion.id == id_ubicacion:
                ubicacion_encontrada = ubicacion
                break

        if ubicacion_encontrada is None:
            print("Error: La ubicación con ID {} no fue encontrada.".format(id_ubicacion))
            return

        destino = DestinoCulinario(id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo,
                               popularidad, disponibilidad, id_ubicacion, imagen)

        cls.destinos.append(destino)

    @classmethod
    def leer_destinos_culinarios(cls):
        print("Lista de destinos culinarios:")
        for destino in cls.destinos:
            print("ID:", destino.id)
            print("Nombre:", destino.nombre)
            print("Tipo de cocina:", destino.tipo_cocina)
            print("Ingredientes:", destino.ingredientes)
            print("Precio mínimo:", destino.precio_minimo)
            print("Precio máximo:", destino.precio_maximo)
            print("Popularidad:", destino.popularidad)
            print("Disponibilidad:", destino.disponibilidad)
            print("ID de ubicación:", destino.id_ubicacion)
            print("Imagen:", destino.imagen)
            print()


class Actividad:
    actividades = []

    def __init__(self, id, nombre, destino_id, hora_inicio):
        self.id = id
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = hora_inicio

    @classmethod
    def crear_actividades(cls):
        nombre = input("Nombre de la actividad: ")
        destino_id = int(input("ID del destino culinario asociado: "))
        hora_inicio = input("Hora de inicio: ")
        print()

        id_actividad = len(cls.actividades) + 1 
        destino_encontrado = None
        for destino in DestinoCulinario.destinos:
            if destino.id == destino_id:
                destino_encontrado = destino
                break

        if destino_encontrado is None:
            print("Error: El destino culinario con ID {} no fue encontrado.".format(destino_id))
            return
        actividad = Actividad(id_actividad, nombre, destino_encontrado, hora_inicio)

        cls.actividades.append(actividad)

    @classmethod
    def leer_actividades(cls):
        print("Lista de actividades:")
        for actividad in cls.actividades:
            print("ID:", actividad.id)
            print("Nombre de la actividad:", actividad.nombre)
            print("ID del destino culinario asociado:", actividad.destino_id)
            print("Hora de inicio:", actividad.hora_inicio)
            print()


class RutaVisitada:
    rutas = []
    def __init__(self, id, nombre, destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos #Averiguar como agregar varias

    @classmethod
    def crear_ruta_visitada(cls):
        print("Ingrese los datos de la ruta de visita:")
        nombre = input("Nombre de la ruta de visita: ")
        destinos = [int(id_destino) for id_destino in input("ID de los destinos (separados por comas): ").split(",")]
        id_ruta = len(cls.rutas) + 1
        ruta_visitada = RutaVisitada(id_ruta, nombre, destinos)

        for destino_id in destinos:
            destino_encontrado = None
            for destino in DestinoCulinario.destinos:
                if destino.id == destino_id:
                    destino_encontrado = destino
                    break

            if destino_encontrado is None:
                print("Error: El destino culinario con ID {} no fue encontrado.".format(destino_id))
                return


        cls.rutas.append(ruta_visitada)

    @classmethod
    def leer_rutas_visitada(cls):
        print("Lista de rutas de visita:")
        for ruta_visitada in cls.rutas:
            print("ID:", ruta_visitada.id)
            print("Nombre de la ruta de visita:", ruta_visitada.nombre)
            print("Destinos:", ruta_visitada.destinos)
            print()


class Ubicacion:
    ubicaciones = []

    def __init__(self, id, direccion, coordenadas):
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas

    @classmethod
    def crear_ubicacion(cls):
        print("Ingrese los datos de la ubicación:")
        direccion = input("Dirección: ")
        coordenadas = input("Coordenadas: ")
        print()

        id_ubicacion = len(cls.ubicaciones) + 1
        ubicacion = Ubicacion(id_ubicacion, direccion, coordenadas)

        cls.ubicaciones.append(ubicacion)

    @classmethod
    def leer_ubicaciones(cls):
        print("Lista de ubicaciones:")
        for ubicacion in cls.ubicaciones:
            print("ID:", ubicacion.id)
            print("Dirección:", ubicacion.direccion)
            print("Coordenadas:", ubicacion.coordenadas)
            print()


class Usuario: 
    """¿Los usuarios son quienes crean las reviews y las rutas?"""
    usuarios = []
    def __init__(self, id, nombre, apellido, historial_rutas):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas
        self.reviews = []

    @classmethod
    def crear_usuario(cls):
        print("Ingrese los datos del usuario:")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        historial_rutas = input("Historial de rutas (separadas por comas): ")
        print()

        id_usuario = len(cls.usuarios) + 1
        usuario = Usuario(id_usuario, nombre, apellido, historial_rutas)

        cls.usuarios.append(usuario)

    @classmethod
    def leer_usuarios(cls):
        print("Lista de usuarios:")
        for usuario in cls.usuarios:
            print("ID:", usuario.id)
            print("Nombre:", usuario.nombre)
            print("Apellido:", usuario.apellido)
            print("Historial de rutas:", usuario.historial_rutas)
            print()

    def buscar_ruta_visita(cls, ruta_id):
        for ruta_visita in RutaVisitada.rutas_visita:
            if ruta_visita.id == ruta_id:
                return ruta_visita
        return None

    def agregar_ruta_visita(self, ruta_id):
        ruta_visita = Usuario.buscar_ruta_visita(ruta_id)

        if ruta_visita is None:
            print("Error: La ruta de visita con ID {} no fue encontrada.".format(ruta_id))
            return

        self.historial_rutas.append(ruta_visita)
   
class Review:
    reviews = []
    def __init__(self, id, id_destino, id_usuario, calificacion, comentario, animo):
        self.id = id
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    @classmethod
    def crear_review(cls):
        print("Ingrese los datos de la nueva review:")
        id_destino = input("ID del destino culinario que se está calificando: ")
        id_usuario = input("ID del usuario que escribió la review: ")
        calificacion = float(input("Calificación del destino culinario (de 1 a 5): "))
        comentario = input("Comentario sobre el destino culinario: ")
        animo = input("Ánimo del comentario (Positivo o Negativo): ") #Hacer un booleano que tenga un pulgar arriba y otro hacia abajo
        print()

        destino_encontrado = None
        for destino in DestinoCulinario.destinos:
            if destino.id == id_destino:
                destino_encontrado = destino
                break

        if destino_encontrado is None:
            print("Error: El destino culinario con ID {} no fue encontrado.".format(id_destino))
            return

        usuario_encontrado = None
        for usuario in Usuario.usuarios:
            if usuario.id == id_usuario:
                usuario_encontrado = usuario
                break

        if usuario_encontrado is None:
            print("Error: El usuario con ID {} no fue encontrado.".format(id_usuario))
            return
        
        review = Review(destino_encontrado, usuario_encontrado, calificacion, comentario, animo)

        cls.reviews.append(review)
        

Ubicacion.crear_ubicacion()
Ubicacion.crear_ubicacion()
DestinoCulinario.crear_destinos_culinarios()
DestinoCulinario.crear_destinos_culinarios()
RutaVisitada.crear_ruta_visitada()
RutaVisitada.crear_ruta_visitada()