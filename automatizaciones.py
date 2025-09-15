from datetime import datetime
from dispositivo import Dispositivo

class Automatizaciones:
    def __init__(self, dispositivos: list[Dispositivo]):
        if not all(isinstance(dispositivo, Dispositivo) for dispositivo in dispositivos):
            raise ValueError("Todos los elementos deben ser objetos de la clase Dispositivo.")
        self._dispositivos = dispositivos
        self._hora_activacion_modo_noche = 23

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
        for dispositivo in self._dispositivos:
            if dispositivo.tipo in [Dispositivo.TIPO_LUZ, Dispositivo.TIPO_MUSICA] and not dispositivo.estado:
                dispositivo.encender()
        return "Modo Fiesta activado: Equipo de Musica y Luces encendidas."
    
    def apagar_modo_fiesta(self):
        for dispositivo in self._dispositivos:
            if dispositivo.tipo in (Dispositivo.TIPO_LUZ, Dispositivo.TIPO_MUSICA) and dispositivo.estado:
                dispositivo.apagar()
        return "Modo fiesta desactivado: Equipo de Musica y Luces apagadas."
    
    def activar_modo_noche(self):
        for dispositivo in self._dispositivos:
            if dispositivo.tipo == Dispositivo.TIPO_CAMARA and dispositivo.estado:
                dispositivo.encender
        return "Modo noche activado: Camaras encendidas."
    def apagar_modo_noche(self):
        for dispositivo in self._dispositivos:
            if dispositivo.tipo == Dispositivo.TIPO_CAMARA and dispositivo.estado:
                dispositivo.apagar()
        return "Modo noche desactivado: Camaras apagadas."
    
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