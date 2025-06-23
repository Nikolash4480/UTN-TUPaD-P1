"""
Práctico 2: Funciones en Python

Objetivo:
Comprender y aplicar el uso de funciones en la programación, desarrollando algoritmos
que implementen modularidad, reutilización de código y una organización estructurada
para resolver problemas.
"""

# --- Actividades ---

"""
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: "Hola Mundo!".
Llamar a esta función desde el programa principal.
"""
def imprimir_hola_mundo():
    print("Hola Mundo!")

if __name__ == "__main__":
    print("--- Ejercicio 1 ---")
    imprimir_hola_mundo()


"""
2. Crear una función llamada saludar_usuario (nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
volver: "Hola Marcos!".
Llamar a esta función desde el programa principal solicitando el nombre al usuario.
"""
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

if __name__ == "__main__":
    nombre_usuario = input("Por favor, ingresa tu nombre: ")
    mensaje_saludo = saludar_usuario(nombre_usuario)
    print(mensaje_saludo)


"""
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: "Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]".
Pe-dir los datos al usuario y llamar a esta función con los valores in-
gresados.
"""
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    try:
        edad = int(input("Ingresa tu edad: "))
    except ValueError:
        edad = "dato inválido" # Manejo básico para edad no numérica
        print("Edad ingresada no es un número. Se mostrará como 'dato inválido'.")
    residencia = input("Ingresa tu lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)


"""
4. Crear dos funciones: calcular_area_circulo (radio) que reciba el ra-
dio como parámetro y devuelva el área del círculo.
calcular_peri-metro_circulo(radio) que reciba el radio como parámetro y devuel-
va el perímetro del círculo.
Solicitar el radio al usuario y llamar am-bas funciones para mostrar los resultados.
"""
import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

if __name__ == "__main__":
    try:
        radio = float(input("Ingresa el radio del círculo: "))
        if radio < 0:
            print("El radio no puede ser negativo.")
        else:
            area = calcular_area_circulo(radio)
            perimetro = calcular_perimetro_circulo(radio)
            print(f"El área del círculo es: {area:.2f}")
            print(f"El perímetro del círculo es: {perimetro:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número para el radio.")


"""
5. Crear una función llamada segundos_a_horas (segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes.
Solicitar al usuario los segundos y mos-trar el resultado usando esta función.
"""
def segundos_a_horas(segundos):
    return segundos / 3600

if __name__ == "__main__":
    try:
        segundos = int(input("Ingresa una cantidad de segundos: "))
        if segundos < 0:
            print("La cantidad de segundos no puede ser negativa.")
        else:
            horas = segundos_a_horas(segundos)
            print(f"{segundos} segundos equivalen a {horas:.2f} horas.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero para los segundos.")


"""
6. Crear una función llamada tabla_multiplicar (numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun-ción.
"""
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

if __name__ == "__main__":
    try:
        numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
        tabla_multiplicar(numero)
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

"""
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta-do
de sumarlos, restarlos, multiplicarlos y dividirlos.
Mostrar los re-sultados de forma clara.
"""
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = None
    if b != 0:
        division = a / b
    return (suma, resta, multiplicacion, division)

if __name__ == "__main__":
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        resultados = operaciones_basicas(num1, num2)
        print(f"Resultados de las operaciones básicas para {num1} y {num2}:")
        print(f"Suma: {resultados[0]}")
        print(f"Resta: {resultados[1]}")
        print(f"Multiplicación: {resultados[2]}")
        if resultados[3] is not None:
            print(f"División: {resultados[3]}")
        else:
            print("División: No se puede dividir por cero.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa números válidos.")


"""
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC).
Solicitar al usuario los datos y llamar a la fun-ción para mostrar el resultado con dos decimales.
"""
def calcular_imc(peso, altura):
    if altura <= 0:
        return None
    return peso / (altura ** 2)

if __name__ == "__main__":
    try:
        peso = float(input("Ingresa tu peso en kilogramos (ej. 70.5): "))
        altura = float(input("Ingresa tu altura en metros (ej. 1.75): "))

        if peso <= 0:
            print("El peso debe ser un valor positivo.")
        elif altura <= 0:
            print("La altura debe ser un valor positivo.")
        else:
            imc = calcular_imc(peso, altura)
            if imc is not None:
                print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
            else:
                print("No se pudo calcular el IMC. Asegúrate de que la altura sea válida.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa números válidos para peso y altura.")

"""
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit.
Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    try:
        celsius = float(input("Ingresa la temperatura en grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número para la temperatura.")

"""
10. Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

if __name__ == "__main__":
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        num3 = float(input("Ingresa el tercer número: "))

        promedio = calcular_promedio(num1, num2, num3)
        print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa números válidos.")