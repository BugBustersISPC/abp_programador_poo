class Automatizaciones:
    def __init__(self, dispositivos):
        self.dispositivos = dispositivos

    def consultar_automatizaciones(self):
        modo = True
        for dispositivo in self.dispositivos:
            if dispositivo["tipo"] == 1 and dispositivo["estado"] == False:
                modo = False
                break

        estado_modo = "On" if modo else "Off"

        return f"Estado de Automatizaciones: - Modo: {estado_modo}"
    
    def activar_modo(self):
        for dispositivo in self.dispositivos:
            if dispositivo["tipo"] == 1 and dispositivo["estado"] == False:
                dispositivo["estado"] = True
        return "Modo activado"
    
    def apagar_modo(self):
        for dispositivo in self.dispositivos:
            if dispositivo["tipo"] == 1 and dispositivo["estado"] == True:
                dispositivo["estado"] = False
        return "Modo apagado"