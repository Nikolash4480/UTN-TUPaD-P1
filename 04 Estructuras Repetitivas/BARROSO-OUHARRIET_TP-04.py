# PRACTICO 4: ESTRUCTURAS REPETITIVAS
#-------------------------------------------------------------------------#
# Alumno: Nikolas Barroso
# PD: este trabajo fue realizado con jupyter y luego exportado a Python.
#-------------------------------------------------------------------------#

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
  print(i)  

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = int(input("Digite um número: "))
cantidad = len(str(numero))
print(f"El número {numero} tiene {cantidad} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Digite el primer número: "))
num2 = int(input("Digite el segundo número: "))

contador = 0
for i in range(num1 + 1, num2):
    contador += i

print(f"La suma entre los numeros comprendidos es de {contador}.")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0
while numero != 0:
    numero = int(input("Ingrese un número (0 para salir): "))
    suma += numero


print(f"La suma de los números es {suma}.")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

from random import randint
numero_aleatorio = randint(0, 9)
intentos = 0
intento = 0

while intento != numero_aleatorio:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == numero_aleatorio:
        print(f"Felicidades, acertaste el numero {numero_aleatorio} en {intentos} intentos.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

numero = 100
while numero != 0:
  numero -= 2
  print(numero)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero = int(input("Ingrese un número: "))
suma = 0

for i in range(0, numero + 1):
    suma += i
    print(suma)

print(f"La suma de los números del 0 al {numero} es {suma}.")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

contador = 0
pares = 0
impares = 0
negativos = 0
positivos = 0

while contador < 10:
  numero = int(input("Ingrese un número: "))
  contador += 1

  if numero >= 0:
    positivos += 1
  elif numero < 0:
    negativos += 1

  if numero % 2 == 0:
    pares += 1
  else:
    impares += 1

print(f"La cantidad de números positivos es: {positivos}\n"
      f"La cantidad de números negativos es: {negativos}\n"
      f"La cantidad de números pares es: {pares}\n"
      f"La cantidad de números impares es: {impares}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

contador = 0
suma = 0

while contador < 10:
  numero = int(input("Ingrese un numero:"))
  print(numero)
  suma += numero
  contador += 1

print(f"La media de los numeros es {suma / contador}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = str(input("Ingrese un número: "))
num_invertido = ""

for i in range(len(numero)):
  num_invertido += numero[-(i + 1)]

print(f"El número invertido es: {num_invertido}")