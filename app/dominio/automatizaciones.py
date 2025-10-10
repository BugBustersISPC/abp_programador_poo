from datetime import datetime
from app.dominio.dispositivo import Dispositivo
from app.dao.interfaces.i_automatizaciones_dao import IAutomatizacionDAO
from app.dao.interfaces.i_dispositivo_dao import IDispositivoDAO

class Automatizaciones:
    MODO_FIESTA = "Modo Fiesta"
    MODO_NOCHE = "Modo Noche"
    
    def __init__(self, dispositivos: list[Dispositivo], automatizacion_dao: IAutomatizacionDAO, dispositivo_dao: IDispositivoDAO):
        if not all(isinstance(dispositivo, Dispositivo) for dispositivo in dispositivos):
            raise ValueError("Todos los elementos deben ser objetos de la clase Dispositivo.")
        self._dispositivos = dispositivos
        self._automatizacion_dao = automatizacion_dao
        self._dispositivo_dao = dispositivo_dao
        self._hora_activacion_modo_noche = 23

        self._sincronizar_automatizaciones()

    def _sincronizar_automatizaciones(self):
        try:
            modo_fiesta_db = self._automatizacion_dao.find_by_accion(self.MODO_FIESTA)
            if not modo_fiesta_db:
                self._automatizacion_dao.create({"Accion": self.MODO_FIESTA, "Estado": False})
            
            modo_noche_db = self._automatizacion_dao.find_by_accion(self.MODO_NOCHE)
            if not modo_noche_db:
                self._automatizacion_dao.create({"Accion": self.MODO_NOCHE, "Estado": False})
        except Exception as error:
            return f"Advertencia: No se pudieron sincronizar automatizaciones: {error}"
        
    # Getter
    def get_dispositivos(self):
        return self._dispositivos
    def get_hora_activacion_modo_noche(self):
        return self._hora_activacion_modo_noche
   
   # Setter
    def set_dispositivos(self, dispositivos: list[Dispositivo]):
        if all(isinstance(dispositivo, Dispositivo) for dispositivo in dispositivos):
            self._dispositivos = dispositivos
            return True
        return False
    def set_hora_activacion_modo_noche(self, nueva_hora: int):
        if nueva_hora < 0 or nueva_hora > 23:
            return False
        self._hora_activacion_modo_noche = nueva_hora
        return True
    
    # Funciones
    def consultar_automatizaciones(self):
        luces_equipomusica = [dispositivo.estado for dispositivo in self._dispositivos if dispositivo.tipo in (Dispositivo.TIPO_LUZ, Dispositivo.TIPO_MUSICA)]
        modo_fiesta = all(luces_equipomusica) if luces_equipomusica else False

        camaras = [dispositivo.estado for dispositivo in self._dispositivos if dispositivo.tipo == Dispositivo.TIPO_CAMARA]
        modo_noche = any(camaras) if camaras else False

        return modo_fiesta, modo_noche

    def mostrar_estado(self):
        modo_fiesta, modo_noche = self.consultar_automatizaciones()
        estado_fiesta = "On" if modo_fiesta else "Off"
        estado_noche = "On" if modo_noche else "Off"
        return f"Estado de Automatizaciones: - Modo Fiesta: {estado_fiesta} / - Modo Noche: {estado_noche}"

    def activar_modo_fiesta(self):
        try:
            for dispositivo in self._dispositivos:
                if dispositivo.tipo in [Dispositivo.TIPO_LUZ, Dispositivo.TIPO_MUSICA] and not dispositivo.estado:
                    dispositivo.encender()
                    self._sincronizar_estado_dispositivo(dispositivo)
            
            modo_fiesta_db = self._automatizacion_dao.find_by_accion(self.MODO_FIESTA)
            if modo_fiesta_db:
                self._automatizacion_dao.set_estado(modo_fiesta_db[0]["ID_automatizacion"], True)
            return "Modo Fiesta activado: Equipo de Musica y Luces encendidas."
        except Exception as error:
            return f"Error al activar modo fiesta: {error}"
    
    def apagar_modo_fiesta(self):
        try:
            for dispositivo in self._dispositivos:
                if dispositivo.tipo in (Dispositivo.TIPO_LUZ, Dispositivo.TIPO_MUSICA) and dispositivo.estado:
                    dispositivo.apagar()
                    self._sincronizar_estado_dispositivo(dispositivo)
            
            modo_fiesta_db = self._automatizacion_dao.find_by_accion(self.MODO_FIESTA)
            if modo_fiesta_db:
                self._automatizacion_dao.set_estado(modo_fiesta_db[0]["ID_automatizacion"], False)
            
            return "Modo fiesta desactivado: Equipo de Musica y Luces apagadas."
        except Exception as error:
            return f"Error al apagar modo fiesta: {error}"
    
    def activar_modo_noche(self):
        try:
            for dispositivo in self._dispositivos:
                if dispositivo.tipo == Dispositivo.TIPO_CAMARA and not dispositivo.estado:
                    dispositivo.encender()
                    self._sincronizar_estado_dispositivo(dispositivo)
            
            modo_noche_db = self._automatizacion_dao.find_by_accion(self.MODO_NOCHE)
            if modo_noche_db:
                self._automatizacion_dao.set_estado(modo_noche_db[0]["ID_automatizacion"], True)
            
            return "Modo noche activado: Camaras encendidas."
        except Exception as error:
            return f"Error al activar modo noche: {error}"

    def apagar_modo_noche(self):
        try:
            for dispositivo in self._dispositivos:
                if dispositivo.tipo == Dispositivo.TIPO_CAMARA and dispositivo.estado:
                    dispositivo.apagar()
                    self._sincronizar_estado_dispositivo(dispositivo)
            
            modo_noche_db = self._automatizacion_dao.find_by_accion(self.MODO_NOCHE)
            if modo_noche_db:
                self._automatizacion_dao.set_estado(modo_noche_db[0]["ID_automatizacion"], False)
            
            return "Modo noche desactivado: Camaras apagadas."
        except Exception as error:
            return f"Error al apagar modo noche: {error}"
    
    def configurar_hora_modo_noche(self, nueva_hora: int):
        if nueva_hora < 0 or nueva_hora > 23:
            return False
        self._hora_activacion_modo_noche = nueva_hora
        return True

    def verificar_hora_modo_noche(self):
        hora_actual = datetime.now().hour
        modo_fiesta, modo_noche = self.consultar_automatizaciones()

        if modo_fiesta or modo_noche:
            return False
        if hora_actual != self._hora_activacion_modo_noche:
            return False
        return True

    """Esta funcion mantiene sincronizados los datos entre la logica del programa
    y los registros en la base de datos mysql"""
    def _sincronizar_estado_dispositivo(self, dispositivo: Dispositivo):
        try:
            dispositivos_db = self._dispositivo_dao.find_by_nombre(dispositivo.nombre)
            if dispositivos_db:
                id_dispositivo = dispositivos_db[0]["ID_dispositivo"]
                self._dispositivo_dao.set_estado(id_dispositivo, dispositivo.estado)
        except Exception as error:
            return f"Advertencia: No se pudo sincronizar dispositivo '{dispositivo.nombre}': {error}"