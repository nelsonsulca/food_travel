import datos
from models import usuario, destino_culinario, actividad, ubicacion, review, ruta_visita

# Destinos Culinarios
destino1= destino_culinario.DestinoCulinario("El pollo loco", "rapida", ["pollo", "huevos", "aceite", "especias"], 25.50, 100.00, 4.5, True, 4, "imagen")

lista_destinos=[destino1]
datos.guardar_datos_destinoCulinario(lista_destinos)
print()
print("MOSTRAMOS LOS DATOS DE LOS DESTINOS CULINARIOS ALMACENADOS EN EL ARCHIVO JSON:")

# datos.mostrar_datos_destinoCulinario()


# Usuarios
usuario1=usuario.Usuario("menganito", "diaz", [2,5,8])
usuario2=usuario.Usuario("julio", "cruz", [9,74,23,52])
usuario3=usuario.Usuario("juan", "perez", [4,8,10])

lista_usuarios=[usuario1, usuario2, usuario3]
datos.guardar_datos_usuario(lista_usuarios)
print()
print()
print("MOSTRAMOS LOS DATOS DE LOS USUARIOS ALMACENADOS EN EL ARCHIVO JSON:")

# datos.mostrar_datos_usuario()


# Actividades
actividad1=actividad.Actividad("La fiesta de comidas", 125, "2023-07-04T09:00:00")
actividad2=actividad.Actividad("Una alegría en tu paladar", 48, "2023-10-02T10:00:00")
actividad3=actividad.Actividad("El terror de los vegetales", 1235, "2023-05-01T02:00:00")

lista_actividades=[actividad1, actividad2, actividad3]
datos.guardar_datos_actividad(lista_actividades)
print()
print()
print("MOSTRAMOS LOS DATOS DE LAS ACTIVIDADES ALMACENADOS EN EL ARCHIVO JSON:")

# datos.mostrar_datos_actividad()


# Ubicaciones
ubicacion1=ubicacion.Ubicacion("san martin 123", ["39° 17′ N", "76° 36′ W"])
ubicacion2=ubicacion.Ubicacion("alverdi 523", ["40° 18′ N", "36° 10′ W"])
ubicacion3=ubicacion.Ubicacion("san juan 321", ["29° 10′ N", "45° ′ W"])

lista_ubicacion=[ubicacion1, ubicacion2, ubicacion3]
datos.guardar_datos_ubicacion(lista_ubicacion)
print()
print()
print("MOSTRAMOS LOS DATOS DE LAS UBICACIONES ALMACENADOS EN EL ARCHIVO JSON:")

# datos.mostrar_datos_ubicacion()


# Reviews
review1=review.Review(2132, 255454, 4, "la comida estuvo muy rica", "psitivo")
review2=review.Review(12, 5455, 1, "la comida fue un asco ya que tenia mucho ajo", "negativo")
review3=review.Review(45322, 58825, 3, "los mozos se tardaron mucho", "positivo")

lista_review=[review1, review2, review3]
datos.guardar_datos_review(lista_review)
print()
print()
print("MOSTRAMOS LOS DATOS DE LOS REVIEWS ALMACENADOS EN EL ARCHIVO JSON:")

# datos.mostrar_datos_review()


# Ruta Visita
rutaVisita1=ruta_visita.RutaVisitada("ruta del cabrito", [2132, 255454, 4])
rutaVisita2=ruta_visita.RutaVisitada("ruta del vino vallisto", [12, 5455, 1])
rutaVisita3=ruta_visita.RutaVisitada("ruta del queso", [45322, 58825, 3])

lista_rutaVisitas=[rutaVisita1, rutaVisita2, rutaVisita3]
datos.guardar_datos_rutaVisita(lista_rutaVisitas)
print()
print()
print("MOSTRAMOS LOS DATOS DE LOS REVIEWS ALMACENADOS EN EL ARCHIVO JSON:")

datos.mostrar_datos_rutaVisita()
