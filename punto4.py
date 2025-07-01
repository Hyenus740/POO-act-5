class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion, tamaño_equipo):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.tamaño_equipo = tamaño_equipo
        self.programadores = []

    def esta_lleno(self):
        return len(self.programadores) >= self.tamaño_equipo

    def añadir_programador(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(programador)

    @staticmethod
    def validar_campo(campo, nombre_del_campo="Campo"):
        if any(caracter.isdigit() for caracter in campo):
            raise Exception(f"{nombre_del_campo} no puede tener dígitos.")
        if len(campo) > 20:
            raise Exception(f"{nombre_del_campo} no debe superar los 20 caracteres.")

    @staticmethod
    def validar_tamaño_equipo(valor):
        if not valor.isdigit():
            raise Exception("El tamaño del equipo debe ser un número entero.")
        entero = int(valor)
        if entero < 2 or entero > 3:
            raise Exception("El equipo debe tener entre 2 y 3 integrantes.")
        return entero

def main():
    try:
        nombre_equipo = input("Nombre del equipo: ")
        EquipoMaratonProgramacion.validar_campo(nombre_equipo, "Nombre del equipo")

        universidad = input("Universidad: ")
        EquipoMaratonProgramacion.validar_campo(universidad, "Universidad")

        lenguaje = input("Lenguaje de programación: ")
        EquipoMaratonProgramacion.validar_campo(lenguaje, "Lenguaje de programación")

        tamaño_str = input("Tamaño del equipo (2 a 3 integrantes): ")
        tamaño_equipo = EquipoMaratonProgramacion.validar_tamaño_equipo(tamaño_str)

        equipo = EquipoMaratonProgramacion(nombre_equipo, universidad, lenguaje, tamaño_equipo)

        print("\nDatos de los integrantes del equipo:")
        for i in range(tamaño_equipo):
            print(f"\nIntegrante {i + 1}")
            nombre = input("Nombre del integrante: ")
            EquipoMaratonProgramacion.validar_campo(nombre, "Nombre del integrante")

            apellidos = input("Apellidos del integrante: ")
            EquipoMaratonProgramacion.validar_campo(apellidos, "Apellidos del integrante")

            programador = Programador(nombre, apellidos)
            equipo.añadir_programador(programador)

        print("\n Equipo registrado exitosamente con los siguientes integrantes:")
        for p in equipo.programadores:
            print(f"- {p.nombre} {p.apellidos}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
