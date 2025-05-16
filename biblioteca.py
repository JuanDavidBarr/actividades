#Ejericio 1 - 🧩 Gestión de Biblioteca

#Contexto:
#Una pequeña biblioteca necesita registrar sus libros en un sistema muy simple.
#Tareas:
#Crear: Agrega nuevos libros al diccionario. Cada libro tendrá: ID, Título, Autor, Año de publicación.
#Leer: Muestra todos los libros almacenados. Permite buscar un libro por su ID o Título.
#Actualizar: Modifica la información de un libro dado su ID. Ejemplo: cambiar el autor o el año de publicación.
#Eliminar: Elimina un libro de la biblioteca usando su ID.
biblioteca = {
    "001": {"título": "La vorágine", "autor": "José Eustasio Rivera", "año": 1924},
    "002": {"título": "Las intermitencias de la muerte", "autor": "José Saramago", "año": 2005},
    "003": {"título": "El club Dumas", "autor": "Arturo Pérez-Reverte", "año": 1993},
    "004": {"título": "Cien años de soledad", "autor": "Gabrel García Márquez", "año": 1967},
    "005": {"título": "La fiesta del chivo", "autor": "Mario Vargas Llosa", "año": 2000}
}


#Menu de opciones
menu = {
    "opción1": "agregar libro", "opción2": "buscar libro", "opción3": "mostrar inventario", "opción4": "actualizar", "opción5": "eliminar", "opción6": "salir"
}


#Confirmación para acceder al menú
#loop while para verificar la entrada del usuario
while True:
    acceder_menu = input("¿Desea acceder al menú? (Si/No): ").lower().strip()
    if not acceder_menu.isalpha() or (acceder_menu != "si" and acceder_menu != "no"):
        print("Por favor ingrese solo \"si\" o \"no\"")
    else:
        break  

#En caso de que desee entrar al menú.   
if acceder_menu == "si":
    print(f"Estas son las opciones: \n{menu}")


#loop while para verificar la entrada del usuario (OPCIONES MENÚ)
    while True:
        accion_usuario = input("Ingrese por favor, la acción que desea llevar a cabo: ")
        if accion_usuario != "1" and accion_usuario != "2" and accion_usuario != "3" and accion_usuario != "4" and accion_usuario != "5" and accion_usuario != "6":
            print("La opción ingresada no se encuentra en el menú, por favor intente de nuevo")
        else: 
            break


#Opción 1 del menú
    if accion_usuario.strip() == "1":
#loop while para verificar la entrada del usuario (NO REPETIR INDICE)
        while True:
            id_nuevo = input("Ingrese el nuevo ID del nuevo libro: ")
            if id_nuevo in biblioteca:
                print("El ID ingresado ya se encuentra en la biblioteca, pruebe con otro")
            else:
                break
        titulo_nuevo = input("Ingrese el titulo: ")
        autor_nuevo = input("Ingrese el autor: ")
        año_nuevo = input("Ingrese el año de publicación: ")
#se usa el método "setdefault" para crear una nueva "key" y posteriormente agregar la primer pareja "key" y "value"
        biblioteca.setdefault(id_nuevo,{}).setdefault("título", titulo_nuevo)
#se agrega el resto de la información del nuevo libro
        biblioteca[id_nuevo]["autor"] = autor_nuevo
        biblioteca[id_nuevo]["año"] = año_nuevo
        print(f"Se muestra la biblioteca actualizada: \n{biblioteca}")


#Opción 2 del menú
    elif accion_usuario.strip() == "2":
#loop while para verificar la entrada del usuario (SOLO SÍ O NO)
        while True:
            formato_busqueda = input("Ingrese \"1\" si desea buscar por ID. Ingrese \"2\" si desea buscar por título: ")
#Se ofrecen dos opciones de modo de búsqueda, dependiendo de cual elija, se da la información. 
            if formato_busqueda.strip() == "1":
#loop while para verificar la entrada del usuario (INDICE)
                while True:
                    busqueda_usuario = input("Ingrese el ID del libro: ")
                    if busqueda_usuario in biblioteca:
                        break
                    else:
                        print("El ID ingresado no existe")
#se usa la función get para obtener el título, se debe usar dos veces ya que se trata de un diccionario anidado
                titulo_buscado = biblioteca.get(busqueda_usuario.strip()).get("título")
                print(f"El libro con el ID {busqueda_usuario}, corresponde al libro {titulo_buscado} y se encuentra disponible")
                break
            elif formato_busqueda == "2": 
#loop while para preguntar si desea intentar de nuevo
                while True:
                    busqueda_usuario = input("Ingrese el título del libro: ")
#como no sabemos el ID del libro usamos for para busque el título
                    titulo_encontrado = False
                    for id,v in biblioteca.items():
#esta variable sirve como indicador de que el libro fue encontrado
                        for id_2 in v:
                            if busqueda_usuario == v["título"]:
                                titulo_encontrado = True
                                print(f"El libro {busqueda_usuario} está en el inventario y se encuentra disponible")
                                break
                            break
                    if titulo_encontrado == False:
                        print("El libro no se encuentra en nuestro inventario")
                        nueva_busqueda = input(("¿Desea intentar de nuevo? (si/no): "))
                        if nueva_busqueda.lower().strip() == "si":
                            print("Buscando de nuevo")
                        elif nueva_busqueda.lower().strip() == "no":
                            break
                    else:
                        break
                break            
            else:
                print("Por favor ingrese solo \"1\" ó \"2\"")


#opción 3. Muestra todo el inventario de la biblioteca
    elif accion_usuario == "3":
        print(f"Este es nuestro inventario: \n {biblioteca.values()}")


#opción 4. Actualizar
    elif accion_usuario == "4":
#loop while para verificar la entrada del usuario (INDICE)
        while True:
            id_libro_modificar = input("Ingrese el ID del libro que desea modificar: ")
            if id_libro_modificar in biblioteca:
                break
            else:
                print("El ID ingresado no existe")
        while True:
            informacion_modificar = input("Ingrese el tipo de información que desea modificar: \n(1) para título, (2) para autor, (3) para año. ")
            if informacion_modificar.strip() == "1":
#Pedimos el nuevo título y accedemos al id indicado para modificar el título con la información ingresada
                nuevo_titulo = biblioteca[id_libro_modificar]["título"] = input("Ingrese el nuevo título: ")
                print(f"El nuevo título del libro es {nuevo_titulo}")
                print(f"Inventario actualizado: \n {biblioteca.values()}")               
#Pedimos el nuevo autor y accedemos al id indicado para modificar el título con la información ingresada
            elif informacion_modificar.strip() == "2":
                nuevo_autor = biblioteca[id_libro_modificar]["autor"] = input("Ingrese el nuevo autor: ")
                print(f"El nuevo autor del libro es {nuevo_autor}")
                print(f"Inventario actualizado: \n {biblioteca.values()}")                
#Pedimos el nuevo año y accedemos al id indicado para modificar el título con la información ingresada
            elif informacion_modificar.strip() == "3":
                nuevo_año = biblioteca[id_libro_modificar]["autor"] = input("Ingrese el nuevo año: ")
                print(f"El nuevo título del libro es {nuevo_año}")
                print(f"Inventario actualizado: \n {biblioteca.values()}")                
            else:
                print("Opción no válida, intente de nuevo")
            nueva_actualización = input("¿Desea actualizar algún otro libro (si/no): ")
            if nueva_actualización.lower().strip() == "si":
                print("Generando nueva actualización")
            elif nueva_actualización.lower().strip == "no":
                break
            else:
                print("Por favor responda solo \"si\" o \"no\" ")
                break

#opción 5. Eliminar
    elif accion_usuario == "5":
#loop while para verificar la entrada del usuario (ELIMINAR MÁS LIBROS)
        while True:       
#loop while para verificar la entrada del usuario (INDICE)
            while True:
                id_libro_eliminar = input("Ingrese el ID del libro que desea eliminar: ")
                if id_libro_eliminar in biblioteca:
                    break
                else:
                    print("El ID ingresado no existe")
            print(f"El libro con ID: {id_libro_eliminar}, \"{biblioteca[id_libro_eliminar]["título"]}\" ha sido eliminado")
            libro_eliminado = biblioteca.pop(id_libro_eliminar)
            print(f"Inventario actualizado: \n {biblioteca.values()}")
            eliminar_otro_libro = input("¿Desea eliminar otro libro? (si/no): ")
            if eliminar_otro_libro.lower().strip() == "si":
                print("preparando")
            elif eliminar_otro_libro.lower().strip() == "no":
                break


#opción 6. Salir
    elif accion_usuario == "6":
                print("Gracias por utilizar nuestro menú")      


elif acceder_menu == "no":
    print("Hasta la proxima!")