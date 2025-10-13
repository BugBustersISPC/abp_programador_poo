from app.dao.usuario_dao import UsuarioDAO
from app.dao.dispositivo_dao import DispositivoDAO
from app.dao.viviendas_dao import ViviendasDAO
from app.dao.automatizaciones_dao import AutomatizacionDAO
from app.dominio.viviendas import Vivienda
from app.dominio.usuario import Usuario, Rol
from app.dominio.dispositivo import ControladorDispositivos, Dispositivo
from app.dominio.automatizaciones import Automatizaciones
from app.conn.db_connection import DBConn
from getpass import getpass 


def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")


def menu_usuario(usuario: Usuario, dispositivo_dao: DispositivoDAO):
    while True:    
        print("----- Menu Usuario -----")
        print("1. Consultar datos personales")
        print("2. Consultar dispositivos")
        print("3. Cerrar sesion")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            usuario_obj = usuario.to_object()
            if "contrasenia" in usuario_obj:
                del usuario_obj["contrasenia"]
            print(usuario_obj)

        elif opcion == "2":
            dispositivos = dispositivo_dao.get_all()
            if not dispositivos:
                print("No hay dispositivos registrados.")
            else:
                print("\n--- Dispositivos registrados ---")
                for d in dispositivos:
                    estado = "Encendido" if d["Estado"] else "Apagado"
                    print(f"ID: {d['ID_dispositivo']} | Nombre: {d['Nombre']} | Estado: {estado}")

        elif opcion == "3":
            print("Cerrando sesion...")
            break
        else:
            print("Error: Selecciona una opcion correcta")


def menu_admin(usuario: Usuario, vivienda_dao: ViviendasDAO, dispositivo_dao: DispositivoDAO, db: DBConn):
    while True:    
        print("----- Menu Administrador -----")
        print("1. Consultar datos personales")
        print("2. Gestionar automatizaciones")
        print("3. Gestionar dispositivos")
        print("4. Gestionar vivienda")
        print("5. Cambiar rol de usuario")
        print("6. Cerrar sesion")
        
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            usuario_obj = usuario.to_object()
            if "contrasenia" in usuario_obj:
                del usuario_obj["contrasenia"]
            print(usuario_obj)

        elif opcion == "2":
            gestionar_automatizaciones(db)

        elif opcion == "3":
            gestionar_dispositivos(dispositivo_dao)

        elif opcion == "4":
            gestionar_vivienda(vivienda_dao)

        elif opcion == "5":
            resultado = cambiar_rol_usuario(db)
            if resultado:
                print('Rol actualizado correctamente')
                if resultado == usuario._id_usuario:
                    print('Se cambio el rol del usuario actual... Saliendo del menu admin')
                    break

        elif opcion == "6":
            print("Cerrando sesion...")
            break
        else:
            print("Error: Selecciona una opcion correcta")


def gestionar_automatizaciones(db: DBConn):
    automatizacion_dao = AutomatizacionDAO(db)
    dispositivo_dao = DispositivoDAO(db)
    
    tipo_map = {
        "CAMARA": Dispositivo.TIPO_CAMARA,
        "LUZ": Dispositivo.TIPO_LUZ,
        "MUSICA": Dispositivo.TIPO_MUSICA
    }
    
    dispositivos_memoria = [
        Dispositivo(
            nombre=disp_db["Nombre"],
            tipo=tipo_map.get(disp_db["Tipo"], Dispositivo.TIPO_LUZ),
            estado=bool(disp_db["Estado"])
        )
        for disp_db in dispositivo_dao.get_all()
    ]
    
    automatizaciones = Automatizaciones(dispositivos=dispositivos_memoria, 
                                        automatizacion_dao=automatizacion_dao, 
                                        dispositivo_dao=dispositivo_dao)

    while True:
        print("--- Gestion de automatizaciones ---")
        print("1. Activar Modo Fiesta")
        print("2. Desactivar Modo Fiesta")
        print("3. Activar Modo Noche")
        print("4. Desactivar Modo Noche")
        print("5. Configurar hora de activacion Modo Noche")
        print("6. Consultar estado automatizaciones")
        print("7. Volver")
        
        opcion = input("Seleccione una opcion: ")
            
        if opcion == "1":
            print("Activando Modo Fiesta...")
            print(automatizaciones.activar_modo_fiesta())

        elif opcion == "2":
            print("Desactivando Modo Fiesta...")
            print(automatizaciones.apagar_modo_fiesta())

        elif opcion == "3":
            print("Activando Modo Noche...")
            print(automatizaciones.activar_modo_noche())

        elif opcion == "4":
            print("Desactivando Modo Noche...")
            print(automatizaciones.apagar_modo_noche())

        elif opcion == "5":
            hora_actual = automatizaciones.get_hora_activacion_modo_noche()
            print(f"Hora actual configurada: {hora_actual}:00")
            try:
                nueva_hora = int(input("Ingrese la nueva hora (0-23): "))
                if automatizaciones.configurar_hora_modo_noche(nueva_hora):
                    print(f"Configuracion establecida correctamente a las {nueva_hora}:00")
                else:
                    print("Error: La hora debe estar entre 0 y 23")
            except ValueError:
                print("Error: Debe ingresar un numero valido")

        elif opcion == "6":
            modo_fiesta, modo_noche = automatizaciones.consultar_automatizaciones()
            print(f"Modo Fiesta: {'ACTIVO' if modo_fiesta else 'INACTIVO'}")
            print(f"Modo Noche: {'ACTIVO' if modo_noche else 'INACTIVO'}")
            print(f"Hora de activacion modo noche: {automatizaciones.get_hora_activacion_modo_noche()}:00")

        elif opcion == "7":
            break
        else:
            print("Error: Selecciona una opcion correcta")


def gestionar_dispositivos(dispositivo_dao: DispositivoDAO):
    while True:
        print("\n===== Gestión de Dispositivos =====")
        print("1. Listar dispositivos")
        print("2. Crear nuevo dispositivo")
        print("3. Actualizar dispositivo existente")
        print("4. Eliminar dispositivo")
        print("5. Volver al menú anterior")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            dispositivos = dispositivo_dao.get_all()
            if not dispositivos:
                print("No hay dispositivos registrados.")
            else:
                for d in dispositivos:
                    estado = "Encendido" if d["Estado"] else "Apagado"
                    print(f"ID: {d['ID_dispositivo']} | Nombre: {d['Nombre']} | Estado: {estado}")

        elif opcion == "2":
            nombre = input("Nombre del dispositivo: ")
            estado_str = input("Estado inicial (encendido/apagado): ").lower()
            estado = estado_str == "encendido"
            try:
                dispositivo = ControladorDispositivos(nombre=nombre, estado=estado)
                dispositivo_dao.create(dispositivo)
                print("Dispositivo creado correctamente.")
            except Exception as e:
                print(f"Error al crear dispositivo: {e}")

        elif opcion == "3":
            id_disp = int(input("Ingrese el ID del dispositivo a actualizar: "))
            dispositivo = dispositivo_dao.get(id_disp)
            if not dispositivo:
                print("No se encontró el dispositivo.")
            else:
                nuevo_nombre = input(f"Nuevo nombre (actual: {dispositivo.get_nombre()}): ") or dispositivo.get_nombre()
                estado_str = input(f"Nuevo estado (actual: {'encendido' if dispositivo.get_estado() else 'apagado'}): ").lower()
                nuevo_estado = dispositivo.get_estado() if estado_str == "" else estado_str == "encendido"
                dispositivo.set_nombre(nuevo_nombre)
                dispositivo.set_estado(nuevo_estado)
                dispositivo_dao.update(dispositivo)
                print("Dispositivo actualizado correctamente.")

        elif opcion == "4":
            id_disp = int(input("Ingrese el ID del dispositivo a eliminar: "))
            confirm = input("¿Está seguro? (si/no): ").lower()
            if confirm == "si":
                ok = dispositivo_dao.delete(id_disp)
                print("Dispositivo eliminado." if ok else "No se pudo eliminar el dispositivo.")
            else:
                print("Operación cancelada.")

        elif opcion == "5":
            break
        else:
            print("Opción no válida")


def gestionar_vivienda(vivienda_dao: ViviendasDAO):
    while True:
        print("\n===== Gestión de Viviendas =====")
        print("1. Listar viviendas")
        print("2. Crear nueva vivienda")
        print("3. Actualizar vivienda existente")
        print("4. Eliminar vivienda")
        print("5. Volver al menú anterior")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            viviendas = vivienda_dao.get_all()
            for v in viviendas:
                print(f"ID: {v.get_id()} | Nombre: {v.get_nombre()} | Dirección: {v.get_direccion()}")

        elif opcion == "2":
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            vivienda = Vivienda(nombre=nombre, direccion=direccion)
            vivienda_dao.create(vivienda)
            print("Vivienda creada correctamente.")

        elif opcion == "3":
            id_viv = int(input("Ingrese el ID de la vivienda a actualizar: "))
            vivienda = vivienda_dao.get(id_viv)
            if vivienda:
                nuevo_nombre = input(f"Nuevo nombre (actual: {vivienda.get_nombre()}): ") or vivienda.get_nombre()
                nueva_dir = input(f"Nueva dirección (actual: {vivienda.get_direccion()}): ") or vivienda.get_direccion()
                vivienda.set_nombre(nuevo_nombre)
                vivienda.set_direccion(nueva_dir)
                vivienda_dao.update(vivienda)
                print("Vivienda actualizada correctamente.")
            else:
                print("No se encontró la vivienda.")

        elif opcion == "4":
            id_viv = int(input("Ingrese el ID de la vivienda a eliminar: "))
            confirm = input("¿Está seguro? (si/no): ").lower()
            if confirm == "si":
                ok = vivienda_dao.delete(id_viv)
                print("Vivienda eliminada." if ok else "No se pudo eliminar la vivienda.")
            else:
                print("Operación cancelada.")

        elif opcion == "5":
            break
        else:
            print("Opción no válida")


def cambiar_rol_usuario(db: DBConn):
    usuario_dao = UsuarioDAO(db)
    usuarios = usuario_dao.get_all()

    for i, u in enumerate(usuarios):
        print(f"{i+1}) {u.get_nombre_apellido()}")

    opcion = int(input("Seleccione su opción: "))
    usuario = usuarios[opcion-1]
    usuario_obj = usuario.to_object()
    usuario_obj["rol"] = "USUARIO" if usuario.is_admin() else "ADMIN"

    return usuario_dao.update(usuario.id_usuario, usuario_obj)

def registrar_usuario(usuario_dao: UsuarioDAO):
    print("\n=== REGISTRO DE USUARIO ===")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    contrasenia = getpass("Contraseña: ")

    if usuario_dao.get_by_email(email):
        print("⚠️ Ese email ya está registrado.")
        return

    usuario = Usuario(None, nombre, apellido, email, Rol.USUARIO, contrasenia)
    id_nuevo = usuario_dao.create(usuario.to_object())
    print(f"✅ Usuario registrado con ID: {id_nuevo}")


def iniciar_sesion(usuario_dao: UsuarioDAO):
    print("\n=== INICIO DE SESIÓN ===")
    email = input("Email: ")
    contrasenia = getpass("Contraseña: ")

    usuario = usuario_dao.get_by_email(email)
    if not usuario:
        print("Usuario no encontrado.")
        return None

    if usuario._contrasenia == contrasenia:
        print(f"Bienvenido, {usuario._Usuario__nombre} ({usuario._Usuario__email})")
        return usuario
    else:
        print("Contraseña incorrecta.")
        return None


def menu_principal():
    db = DBConn()
    usuario_dao = UsuarioDAO(db)
    dispositivo_dao = DispositivoDAO(db)
    vivienda_dao = ViviendasDAO(db)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == '1':
            registrar_usuario(usuario_dao)
        elif opcion == '2':
            usuario = iniciar_sesion(usuario_dao)
            if usuario:
                if usuario.is_admin():
                    menu_admin(usuario, vivienda_dao, dispositivo_dao, db)
                else:
                    menu_usuario(usuario, dispositivo_dao)
        elif opcion == '3':
            print("👋 Saliendo de la aplicación...")
            break
        else:
            print("Error: Selecciona una opcion correcta")


if __name__ == "__main__":
    menu_principal()
