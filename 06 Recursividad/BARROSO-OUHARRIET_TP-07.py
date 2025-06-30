# PRACTICO 7: RECURSIVIDAD
#-------------------------------------------------------------------------#
# Alumno: Nikolas Barroso
# PD: este trabajo fue realizado con jupyter y luego exportado a Python.
#-------------------------------------------------------------------------#

# --- Actividades ---
"""
Práctico 7: Aplicación de la Recursividad

Objetivo:

Comprender el uso de recursividad en problemas matemáticos simples.
"""

# EJERCICIO 1: Factorial
print("\n1. FACTORIAL")
print("-" * 30)

def factorial(n):
    """
    Función recursiva que calcula el factorial de un número.
    Caso base: factorial(0) = 1 y factorial(1) = 1
    Caso recursivo: factorial(n) = n * factorial(n-1)
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Programa principal para el factorial
try:
    numero = int(input("Ingrese un número para calcular factoriales desde 1 hasta ese número: "))
    if numero < 1:
        print("Por favor, ingrese un número mayor a 0")
    else:
        print(f"\nFactoriales desde 1 hasta {numero}:")
        for i in range(1, numero + 1):
            print(f"{i}! = {factorial(i)}")
except ValueError:
    print("Error: Ingrese un número entero válido")

# EJERCICIO 2: Fibonacci
print("\n\n2. SERIE DE FIBONACCI")
print("-" * 30)

def fibonacci(n):
    """
    Función recursiva que calcula el valor de Fibonacci en la posición n.
    Caso base: fib(0) = 0, fib(1) = 1
    Caso recursivo: fib(n) = fib(n-1) + fib(n-2)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Programa principal para Fibonacci
try:
    posicion = int(input("Ingrese la posición hasta donde mostrar la serie de Fibonacci: "))
    if posicion < 0:
        print("Por favor, ingrese un número no negativo")
    else:
        print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
        for i in range(posicion + 1):
            print(f"F({i}) = {fibonacci(i)}")
except ValueError:
    print("Error: Ingrese un número entero válido")

# EJERCICIO 3: Potencia
print("\n\n3. POTENCIA")
print("-" * 30)

def potencia(base, exponente):
    """
    Función recursiva que calcula base^exponente.
    Caso base: base^0 = 1
    Caso recursivo: base^n = base * base^(n-1)
    """
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Programa principal para potencia
try:
    base = int(input("Ingrese la base: "))
    exp = int(input("Ingrese el exponente: "))
    if exp < 0:
        print("Este algoritmo solo funciona con exponentes no negativos")
    else:
        resultado = potencia(base, exp)
        print(f"{base}^{exp} = {resultado}")
except ValueError:
    print("Error: Ingrese números enteros válidos")

# EJERCICIO 4: Conversión a binario
print("\n\n4. CONVERSIÓN A BINARIO")
print("-" * 30)

def decimal_a_binario(n):
    """
    Función recursiva que convierte un número decimal a binario.
    Caso base: si n == 0, devolver "0"
    Caso recursivo: decimal_a_binario(n//2) + str(n%2)
    """
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Programa principal para conversión binaria
try:
    numero = int(input("Ingrese un número decimal positivo para convertir a binario: "))
    if numero < 0:
        print("Por favor, ingrese un número positivo")
    else:
        binario = decimal_a_binario(numero)
        print(f"El número {numero} en binario es: {binario}")
except ValueError:
    print("Error: Ingrese un número entero válido")

# EJERCICIO 5: Palíndromo
print("\n\n5. VERIFICAR PALÍNDROMO")
print("-" * 30)

def es_palindromo(palabra):
    """
    Función recursiva que verifica si una palabra es palíndromo.
    Caso base: si la palabra tiene 0 o 1 caracteres, es palíndromo
    Caso recursivo: comparar primer y último carácter, y verificar el resto
    """
    # Convertir a minúsculas para comparar
    palabra = palabra.lower()
    
    # Caso base: palabra vacía o de un carácter
    if len(palabra) <= 1:
        return True
    
    # Comparar primer y último carácter
    if palabra[0] == palabra[-1]:
        # Si coinciden, verificar la palabra sin el primer y último carácter
        return es_palindromo(palabra[1:-1])
    else:
        return False

# Programa principal para palíndromo
palabra_input = input("Ingrese una palabra (sin espacios ni tildes): ")
if es_palindromo(palabra_input):
    print(f"'{palabra_input}' ES un palíndromo")
else:
    print(f"'{palabra_input}' NO es un palíndromo")

# EJERCICIO 6: Suma de dígitos
print("\n\n6. SUMA DE DÍGITOS")
print("-" * 30)

def suma_digitos(n):
    """
    Función recursiva que suma todos los dígitos de un número.
    Caso base: si n < 10, devolver n
    Caso recursivo: (n % 10) + suma_digitos(n // 10)
    """
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Programa principal para suma de dígitos
try:
    numero = int(input("Ingrese un número entero positivo: "))
    if numero < 0:
        numero = abs(numero)  # Trabajar con valor absoluto
        print(f"Trabajando con el valor absoluto: {numero}")
    
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")
except ValueError:
    print("Error: Ingrese un número entero válido")

# EJERCICIO 7: Contar bloques de pirámide
print("\n\n7. CONTAR BLOQUES DE PIRÁMIDE")
print("-" * 30)

def contar_bloques(n):
    """
    Función recursiva que cuenta el total de bloques en una pirámide.
    Caso base: si n == 1, devolver 1
    Caso recursivo: n + contar_bloques(n-1)
    """
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Programa principal para contar bloques
try:
    nivel_base = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide: "))
    if nivel_base < 1:
        print("El número debe ser mayor a 0")
    else:
        total_bloques = contar_bloques(nivel_base)
        print(f"Total de bloques necesarios para la pirámide: {total_bloques}")
except ValueError:
    print("Error: Ingrese un número entero válido")

# EJERCICIO 8: Contar dígito específico
print("\n\n8. CONTAR DÍGITO ESPECÍFICO")
print("-" * 30)

def contar_digito(numero, digito):
    """
    Función recursiva que cuenta cuántas veces aparece un dígito en un número.
    Caso base: si numero == 0, devolver 0
    Caso recursivo: comparar último dígito y continuar con el resto del número
    """
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10
    resto_numero = numero // 10
    
    if ultimo_digito == digito:
        return 1 + contar_digito(resto_numero, digito)
    else:
        return contar_digito(resto_numero, digito)

# Programa principal para contar dígito
try:
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese el dígito a contar (0-9): "))
    
    if numero < 0:
        numero = abs(numero)
        print(f"Trabajando con el valor absoluto: {numero}")
    
    if digito < 0 or digito > 9:
        print("El dígito debe estar entre 0 y 9")
    else:
        cantidad = contar_digito(numero, digito)
        print(f"El dígito {digito} aparece {cantidad} veces en {numero}")
except ValueError:
    print("Error: Ingrese números enteros válidos")

print("\n" + "="*60)
print("FIN DEL PRÁCTICO")
print("="*60)