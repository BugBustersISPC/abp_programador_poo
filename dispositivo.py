
class Dispositivo:
    """
    representa un dispositivo inteligente dentro del hogar
    los atributos se mantienen privados y se accede a ellos a través de propiedades
    """
    # absorbemos la clase TipoDispositivo como constantes de clase para mayor claridad
    TIPO_CAMARA = 1
    TIPO_LUZ = 2
    TIPO_MUSICA = 3
    
    # un diccionario para mapear el tipo numérico a un texto descriptivo
    __TIPO_A_TEXTO = {
        TIPO_CAMARA: "Cámara",
        TIPO_LUZ: "Luz",
        TIPO_MUSICA: "Música"
    }

    def __init__(self, nombre: str, tipo: int, estado: bool):
        
       # constructor de la clase Dispositivo
       # valida los datos de entrada antes de crear el objeto
        
        # validación de atributos
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre no puede estar vacío y debe ser un texto.")
        if tipo not in self.__TIPO_A_TEXTO:
            raise ValueError(f"El tipo de dispositivo '{tipo}' no es válido.")
        if not isinstance(estado, bool):
            raise ValueError("El estado debe ser un valor booleano (True/False).")
            
        #  atributos privados
        self.__nombre = nombre
        self.__tipo = tipo
        self.__estado = estado

    # getters para acceso controlado a los atributos
    @property
    def nombre(self) -> str:
        """obtiene el nombre del dispositivo."""
        return self.__nombre

    @property
    def tipo(self) -> int:
        """obtiene el tipo numérico del dispositivo"""
        return self.__tipo
        
    @property
    def estado(self) -> bool:
        """obtiene el estado (On/Off) del dispositivo"""
        return self.__estado

    # --- Setter para modificar el estado con validación ---
    @estado.setter
    def estado(self, nuevo_estado: bool):
        """establece un nuevo estado para el dispositivo, validando que sea booleano"""
        if not isinstance(nuevo_estado, bool):
            raise ValueError("El estado solo puede ser True o False.")
        self.__estado = nuevo_estado

    # --- Métodos de la clase ---
    def encender(self):
        """cambia el estado del dispositivo a encendido (True)"""
        self.__estado = True
        print(f"El dispositivo '{self.nombre}' ha sido encendido.")

    def apagar(self):
        """cambia el estado del dispositivo a apagado (False)"""
        self.__estado = False
        print(f"El dispositivo '{self.nombre}' ha sido apagado.")

    def __str__(self):
        """
        devuelve una representación en formato de texto del dispositivo
        """
        tipo_texto = self.__TIPO_A_TEXTO.get(self.__tipo, "Desconocido")
        estado_texto = "On" if self.__estado else "Off"
        return f"{self.nombre} (Tipo: {tipo_texto}) - Estado: {estado_texto}"
    

class ControladorDispositivos:
    """
    gestiona la colección de objetos Dispositivo
    se encarga de agregar, eliminar, buscar y listar los dispositivos
    """
    def __init__(self):
        # inicializa el controlador con una lista vacía de dispositivos
        self.__dispositivos = []

    def agregar_dispositivo(self, nombre: str, tipo: int, estado: bool) -> bool:
        """
        agrega un nuevo dispositivo a la coleccion
        no permite agregar dispositivos con nombres duplicados
        devuelve True si se agrego, False en caso contrario
        """
        if self.buscar_por_nombre(nombre):
            print(f"Error: Ya existe un dispositivo con el nombre '{nombre}'.")
            return False
        
        try:
            nuevo_dispositivo = Dispositivo(nombre, tipo, estado)
            self.__dispositivos.append(nuevo_dispositivo)
            print(f"Dispositivo '{nombre}' agregado correctamente.")
            return True
        except ValueError as e:
            print(f"Error al crear el dispositivo: {e}")
            return False

    def buscar_por_nombre(self, nombre: str) -> Dispositivo | None:
        """
        busca un dispositivo por su nombre
        devuelve el objeto Dispositivo si lo encuentra, o None si no
        """
        for dispositivo in self.__dispositivos:
            if dispositivo.nombre.lower() == nombre.lower():
                return dispositivo
        return None

    def eliminar_dispositivo(self, nombre: str) -> bool:
        """
        elimina un dispositivo de la colección por su nombre
        devuelve True si se eliminó, False si no se encontró
        """
        dispositivo_a_eliminar = self.buscar_por_nombre(nombre)
        if dispositivo_a_eliminar:
            self.__dispositivos.remove(dispositivo_a_eliminar)
            print(f"Dispositivo '{nombre}' eliminado.")
            return True
        
        print(f"Error: No se encontró el dispositivo '{nombre}' para eliminar.")
        return False

    def listar_dispositivos(self):
        # muestra en pantalla todos los dispositivos registrados
        print("\n--- LISTA DE DISPOSITIVOS ---")
        if not self.__dispositivos:
            print("No hay dispositivos registrados.")
        else:
            for dispositivo in self.__dispositivos:
                print(f"- {dispositivo}") # Usa el método __str__ de Dispositivo
        print("-----------------------------\n")
