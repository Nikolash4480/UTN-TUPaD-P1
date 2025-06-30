# %% [markdown]
# {
#  "cells": [
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "# Práctico 2: Funciones en Python\n",
#     "\n",
#     "**Objetivo:**\n",
#     "\n",
#     "Comprender y aplicar el uso de funciones en la programación, desarrollando algoritmos que implementen modularidad, reutilización de código y una organización estructurada para resolver problemas. \n",
#     "\n",
#     "---"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "## Actividades:\n",
#     "\n",
#     "**1. Crear una función llamada `imprimir_hola_mundo` que imprima por pantalla el mensaje: \"Hola Mundo!\".  Llamar a esta función desde el programa principal. **"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "def imprimir_hola_mundo():\n",
#     "    print(\"Hola Mundo!\")\n",
#     "\n",
#     "if __name__ == \"__main__\":\n",
#     "    imprimir_hola_mundo()"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "**2. Crear una función llamada `saludar_usuario (nombre)` que reciba como parámetro un nombre y devuelva un saludo personalizado.  Por ejemplo, si se llama con `saludar_usuario(\"Marcos\")`, deberá devolver: \"Hola Marcos!\".  Llamar a esta función desde el programa principal solicitando el nombre al usuario. **"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "def saludar_usuario(nombre):\n",
#     "    return f\"Hola {nombre}!\"\n",
#     "\n",
#     "if __name__ == \"__main__\":\n",
#     "    nombre_usuario = input(\"Por favor, ingresa tu nombre: \")\n",
#     "    mensaje_saludo = saludar_usuario(nombre_usuario)\n",
#     "    print(mensaje_saludo)"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "**3. Crear una función llamada `informacion_personal(nombre, apellido, edad, residencia)` que reciba cuatro parámetros e imprima: \"Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]\".  Pedir los datos al usuario y llamar a esta función con los valores ingresados. **"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "def informacion_personal(nombre, apellido, edad, residencia):\n",
#     "    print(f\"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.\")\n",
#     "\n",
#     "if __name__ == \"__main__\":\n",
#     "    nombre = input(\"Ingresa tu nombre: \")\n",
#     "    apellido = input(\"Ingresa tu apellido: \")\n",
#     "    edad = int(input(\"Ingresa tu edad: \"))\n",
#     "    residencia = input(\"Ingresa tu lugar de residencia: \")\n",
#     "    informacion_personal(nombre, apellido, edad, residencia)"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "**4. Crear dos funciones: `calcular_area_circulo (radio)` que reciba el radio como parámetro y devuelva el área del círculo.  `calcular_perimetro_circulo(radio)` que reciba el radio como parámetro y devuelva el perímetro del círculo.  Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados. **"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "import math\n",
#     "\n",
#     "def calcular_area_circulo(radio):\n",
#     "    return math.pi * (radio ** 2)\n",
#     "\n",
#     "def calcular_perimetro_circulo(radio):\n",
#     "    return 2 * math.pi * radio\n",
#     "\n",
#     "if __name__ == \"__main__\":\n",
#     "    try:\n",
#     "        radio = float(input(\"Ingresa el radio del círculo: \"))\n",
#     "        if radio < 0:\n",
#     "            print(\"El radio no puede ser negativo.\")\n",
#     "        else:\n",
#     "            area = calcular_area_circulo(radio)\n",
#     "            perimetro = calcular_perimetro_circulo(radio)\n",
#     "            print(f\"El área del círculo es: {area:.2f}\")\n",
#     "            print(f\"El perímetro del círculo es: {perimetro:.2f}\")\n",
#     "    except ValueError:\n",
#     "        print(\"Entrada inválida. Por favor, ingresa un número para el radio.\")"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "**5. Crear una función llamada `segundos_a_horas (segundos)` que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes.  Solicitar al usuario los segundos y mostrar el resultado usando esta función. **"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "def segundos_a_horas(segundos):\n",
#     "    return segundos / 3600\n",
#     "\n",
#     "if __name__ == \"__main__\":\n",
#     "    try:\n",
#     "        segundos = int(input(\"Ingresa una cantidad de segundos: \"))\n",
#     "        if segundos < 0:\n",
#     "            print(\"La cantidad de segundos no puede ser negativa.\")\n",
#     "        else:\n",
#     "            horas = segundos_a_horas(segundos)\n",
#     "            print(f\"{segundos} segundos equivalen a {horas:.2f} horas.\")\n",
#     "    except ValueError:\n",
#     "        print(\"Entrada inválida. Por favor, ingresa un número entero para los segundos.\")"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "**6. Crear una función llamada `tabla_multiplicar (numero)` que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10.  Pedir al usuario el número y llamar a la función. **"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "def tabla_multiplicar(numero):\n",
#     "    print(f\"Tabla de multiplicar del {numero}:\")\n",
#     "    for i in range(1, 11):\n",
#     "        print(f\"{numero} x {i} = {numero * i}\")\n",
#     "\n",
#     "if __name__ == \"__main__\":\n",
#     "    try:\n",
#     "        numero = int(input(\"Ingresa un número para ver su tabla de multiplicar: \"))\n",
#     "        tabla_multiplicar(numero)\n",
#     "    except ValueError:\n",
#     "        print(\"Entrada inválida. Por favor, ingresa un número entero.\")"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "**7. Crear una función llamada `operaciones_basicas(a, b)` que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.  Mostrar los resultados de forma clara. **"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "def operaciones_basicas(a, b):\n",
#     "    suma = a + b\n",
#     "    resta = a - b\n",
#     "    multiplicacion = a * b\n",
#     "    division = None\n",
#     "    if b != 0:\n",
#     "        division = a / b\n",
#     "    return (suma, resta, multiplicacion, division)\n",
#     "\n",
#     "if __name__ == \"__main__\":\n",
#     "    try:\n",
#     "        num1 = float(input(\"Ingresa el primer número: \"))\n",
#     "        num2 = float(input(\"Ingresa el segundo número: \"))\n",
#     "\n",
#     "        resultados = operaciones_basicas(num1, num2)\n",
#     "        print(f\"Resultados de las operaciones básicas para {num1} y {num2}:\")\n",
#     "        print(f\"Suma: {resultados[0]}\")\n",
#     "        print(f\"Resta: {resultados[1]}\")\n",
#     "        print(f\"Multiplicación: {resultados[2]}\")\n",
#     "        if resultados[3] is not None:\n",
#     "            print(f\"División: {resultados[3]}\")\n",
#     "        else:\n",
#     "            print(\"División: No se puede dividir por cero.\")\n",
#     "    except ValueError:\n",
#     "        print(\"Entrada inválida. Por favor, ingresa números válidos.\")"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "**8. Crear una función llamada `calcular_imc(peso, altura)` que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC).  Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales. **"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "def calcular_imc(peso, altura):\n",
#     "    if altura <= 0:\n",
#     "        return None\n",
#     "    return peso / (altura ** 2)\n",
#     "\n",
#     "if __name__ == \"__main__\":\n",
#     "    try:\n",
#     "        peso = float(input(\"Ingresa tu peso en kilogramos (ej. 70.5): \"))\n",
#     "        altura = float(input(\"Ingresa tu altura en metros (ej. 1.75): \"))\n",
#     "\n",
#     "        if peso <= 0:\n",
#     "            print(\"El peso debe ser un valor positivo.\")\n",
#     "        elif altura <= 0:\n",
#     "            print(\"La altura debe ser un valor positivo.\")\n",
#     "        else:\n",
#     "            imc = calcular_imc(peso, altura)\n",
#     "            if imc is not None:\n",
#     "                print(f\"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}\")\n",
#     "            else:\n",
#     "                print(\"No se pudo calcular el IMC. Asegúrate de que la altura sea válida.\")\n",
#     "    except ValueError:\n",
#     "        print(\"Entrada inválida. Por favor, ingresa números válidos para peso y altura.\")"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "**9. Crear una función llamada `celsius_a_fahrenheit(celsius)` que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.  Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función. **"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "def celsius_a_fahrenheit(celsius):\n",
#     "    return (celsius * 9/5) + 32\n",
#     "\n",
#     "if __name__ == \"__main__\":\n",
#     "    try:\n",
#     "        celsius = float(input(\"Ingresa la temperatura en grados Celsius: \"))\n",
#     "        fahrenheit = celsius_a_fahrenheit(celsius)\n",
#     "        print(f\"{celsius}°C equivalen a {fahrenheit:.2f}°F.\")\n",
#     "    except ValueError:\n",
#     "        print(\"Entrada inválida. Por favor, ingresa un número para la temperatura.\")"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "**10. Crear una función llamada `calcular_promedio(a, b, c)` que reciba tres números como parámetros y devuelva el promedio de ellos.  Solicitar los números al usuario y mostrar el resultado usando esta función. **"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "def calcular_promedio(a, b, c):\n",
#     "    return (a + b + c) / 3\n",
#     "\n",
#     "if __name__ == \"__main__\":\n",
#     "    try:\n",
#     "        num1 = float(input(\"Ingresa el primer número: \"))\n",
#     "        num2 = float(input(\"Ingresa el segundo número: \"))\n",
#     "        num3 = float(input(\"Ingresa el tercer número: \"))\n",
#     "\n",
#     "        promedio = calcular_promedio(num1, num2, num3)\n",
#     "        print(f\"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}\")\n",
#     "    except ValueError:\n",
#     "        print(\"Entrada inválida. Por favor, ingresa números válidos.\")"
#    ]
#   }
#  ],
#  "metadata": {
#   "kernelspec": {
#    "display_name": "Python 3",
#    "language": "python",
#    "name": "python3"
#   },
#   "language_info": {
#    "codemirror_mode": {
#     "name": "ipython",
#     "version": 3
#    },
#    "file_extension": ".py",
#    "mimetype": "text/x-python",
#    "name": "python",
#    "nbconvert_exporter": "python",
#    "pygments_lexer": "ipython3",
#    "version": "3.9.7"
#   }
#  },
#  "nbformat": 4,
#  "nbformat_minor": 4
# }


