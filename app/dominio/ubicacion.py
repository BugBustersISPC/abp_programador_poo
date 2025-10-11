class Ubicacion: 
    _contador_id = 0

    @classmethod 
    def _generar_siguiente_id(cls):
        cls._contador_id += 1
        return cls._contador_id
    
    def __init__(self, nombre: str, id_vivienda:int, id_ubicacion:int = None):
        if id_ubicacion is not None:
            self.id = id_ubicacion
        else:
            self.id = self._generar_siguiente_id()
        self.nombre = nombre
        self.id_vivienda = id_vivienda
        self._dispositivos = []

    def agregar_dispositivo(self, nombre_dispositivo: str):
        if nombre_dispositivo and nombre_dispositivo not in self._dispositivos:
            self._dispositivos.append(nombre_dispositivo)
            return True
        return False
    
    def obtener_dispositivos(self):
        return self._dispositivos.copy()