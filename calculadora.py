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


if __name__ == "__main__":
    presentacion()

    print("Suma:", sumar(10, 5))
    print("Resta:", restar(10, 5))