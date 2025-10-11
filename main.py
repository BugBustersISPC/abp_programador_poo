from app.dao.ubicacion_dao import UbicacionDAO

def listar_ubicaciones_por_vivienda():
    """Lista todas las ubicaciones de una vivienda específica"""
    
    # Crear instancia del DAO
    dao = UbicacionDAO()
    
    # Pedir ID de vivienda al usuario
    print("=" * 60)
    print("LISTAR UBICACIONES DE UNA VIVIENDA")
    print("=" * 60)
    
    try:
        id_vivienda = int(input("\nIngrese el ID de la vivienda: "))
        
        # Obtener ubicaciones
        ubicaciones = dao.obtener_por_vivienda(id_vivienda)
        
        if ubicaciones:
            print(f"\n Se encontraron {len(ubicaciones)} ubicaciones:\n")
            print(f"{'ID':<5} {'Nombre':<25} {'ID Vivienda':<15}")
            print("-" * 50)
            
            for ub in ubicaciones:
                print(f"{ub.id:<5} {ub.nombre:<25} {ub.id_vivienda:<15}")
                
                # Mostrar dispositivos si los tiene
                dispositivos = ub.obtener_dispositivos()
                if dispositivos:
                    print(f"      └─ Dispositivos: {', '.join(dispositivos)}")
        else:
            print(f"\n No se encontraron ubicaciones para la vivienda ID={id_vivienda}")
            
    except ValueError:
        print("Error: Debes ingresar un número válido")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    listar_ubicaciones_por_vivienda()