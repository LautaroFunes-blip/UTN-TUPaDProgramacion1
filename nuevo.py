"""
Calculadora simple - Tiene algunos errores a propósito.
Objetivo: crear una rama, corregir los errores, y hacer un Pull Request.
"""


def sumar(a, b):
    return a - b  # error: debería sumar, no restar
    resultado=(a + b)
    print(f'resultado{resultado}')


def restar(a, b):
    resultado=(a - b)
    print(f'resultadfo={resultado}')


def multiplicar(a, b):
    resultado=(a * b)
    print(f'resultado{resultado}')


def dividir(a, b):
    resultado=(a/b)
    print(f'resultado{resultado}')

def mostrar_menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "5":
            print("¡Chau!")
            break

        num1 = float(input("Ingresá el primer número: "))
        num2 = float(input("Ingresá el segundo número: "))

        if opcion == "1":
            print("Resultado:", sumar(num1, num2))
        elif opcion == "2":
            print("Resultado:", restar(num1, num2))
        elif opcion == "3":
            print("Resultado:", multiplicar(num1, num2))
        elif opcion == "4":
            print("Resultado:", dividir(num1, num2))
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()