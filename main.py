from app.dao.usuario_dao import UsuarioDAO
from app.dominio.usuario import Usuario, Rol
from app.conn.db_connection import DBConn
from app.dominio.dispositivo import ControladorDispositivos
from getpass import getpass 


def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")

def menu_usuario(usuario: Usuario):
    while True:    
        print("----- Menu Usuario -----")
        print("1. Consultar datos personales")
        print("2. Consultar dispositivos")
        print("3. Cerrar sesion")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            print(usuario.to_object())

        if opcion == 2:
            pass
            
        if opcion == 3:
            print("Cerrando sesion...")
            break

def menu_admin(usuario: Usuario):
    while True:    
        print("----- Menu Administrador -----")
        print("1. Consultar datos personales")
        print("2. Gestionar automatizaciones")
        print("3. Gestionar dispositivos")
        print("4. Gestionar vivienda")
        print("5. Cambiar rol de usuario")
        print("6. Cerrar sesion")
        
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            print(usuario.to_object())
        if opcion == 2:
            gestionar_automatizaciones()
        if opcion == 3:
            gestionar_dispositivos()
        if opcion == 4:
            gestionar_vivienda()
        if opcion == 5:
            cambiar_rol_usuario()
        if opcion == 6:
            print("Cerrando sesion...")
            break

def consultar_datos():
    pass
def gestionar_automatizaciones():
    pass
def gestionar_dispositivos():
    pass
def gestionar_vivienda():
    pass
def cambiar_rol_usuario():
    pass

def registrar_usuario(usuario_dao: UsuarioDAO):
    print("\n=== REGISTRO DE USUARIO ===")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    contrasenia = getpass("Contraseña: ")

    # Verificar si ya existe
    existente = usuario_dao.get_by_email(email)
    if existente:
        print("⚠️ Ese email ya está registrado.")
        return

    usuario = Usuario(
        id_usuario=None,
        nombre=nombre,
        apellido=apellido,
        email=email,
        rol=Rol.USUARIO,
        contrasenia=contrasenia
    )

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

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == '1':
            registrar_usuario(usuario_dao)
        elif opcion == '2':
            usuario = iniciar_sesion(usuario_dao)
            if usuario:
                print(f"\n Sesión iniciada como {usuario._Usuario__nombre}")
                if usuario.is_admin():
                    menu_admin(usuario)
                else:
                    menu_usuario(usuario)
        elif opcion == '3':
            print("👋 Saliendo de la aplicación...")
            break


if __name__ == "__main__":
    menu_principal()