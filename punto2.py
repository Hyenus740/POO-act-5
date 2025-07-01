class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = None

    def imprimir(self):
        print("Nombre del vendedor =", self.nombre)
        print("Apellidos del vendedor =", self.apellidos)
        print("Edad del vendedor =", self.edad)

    def verificar_edad(self, edad):
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        if 0 <= edad < 120:
            self.edad = edad
        else:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")

def main():
    try:
        nombre = input("Nombre del vendedor = ")
        apellidos = input("Apellidos del vendedor = ")
        vendedor = Vendedor(nombre, apellidos)
        edad = int(input("Edad del vendedor = "))
        vendedor.verificar_edad(edad)
        vendedor.imprimir()
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()