# PRACTICO 11: RECURSIVIDAD
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

# --- Actividades ---

"""
1. Crea una función recursiva que calcule el factorial de un número.
Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario.
"""
def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

if __name__ == "__main__":
    try:
        numero_usuario = int(input("Ingresa un número entero para calcular su factorial y los anteriores: "))
        if numero_usuario < 0:
            print("El factorial no está definido para números negativos.")
        else:
            print(f"Factoriales desde 1 hasta {numero_usuario}:")
            for i in range(1, numero_usuario + 1):
                print(f"El factorial de {i} es: {factorial_recursivo(i)}")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")


"""
2. Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
"""
def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

if __name__ == "__main__":
    try:
        posicion_fibonacci = int(input("Ingresa la posición hasta la cual quieres ver la serie de Fibonacci: "))
        if posicion_fibonacci < 0:
            print("La posición debe ser un número no negativo.")
        else:
            print(f"Serie de Fibonacci hasta la posición {posicion_fibonacci}:")
            for i in range(posicion_fibonacci + 1):
                print(f"F({i}) = {fibonacci_recursivo(i)}")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")


"""
3. Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula $n^{m}=n*n^{(m-1)}$.
Prueba esta función en un algoritmo general.
"""
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        # Manejo de exponentes negativos: a^-n = 1 / (a * a^(n-1))
        return 1 / (base * potencia_recursiva(base, abs(exponente) - 1))
    else:
        return base * potencia_recursiva(base, exponente - 1)

if __name__ == "__main__":
    try:
        base_num = float(input("Ingresa la base: "))
        exponente_num = int(input("Ingresa el exponente: "))
        
        resultado_potencia = potencia_recursiva(base_num, exponente_num)
        print(f"{base_num} elevado a la {exponente_num} es: {resultado_potencia}")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa números válidos.")


"""
4. Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
procedimiento:

1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
"""
def decimal_a_binario_recursivo(decimal):
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"
    else:
        resto = decimal % 2
        cociente = decimal // 2
        return decimal_a_binario_recursivo(cociente) + str(resto)

if __name__ == "__main__":
    try:
        num_decimal = int(input("Ingresa un número entero positivo en base decimal para convertirlo a binario: "))
        if num_decimal < 0:
            print("Por favor, ingresa un número entero positivo.")
        else:
            binario_resultante = decimal_a_binario_recursivo(num_decimal)
            print(f"El número {num_decimal} en binario es: {binario_resultante}")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")


"""
5. Implementá una función recursiva llamada es_palindromo (palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
"""
def es_palindromo(palabra):
    palabra = palabra.lower()
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False

if __name__ == "__main__":
    texto = input("Ingresa una palabra (sin espacios ni tildes) para verificar si es un palíndromo: ")
    if es_palindromo(texto):
        print(f"'{texto}' es un palíndromo.")
    else:
        print(f"'{texto}' no es un palíndromo.")


"""
6. Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un

número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
"""
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

if __name__ == "__main__":
    try:
        num_suma = int(input("Ingresa un número entero positivo para sumar sus dígitos: "))
        if num_suma < 0:
            print("Por favor, ingresa un número entero positivo.")
        else:
            resultado_suma_digitos = suma_digitos(num_suma)
            print(f"La suma de los dígitos de {num_suma} es: {resultado_suma_digitos}")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")


"""
7. Un niño está construyendo una pirámide con bloques.
En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos $(n-1),$ y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
"""
def contar_bloques(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

if __name__ == "__main__":
    try:
        bloques_base = int(input("Ingresa el número de bloques en el nivel más bajo de la pirámide: "))
        if bloques_base < 0:
            print("El número de bloques no puede ser negativo.")
        else:
            total_bloques = contar_bloques(bloques_base)
            print(f"Para una pirámide con {bloques_base} bloques en la base, se necesitan un total de {total_bloques} bloques.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")


"""
8. Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un

número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces

aparece ese dígito dentro del número.
"""
def contar_digito(numero, digito):
    if numero < 0:
        numero = abs(numero)

    if numero == 0:
        return 1 if digito == 0 else 0
    
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        ultimo_digito = numero % 10
        contador = 1 if ultimo_digito == digito else 0
        return contador + contar_digito(numero // 10, digito)

if __name__ == "__main__":
    try:
        num_contar = int(input("Ingresa un número entero positivo: "))
        digito_buscar = int(input("Ingresa el dígito (entre 0 y 9) que deseas contar: "))
        
        if not (0 <= digito_buscar <= 9):
            print("El dígito a buscar debe estar entre 0 y 9.")
        elif num_contar < 0:
            print("El número debe ser entero positivo.")
        else:
            apariciones = contar_digito(num_contar, digito_buscar)
            print(f"El dígito {digito_buscar} aparece {apariciones} veces en el número {num_contar}.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa números enteros.")