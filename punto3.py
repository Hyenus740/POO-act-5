import math

def calcular_logaritmo_neperiano(valor):
    try:
        if valor < 0:
            raise ArithmeticError("El valor debe ser un número positivo para calcular el logaritmo.")
        resultado = math.log(valor)
        print(f"Logaritmo neperiano: {resultado}")
    except ArithmeticError as ae:
        print(ae)
    except ValueError:
        print("El valor debe ser numérico para calcular el logaritmo.")

def calcular_raiz_cuadrada(valor):
    try:
        if valor < 0:
            raise ArithmeticError("El valor debe ser un número positivo para calcular la raíz cuadrada.")
        resultado = math.sqrt(valor)
        print(f"Raíz cuadrada: {resultado}")
    except ArithmeticError as ae:
        print(ae)
    except ValueError:
        print("El valor debe ser numérico para calcular la raíz cuadrada.")

def main():
    try:
        valor = float(input("Ingrese un valor numérico: "))
        calcular_logaritmo_neperiano(valor)
        calcular_raiz_cuadrada(valor)
    except ValueError:
        print("Debe ingresar un valor numérico válido.")

if __name__ == "__main__":
    main()
