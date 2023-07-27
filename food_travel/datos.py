import json
from models import usuario, actividad, destino_culinario, review, ruta_visita, ubicacion



def guardar_datos(lista_datos, nombre_archivo):
    """
    Esta función recibe una lista de objetos y los convierte al formato json y los guarda en un archivo JSON de la carpeta 'data'
    """
    with open(f'data/{nombre_archivo}.json','w') as f:  # Abrir archivo JSON para escritura
        data = [dato.a_json() for dato in lista_datos] #se crea una lista, se itera sobre el elemento 'dato' y se llama al metodo a_json por cada iteracion
        json.dump(data, f, indent=4) # La lista de diccionarios 'data' se convierte al formato JSON y se almacena en el archivo.json 


def cargar_datos(nombre_archivo):
    """
    Esta función convierte los elementos de un archivo JSON en objetos para luego guardarlos en una lista vacia y nos retornará esa lista de objetos 
    """
    try:
        with open(f'data/{nombre_archivo}.json', 'r') as f: # Abrir el archivo json para la lectura
            data = json.load(f) # Cargar los datos JSON desde el archivo en formato de lista de diccionarios
        lista_datos = [] # Crear una lista vacía para almacenar los objetos de la clase Usuario

        for elemento_data in data:
            tipo = elemento_data.get('tipo')  # Obtener el tipo del elemento

            if elemento_data['tipo'] == 'Usuario': # Verificar si el tipo de elemento es 'Usuario' (esto se indica en el JSON)
                usuario_obj = usuario.Usuario(elemento_data['nombre'], elemento_data['apellido'], elemento_data['historial_rutas']) # Si es un elemento de tipo 'Usuario', crear un objeto Usuario y agregarlo a la lista_usuarios
                lista_datos.append(usuario_obj)
            elif tipo == 'Actividad':
                actividad_obj = actividad.Actividad(elemento_data['nombre'], elemento_data['destino_id'], elemento_data['hora_inicio'])
                lista_datos.append(actividad_obj)
            elif tipo == 'DestinoCulinario':
                destino_culinario_obj = destino_culinario.DestinoCulinario(
                    elemento_data['nombre'], elemento_data['tipo_cocina'], elemento_data['ingredientes'],
                    elemento_data['precio_minimo'], elemento_data['precio_maximo'], elemento_data['popularidad'],
                    elemento_data['disponibilidad'], elemento_data['id_ubicacion'], elemento_data['imagen']
                )
                lista_datos.append(destino_culinario_obj)
            elif tipo == 'Review':
                review_obj = review.Review(
                    elemento_data['id_destino'], elemento_data['id_usuario'], elemento_data['calificacion'],
                    elemento_data['comentario'], elemento_data['animo']
                )
                lista_datos.append(review_obj)
            elif tipo == 'RutaVisitada':
                ruta_visitada_obj = ruta_visita.RutaVisita(
                    elemento_data['nombre'], elemento_data['destinos']
                )
                lista_datos.append(ruta_visitada_obj)
            elif tipo == 'Ubicacion':
                ubicacion_obj = ubicacion.Ubicacion(
                    elemento_data['direccion'], elemento_data['coordenadas']
                )
                lista_datos.append(ubicacion_obj)

        return lista_datos

    except FileNotFoundError:
        return None
    
    
def eliminar_datos(id_eliminar, nombre_archivo):

    with open(f'data/{nombre_archivo}.json', 'r') as f:
        data = json.load(f)

    elemento_encontrado = None

    for elemento_data in data:
        if elemento_data['id'] == id_eliminar:
            elemento_encontrado = elemento_data
            break

    if elemento_encontrado:
        data.remove(elemento_encontrado)
        with open(f'data/{nombre_archivo}.json', 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Elemento con ID {id_eliminar} eliminado exitosamente.")
        return True
    else:
        print(f"No se encontró ningún elemento con el ID {id_eliminar}.")
        return False
    

def mostrar_datos(nombre_archivo):
    with open(f'data/{nombre_archivo}.json', 'r') as f:
        data = json.load(f)

    if data:
        print(f"Elementos encontrados en el archivo {nombre_archivo}.json:")
        for elemento in data:
            print("ID:", elemento['id'])
            print("Tipo:", elemento['tipo'])
            print("Datos:", elemento)
            print("-------------------")
        return data
    else:
        print(f"No se encontró ningún elemento en el archivo {nombre_archivo}.json.")
        return None
    


def actualizar_datos(id_actualizar, nombre_archivo):
    with open(f'data/{nombre_archivo}.json', 'r') as f:
        data = json.load(f)

    elemento_encontrado = None

    for elemento_data in data:
        if elemento_data['id'] == id_actualizar:
            elemento_encontrado = elemento_data
            break

    if elemento_encontrado:
        if elemento_encontrado['tipo'] == 'Usuario':            
            nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
            nuevo_apellido = input("Ingrese el nuevo apellido del usuario: ")
            elemento_encontrado['nombre'] = nuevo_nombre
            elemento_encontrado['apellido'] = nuevo_apellido            
            print("Usuario modificado exitosamente.")

        elif elemento_encontrado['tipo'] == 'Actividad':            
            nuevo_nombre = input("Ingrese el nuevo nombre de la actividad: ")
            nueva_hora= input("Ingrese la nueva hora de la actividad: ")
            elemento_encontrado['nombre'] = nuevo_nombre
            elemento_encontrado['hora_inicio'] = nueva_hora
            print("Actividad modificada exitosamente.")

        elif elemento_encontrado['tipo'] == 'DestinoCulinario':            
            nuevo_nombre = input("Ingrese el nuevo nombre del destino culinario: ")
            nuevo_tipo_cocina= input("Ingrese el nuevo tipo de cocina del destino culinario: ")
            cant_ingredientes= int(input("Ingrese la cantidad de ingredientes utilizados: "))
            nuevos_ingredientes= []
            for i in range(1,cant_ingredientes + 1):
                ingrediente= input(f"Ingrese el ingrediente {i}: ")
                nuevos_ingredientes.append(ingrediente)
            nuevo_precio_minimo= input("Ingrese el nuevo precio minimo: ")
            nuevo_precio_maximo= input("Ingrese el nuevo pricio maximo: ")
            elemento_encontrado['nombre'] = nuevo_nombre
            elemento_encontrado['tipo_cocina'] = nuevo_tipo_cocina
            elemento_encontrado['ingredientes'] = nuevos_ingredientes
            elemento_encontrado['precio_minimo'] = nuevo_precio_minimo
            elemento_encontrado['precio_maximo'] = nuevo_precio_maximo
            print("Actividad modificada exitosamente.")

        elif elemento_encontrado['tipo'] == 'Review':            
            nuevo_comentario = input("Ingrese el nuevo cometario: ")
            nuevo_animo= input("Ingrese el nuevo animo: ")
            elemento_encontrado['comentario'] = nuevo_comentario
            elemento_encontrado['animo'] = nuevo_animo
            print("Actividad modificada exitosamente.")

        elif elemento_encontrado['tipo'] == 'RutaVisitada':            
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            elemento_encontrado['nombre'] = nuevo_nombre            
            print("Actividad modificada exitosamente.")

        elif elemento_encontrado['tipo'] == 'Ubicacion':            
            nueva_direccion = input("Ingrese la nueva direccion: ")
            elemento_encontrado['direccion'] = nueva_direccion            
            print("Actividad modificada exitosamente.")
    else:
        print(f"No se encontró ningún elemento con el ID {id_actualizar}.")

    # Guardar los cambios en el archivo JSON
    with open(f'data/{nombre_archivo}.json', 'w') as f:
        json.dump(data, f, indent=4)




    







    
