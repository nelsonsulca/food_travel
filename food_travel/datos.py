import json

# Archivo de Destino Culinario
def guardar_datos_destinoCulinario(lista_destinos):
    with open('data/destino_culinario.json','w') as f:  
        data = [destino.a_json() for destino in lista_destinos]
        json.dump(data, f, indent=4) # En este caso se utiliza dump y no dumps

def cargar_datos_destinoCulinario():
    with open('data/destino_culinario.json', 'r') as f:
        data = json.load(f)
        return data

def mostrar_datos_destinoCulinario():
    data = cargar_datos_destinoCulinario()
    for destino_data in data:
        print("id:", destino_data['id'])
        print("nombre:", destino_data['nombre'])
        print("tipo_cocina:", destino_data['tipo_cocina'])
        print("ingredientes:", destino_data['ingredientes'])
        print("precio_minimo:", destino_data['precio_minimo'])
        print("precio_maximo:", destino_data['precio_maximo'])
        print("popularidad:", destino_data['popularidad'])
        print("disponibilidad:", destino_data['disponibilidad'])
        print("id_ubicacion:", destino_data['id_ubicacion'])
        print("imagen:", destino_data['imagen'])
        
        print("--------------------")


# Archivo de Usuarios
def guardar_datos_usuario(lista_usuarios):
    with open('data/usuarios.json','w') as f:  
        data = [usuario.a_json() for usuario in lista_usuarios]
        json.dump(data, f, indent=4) # En este caso se utiliza dump y no dumps

def cargar_datos_usuario():
    with open('data/usuarios.json', 'r') as f:
        data = json.load(f)
        return data

def mostrar_datos_usuario():
    data = cargar_datos_usuario()
    for usuario_data in data:
        print("id:", usuario_data['id'])
        print("nombre:", usuario_data['nombre'])
        print("apellido:", usuario_data['apellido'])
        print("historial de rutas:", usuario_data['historial_rutas'])
        
        print("--------------------")


# Archivo de Actividades
def guardar_datos_actividad(lista_actividades):
    with open('data/actividades.json','w') as f:  
        data = [actividad.a_json() for actividad in lista_actividades]
        json.dump(data, f, indent=4) # En este caso se utiliza dump y no dumps

def cargar_datos_actividad():
    with open('data/actividades.json', 'r') as f:
        data = json.load(f)
        return data

def mostrar_datos_actividad():
    data = cargar_datos_actividad()
    for actividad_data in data:
        print("id:", actividad_data['id'])
        print("nombre:", actividad_data['nombre'])
        print("destino_id:", actividad_data['destino_id'])
        print("hora_inicio:", actividad_data['hora_inicio'])
        
        print("--------------------")


# Archivo de Ubicacion
def guardar_datos_ubicacion(lista_ubicacion):
    with open('data/ubicaciones.json','w') as f:  
        data = [ubicacion.a_json() for ubicacion in lista_ubicacion]
        json.dump(data, f, indent=4) # En este caso se utiliza dump y no dumps

def cargar_datos_ubicacion():
    with open('data/ubicaciones.json', 'r') as f:
        data = json.load(f)
        return data

def mostrar_datos_ubicacion():
    data = cargar_datos_ubicacion()
    for ubicacion_data in data:
        print("id:", ubicacion_data['id'])
        print("direccion:", ubicacion_data['direccion'])
        print("coordenadas:", ubicacion_data['coordenadas'])
        
        print("--------------------")


# Archivo de Review
def guardar_datos_review(lista_review):
    with open('data/review.json','w') as f:  
        data = [review.a_json() for review in lista_review]
        json.dump(data, f, indent=4) # En este caso se utiliza dump y no dumps

def cargar_datos_review():
    with open('data/review.json', 'r') as f:
        data = json.load(f)
        return data

def mostrar_datos_review():
    data = cargar_datos_review()
    for review_data in data:
        print("id:", review_data['id'])
        print("id_destino:", review_data['id_destino'])
        print("id_usuario:", review_data['id_usuario'])
        print("calificacion:", review_data['calificacion'])
        print("comentario:", review_data['comentario'])
        print("animo:", review_data['animo'])
        
        print("--------------------")


# Archivo de Ruta de Visitas
def guardar_datos_rutaVisita(lista_rutaVisita):
    with open('data/rutaVisita.json','w') as f:  
        data = [rutaVisita.a_json() for rutaVisita in lista_rutaVisita]
        json.dump(data, f, indent=4) # En este caso se utiliza dump y no dumps

def cargar_datos_rutaVisita():
    with open('data/rutaVisita.json', 'r') as f:
        data = json.load(f)
        return data

def mostrar_datos_rutaVisita():
    data = cargar_datos_rutaVisita()
    for rutaVisita_data in data:
        print("id:", rutaVisita_data['id'])
        print("nombre:", rutaVisita_data['nombre'])
        print("destinos:", rutaVisita_data['destinos'])
        
        print("--------------------")