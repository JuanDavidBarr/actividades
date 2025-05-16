#Ejercicio 2 - 🧩 Agenda de Contactos
#Contexto: Vas a construir una agenda que guarda información de contactos personales.
#Tareas:
#Crear: Agregar nuevos contactos. Cada contacto debe tener: Nombre, Teléfono, Email.
#Leer: Listar todos los contactos. Permitir la búsqueda de un contacto por Nombre.
#Actualizar: Actualizar el número de teléfono o el email de un contacto dado su nombre.
#Eliminar: Eliminar un contacto usando su nombre.
#Consideraciones: El nombre del contacto debe ser único dentro de la agenda. Al actualizar o eliminar, primero se debe verificar que el contacto exista.



#Estructura agenda: agenda = { 
# "contacto1": {"nombre": n", "teléfono": "t", "email": "e"},
# "contacto2": {"nombre": n", "teléfono": "t", "email": "e"}
# }

agenda = {
    "Camilo Gutierrez": {"telefono": "3016153861", "email": "camilo.gutierrez@gmail.com"}
}


#1 agregar nuevos contactos
#Inicializamos una variable la cual indicará si el usuario desea agregar otro contacto
desea_agregar = "si"
#loop while para preguntar al usuario si desea agregar un contacto más
while desea_agregar.lower().strip() == "si":
    #preguntamos al usuario la información del nuevo contacto
    nuevo_contacto = input("Ingrese el nuevo contacto: ")
    telefono = input("Ingrese el teléfono del nuevo contacto: ")
    email = input ("Ingrese el email del nuevo contacto: ")
    #setdefault para crear la primer llave externa y la primer pareja "llave"-"valor" interna
    agenda.setdefault(nuevo_contacto, {}).setdefault("Teléfono", telefono)
    #continuamos con el resto de la información
    agenda[nuevo_contacto]["Email"] = email
    desea_agregar = input("¿Desea agregar otro contacto? (si/no): ")
#Mostramos como quedó la agenda actualizada
print("Agenda actualizada")
for llaves,valores in agenda.items():
    print(f"{llaves},{valores}")


#2. Busqueda por nombre
#Inicializamos una variable la cual indicará si el usuario desea buscar otro contacto
desea_buscar = "si"
#loop while para preguntar al usuario si desea agregar un contacto más
while desea_buscar.lower().strip() == "si":
    busqueda_usuario = input("Ingrese el nombre del contacto: ")
    if busqueda_usuario in agenda.keys():
        print(f"Contacto solicitado: {agenda[busqueda_usuario]}")
    else:
        print("El contacto ingresado no se encuentra en la agenda")
    
    desea_buscar = input("¿Desea hacer una nueva búsqueda? (si/no): ")


#3. Actualizar dado el nombre
#Inicializamos una variable la cual indicará si el usuario desea actualizar otro contacto
desea_actualizar = "si"
#loop while para preguntar al usuario si desea actualizar un contacto más
while desea_actualizar.lower().strip() == "si":
    contacto_actualizar = input("Ingrese el contacto que desea actualizar: ")
#verificamos que el contacto se encuentre en la lista de contactos
    if contacto_actualizar in list(agenda.keys()):
        seleccion_usuario = input("Para actualizar número de teléfono escriba \"1\". Para actualizar email escriba \"2\": ")
        if seleccion_usuario.strip() == "1":
            nuevo_numero = input("Ingrese el número nuevo: ")
            agenda[contacto_actualizar]["numero"] = nuevo_numero
            print(f"Contacto actualizado: \n{contacto_actualizar} : {agenda[contacto_actualizar]["numero"]}")
            desea_actualizar = input("¿Desea actualizar otro contacto? (Si/No): ")
        elif seleccion_usuario.strip() == "2":
            nuevo_correo = input("Ingrese el email nuevo: ")
            agenda[contacto_actualizar]["email"] = nuevo_correo
            print(f"Contacto actualizado: \n{contacto_actualizar} : {agenda[contacto_actualizar]["email"]} ")
            desea_actualizar = input("¿Desea acutalizar otro contacto? (Si/No): ")
    else:
        print(f"El contacto {contacto_actualizar}, no se encuentra en la lista. Intente de nuevo")


#4. Eliminar
#Inicializamos una variable la cual indicará si el usuario desea eliminar otro contacto
desea_eliminar = "si"
#loop while para preguntar al usuario si desea actualizar un contacto más
while desea_eliminar == "si":
    contacto_eliminar = input("Ingrese el contacto que desea eliminar: ")
#verificamos que el contacto se encuentre en la lista de contactos
    if contacto_actualizar in list(agenda.keys()):
        eliminado = agenda.pop(contacto_eliminar)
        print(f"{eliminado} ha sido eliminado de los contactos")
        desea_eliminar = input("¿Desea eliminar otro contacto? (Si/No): ")
    else:
        print(f"El contacto {contacto_eliminar}, no se encuentra en la lista. Intente de nuevo")
    


    
              

    






