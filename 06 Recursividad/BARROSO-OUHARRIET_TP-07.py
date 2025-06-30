# PRACTICO 11: RECURSIVIDAD
#-------------------------------------------------------------------------#
# Alumno: Nikolas Barroso
# PD: este trabajo fue realizado con jupyter y luego exportado a Python.
#-------------------------------------------------------------------------#
# --- Actividades ---

# --EJERCICIO 1--
print("\n1. FACTORIAL")
print("-" * 20)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # llamada a la funcion recursiva

numero = int(input("Ingrese un número: "))
print(f"\nFactoriales desde 1 hasta {numero}:")
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")

# --EJERCICIO 2--
print("\n\n2. SERIE DE FIBONACCI")
print("-" * 20)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # llamada a la funcion recursiva

posicion = int(input("Ingrese hasta qué posición mostrar Fibonacci: "))
print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")

# --EJERCICIO 3--
print("\n\n3. POTENCIA")
print("-" * 20)

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)  # llamada a la funcion recursiva

base = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))
resultado = potencia(base, exp)
print(f"{base}^{exp} = {resultado}")

# --EJERCICIO 4--
print("\n\n4. CONVERSIÓN A BINARIO")
print("-" * 20)

def binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return binario(n // 2) + str(n % 2)  # llamada a la funcion recursiva

numero = int(input("Ingrese un número decimal: "))
resultado = binario(numero)
print(f"El número {numero} en binario es: {resultado}")

# --EJERCICIO 5--
print("\n\n5. VERIFICAR PALÍNDROMO")
print("-" * 20)

def palindromo(palabra):
    palabra = palabra.lower()
    
    if len(palabra) <= 1:
        return True
    
    if palabra[0] == palabra[-1]:
        return palindromo(palabra[1:-1])  # llamada a la funcion recursiva
    else:
        return False

palabra = input("Ingrese una palabra: ")
if palindromo(palabra):
    print(f"'{palabra}' ES un palíndromo")
else:
    print(f"'{palabra}' NO es un palíndromo")

# --EJERCICIO 6--
print("\n\n6. SUMA DE DÍGITOS")
print("-" * 20)

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)  # llamada a la funcion recursiva

numero = int(input("Ingrese un número: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")

# --EJERCICIO 7--
print("\n\n7. CONTAR BLOQUES DE PIRÁMIDE")
print("-" * 20)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)  # llamada a la funcion recursiva

nivel = int(input("Ingrese bloques en el nivel más bajo: "))
total = contar_bloques(nivel)
print(f"Total de bloques necesarios: {total}")

# --EJERCICIO 8--
print("\n\n8. CONTAR DÍGITO ESPECÍFICO")
print("-" * 20)

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    
    ultimo = numero % 10
    resto = numero // 10
    
    if ultimo == digito:
        return 1 + contar_digito(resto, digito)  # llamada a la funcion recursiva
    else:
        return contar_digito(resto, digito)  # llamada a la funcion recursiva

numero = int(input("Ingrese un número: "))
digito = int(input("Ingrese el dígito a buscar (0-9): "))
cantidad = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {cantidad} veces en {numero}")

print("\n" + "="*50)
print("FIN DEL PRÁCTICO")
print("="*50)