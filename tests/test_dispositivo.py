import unittest
from dispositivo import Dispositivo 

class TestDispositivo(unittest.TestCase):
    
    def test_creacion_dispositivo_valido(self):
        dispositivo = Dispositivo(nombre="Luz Living", tipo=Dispositivo.TIPO_LUZ, estado=False)
        self.assertEqual(dispositivo.nombre, "Luz Living")
        self.assertEqual(dispositivo.tipo, 2)
        self.assertEqual(dispositivo.estado, False)
        
    def test_creacion_falla_por_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Dispositivo(nombre="", tipo=Dispositivo.TIPO_LUZ, estado=True)
            
    def test_creacion_falla_por_tipo_invalido(self):
        with self.assertRaises(ValueError):
            Dispositivo(nombre="Dispositivo Raro", tipo=99, estado=True)
            
    def test_cambiar_estado(self):
        dispositivo = Dispositivo(nombre="Cámara Jardín", tipo=Dispositivo.TIPO_CAMARA, estado=False)
        self.assertFalse(dispositivo.estado)
        
        # Probamos encender
        dispositivo.encender()
        self.assertTrue(dispositivo.estado)
        
        # Probamos apagar
        dispositivo.apagar()
        self.assertFalse(dispositivo.estado)
        
    def test_falla_al_cambiar_estado_con_valor_no_booleano(self):
        dispositivo = Dispositivo(nombre="Parlante", tipo=Dispositivo.TIPO_MUSICA, estado=True)
        with self.assertRaises(ValueError):
            dispositivo.estado = "apagado"

    def test_representacion_string(self):
        disp_on = Dispositivo("Luz RGB", Dispositivo.TIPO_LUZ, True)
        disp_off = Dispositivo("Alarma", Dispositivo.TIPO_CAMARA, False)
        
        self.assertEqual(str(disp_on), "Luz RGB (Tipo: Luz) - Estado: On")
        self.assertEqual(str(disp_off), "Alarma (Tipo: Cámara) - Estado: Off")

if __name__ == '__main__':
    unittest.main()