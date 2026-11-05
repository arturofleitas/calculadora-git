# calculadora.py

def presentacion():
    print("====================================")
    print("     CALCULADORA MODULAR EN PYTHON")
    print("====================================")


# Funcion para sumar dos numeros
def sumar(a, b):
    return a + b


# Funcion para restar dos numeros
def restar(a, b):
    return a - b


# Funcion para multiplicar dos numeros
def multiplicar(a, b):
    return a * b


# Funcion para dividir dos numeros
def dividir(a, b):
    if b == 0:
        return "Error: no es posible dividir entre cero"
    return a / b


if __name__ == "__main__":
    presentacion()

    print("Suma:", sumar(10, 5))
    print("Resta:", restar(10, 5))
    print("Multiplicacion:", multiplicar(10, 5))
    print("Division:", dividir(10, 5))
    print("Division entre cero:", dividir(10, 0))