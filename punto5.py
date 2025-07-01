class LeerArchivo:

    @staticmethod
    def main():
        nombre_archivo = "prueba.txt"  # Definición del archivo de texto a leer
        
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                # Lee línea por línea
                for linea in archivo:
                    print(linea, end='')  # Imprime la línea (end='' evita dobles saltos)
                    
        except FileNotFoundError:
            print("No se pudo encontrar el archivo.")
        except IOError:
            print("No se pudo leer el archivo.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

# Ejecutar el método main
if __name__ == "__main__":
    LeerArchivo.main()