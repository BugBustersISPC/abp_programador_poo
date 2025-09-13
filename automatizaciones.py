from datetime import datetime

class Automatizaciones:
    def __init__(self, dispositivos):
        self.dispositivos = dispositivos
        self.hora_activacion_modo_noche = 23

    def consultar_automatizaciones(self):
        luces_equipomusica = [dispositivo["estado"] for dispositivo in self.dispositivos if dispositivo["tipo"] in (2, 3)]
        modo_fiesta = all(luces_equipomusica) if luces_equipomusica else False

        camaras = [dispositivo["estado"] for dispositivo in self.dispositivos if dispositivo["tipo"] == 1]
        modo_noche = any(camaras) if camaras else False

        return modo_fiesta, modo_noche

    def mostrar_estado(self):
        modo_fiesta, modo_noche = self.consultar_automatizaciones()
        estado_fiesta = "On" if modo_fiesta else "Off"
        estado_noche = "On" if modo_noche else "Off"
        return f"Estado de Automatizaciones: - Modo Fiesta: {estado_fiesta} / - Modo Noche: {estado_noche}"

    
    def activar_modo_fiesta(self):
        for dispositivo in self.dispositivos:
            if dispositivo["tipo"] in [2, 3] and dispositivo["estado"] == False:
                dispositivo["estado"] = True
        return "Modo Fiesta activado: Equipo de Musica y Luces encendidas."
    
    def apagar_modo_fiesta(self):
        for dispositivo in self.dispositivos:
            if dispositivo["tipo"] in [2, 3] and dispositivo["estado"] == True:
                dispositivo["estado"] = False
        return "Modo fiesta desactivado: Equipo de Musica y Luces apagadas."
    
    def activar_modo_noche(self):
        for dispositivo in self.dispositivos:
            if dispositivo["tipo"] in [2,3] and dispositivo["estado"] == True:
                dispositivo["estado"] = False
            if dispositivo["tipo"] == 1 and dispositivo["estado"] == False:
                dispositivo["estado"] = True
        return "Modo noche activado: Camaras encendidas, equipo de musica y luces apagadas."
    def apagar_modo_noche(self):
        for dispositivo in self.dispositivos:
            if dispositivo["tipo"] == 1 and dispositivo["estado"] == True:
                dispositivo["estado"] = False
        return "Modo noche desactivado: Camaras apagadas."
    
    def configurar_hora_modo_noche(self, nueva_hora: int):
        if nueva_hora < 0 or nueva_hora > 23:
            return False
        self.hora_activacion_modo_noche = nueva_hora
        return True

    def verificar_hora_modo_noche(self):
        hora_actual = datetime.now().hour
        modo_fiesta, modo_noche = self.consultar_automatizaciones()

        if modo_fiesta or modo_noche:
            return False
        if hora_actual != self.hora_activacion_modo_noche:
            return False
        return True