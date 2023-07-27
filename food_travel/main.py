import datos
from models import usuario, destino_culinario, actividad, ubicacion, review, ruta_visita


def agregar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    apellido = input("Ingrese el apellido del usuario: ")
    rutas= int(input("Ingrese la cantidad de rutas realizadas: "))
    historial_rutas= []
    for i in range(rutas):
        id_ruta= int(input(f"Ingrese el id de la ruta recorrida: "))
        historial_rutas.append(id_ruta)

    nuevo_usuario = usuario.Usuario(nombre, apellido, historial_rutas)
    lista_usuarios = datos.cargar_datos('usuarios')

    if lista_usuarios is None:  # Si no hay objetos en el archivo, se crea una lista vacía
        lista_usuarios = []
    
    lista_usuarios.append(nuevo_usuario)

    datos.guardar_datos(lista_usuarios, 'usuarios')
    print("Usuario agregado exitosamente.")


def agregar_actividad():
    nombre = input("Ingrese el nombre de la actividad: ")
    destino_id = int(input("Ingrese el identificador de la actividad: "))
    hora_inicio = input("Ingrese la hora de inicio de la actividad ")

    nueva_actividad = actividad.Actividad(nombre, destino_id, hora_inicio)
    lista_actividades = datos.cargar_datos('actividades') # Se crea una lista con los objetos que retorna la funcion cargar_datos

    if lista_actividades is None:  # Si no hay objetos en el archivo, se crea una lista vacía
        lista_actividades = []
    lista_actividades.append(nueva_actividad)

    datos.guardar_datos(lista_actividades, 'actividades')
    print("Actividad agregada exitosamente.")


def agregar_destino_culinario():
    nombre = input("Ingrese el nombre del destino: ")
    tipo_cocina = input("Ingrese el tipo de cocina: ")
    cant_ingredientes= int(input("Ingrese la cantidad de ingredientes utilizados: "))
    ingredientes= []
    for i in range(1,cant_ingredientes + 1):
        ingrediente= input(f"Ingrese el ingrediente {i}: ")
        ingredientes.append(ingrediente)
    precio_minimo= float(input("Ingrese el precio mínimo: "))
    precio_maximo= float(input("Ingrese el precio máximo: "))
    popularidad= float(input("Ingrese la popularidad del destino culinario: "))
    disponibilidad= bool(input("Ingrese True si esta disponible o False si no lo está: "))
    id_ubicacion= int(input("Ingrese el id de la ubicacion del destino culinario: "))
    imagen= "imagen"    

    nuevo_destino = destino_culinario.DestinoCulinario(nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad, disponibilidad, id_ubicacion, imagen)
    lista_destinos = datos.cargar_datos('destino_culinario') # Se crea una lista con los objetos que retorna la funcion cargar_datos

    if lista_destinos is None:  # Si no hay objetos en el archivo, se crea una lista vacía
        lista_destinos = []
    lista_destinos.append(nuevo_destino)

    datos.guardar_datos(lista_destinos, 'destino_culinario')
    print("Destino agregado exitosamente.")


def agregar_review():
    id_destino = int(input("Ingrese el id del destino culinario que quiere calificar: "))
    id_usuario = int(input("Ingrese el id del usuario que escribe el review: "))
    calificacion = int(input("Ingrese una calificacion del 1 al 5: "))
    comentario = input("Ingrese un comentario: ")
    animo = input("Ingrese si el lugar le parecio Positivo o Negativo: ")

    nuevo_review = review.Review(id_destino, id_usuario, calificacion, comentario, animo)
    lista_reviews = datos.cargar_datos('review') # Se crea una lista con los objetos que retorna la funcion cargar_datos

    if lista_reviews is None:  # Si no hay objetos en el archivo, se crea una lista vacía
        lista_reviews = []
    lista_reviews.append(nuevo_review)

    datos.guardar_datos(lista_reviews, 'reviews')
    print("Review agregado exitosamente.")


def agregar_ruta():
    nombre = input("Ingrese el nombre de la ruta: ")
    cant_destinos= int(input("Ingrese la cantidad de destinos culinarios que tiene la ruta visita: "))
    destinos= []
    for i in range(1,cant_destinos+1):
        id_destino= int(input(f"Ingrese el id del destino {i}: "))
        destinos.append(id_destino)

    nueva_ruta = ruta_visita.RutaVisitada(nombre, destinos)
    lista_rutas = datos.cargar_datos('ruta_visita') # Se crea una lista con los objetos que retorna la funcion cargar_datos

    if lista_rutas is None:  # Si no hay objetos en el archivo, se crea una lista vacía
        lista_rutas = []
    lista_rutas.append(nueva_ruta)

    datos.guardar_datos(lista_rutas, 'ruta_visita')
    print("Actividad agregada exitosamente.")

def agregar_ubicacion():
    direccion = input("Ingrese la direccion de la ubicacion: ")
    latitud= input("Ingrese la latitud de la ubicacion: ")
    longitud= input("Ingrese la longitud de la ubicacion: ")
    coordenadas= [latitud, longitud]
    
    nueva_ubicacion = ubicacion.Ubicacion(direccion, coordenadas)
    lista_ubicacion = datos.cargar_datos('ubicacion') # Se crea una lista con los objetos que retorna la funcion cargar_datos

    if lista_ubicacion is None:  # Si no hay objetos en el archivo, se crea una lista vacía
        lista_ubicacion = []
    lista_ubicacion.append(nueva_ubicacion)

    datos.guardar_datos(lista_ubicacion, 'ubicacion')
    print("Actividad agregada exitosamente.")


def menu_eliminar():
    
    print()
    print("1- Actividad\n2- Destino Culinario\n3- Review\n4- Ruta Visitada\n5- Ubicacion\n6- Usuario")
    opcion=int(input("Seleccione una opcion para borrar: "))
    if opcion==1:
        id_actividad=int(input("Ingrese el id de la actividad que quiere eliminar: "))
        datos.eliminar_datos(id_actividad, "actividades") 
    elif opcion==2:
        id_destinoCulinario=int(input("Ingrese el id del destino culinario que quiere eliminar: "))
        datos.eliminar_datos(id_destinoCulinario, "destino_culinario") 
    elif opcion==3:
        id_review=int(input("Ingrese el id de la review que quiere eliminar: "))
        datos.eliminar_datos(id_review, "reviews") 
    elif opcion==4:
        id_rutaVisita=int(input("Ingrese el id de la ruta visitada que quiere eliminar: "))
        datos.eliminar_datos(id_rutaVisita, "ruta_visita") 
    elif opcion==5:
        id_ubicacion=int(input("Ingrese el id de la ubicacion que quiere eliminar: "))
        datos.eliminar_datos(id_ubicacion, "ubicacion") 
    elif opcion==6:
        id_usuario=int(input("Ingrese el id del usuario que quiere eliminar: "))
        datos.eliminar_datos(id_usuario, "usuarios") 


def menu_mostrar():
    
    print()
    print("1- Actividad\n2- Destino Culinario\n3- Review\n4- Ruta Visitada\n5- Ubicacion\n6- Usuario")
    opcion=int(input("Seleccione una opcion para mostrar: "))
    if opcion==1:        
        datos.mostrar_datos("actividades") 
    elif opcion==2:        
        datos.mostrar_datos("destino_culinario") 
    elif opcion==3:       
        datos.mostrar_datos("reviews") 
    elif opcion==4:        
        datos.mostrar_datos("ruta_visita") 
    elif opcion==5:        
        datos.mostrar_datos("ubicacion") 
    elif opcion==6:        
        datos.mostrar_datos("usuarios") 


def menu_actualizar():
    print()
    print("1- Actividad\n2- Destino Culinario\n3- Review\n4- Ruta Visitada\n5- Ubicacion\n6- Usuario")
    opcion=int(input("Seleccione una opcion para actualizar: "))
    if opcion==1:
        id_actividad=int(input("Ingrese el id de la actividad que quiere actualizar: "))
        datos.actualizar_datos(id_actividad, "actividades") 
    elif opcion==2:
        id_destinoCulinario=int(input("Ingrese el id del destino culinario que quiere actualizar: "))
        datos.actualizar_datos(id_destinoCulinario, "destino_culinario") 
    elif opcion==3:
        id_review=int(input("Ingrese el id de la review que quiere actualizar: "))
        datos.actualizar_datos(id_review, "reviews") 
    elif opcion==4:
        id_rutaVisita=int(input("Ingrese el id de la ruta visitada que quiere actualizar: "))
        datos.actualizar_datos(id_rutaVisita, "ruta_visita") 
    elif opcion==5:
        id_ubicacion=int(input("Ingrese el id de la ubicacion que quiere actualizar: "))
        datos.actualizar_datos(id_ubicacion, "ubicacion") 
    elif opcion==6:
        id_usuario=int(input("Ingrese el id del usuario que quiere actualizar: "))
        datos.actualizar_datos(id_usuario, "usuarios") 


def main():

    
    while True:
        print("1. Crear")
        print("2. Leer")
        print("3. Actualizar")
        print("4. Borrar")
        print("5. Salir")
        
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            while True:
                print("1. Agregar usuario")
                print("2. Agregar actividad")
                print("3. Agregar destino culinario")
                print("4. Agregar review")
                print("5. Agregar ruta visitada")
                print("6. Agregar ubicacion")
                print("7. Salir")

                opcion2= int(input("Seleccione una opción: "))

                if opcion2 == 1:
                    agregar_usuario()
                elif opcion2 == 2:
                    agregar_actividad()
                elif opcion2 == 3:
                    agregar_destino_culinario()
                elif opcion2 == 4:
                    agregar_review()
                elif opcion2 == 5:
                    agregar_ruta()
                elif opcion2 == 6:
                    agregar_ubicacion()
                elif opcion2 == 7:            
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")

        elif opcion == 2:
            menu_mostrar()
        elif opcion == 3:
            menu_actualizar()
        elif opcion == 4:
            menu_eliminar()       
        elif opcion == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()


